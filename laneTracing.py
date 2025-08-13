#!/usr/bin/env python3
#-*- coding:utf-8-*-
# rostopic info /image_jpeg/compressed -> sensor_msgs/CompressedImage

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np
from std_msgs.msg import Float64
import time
import Vehicle
from Subscribers import Lidar, TrafficLight, Camera
from enum import Enum
#from math import sqrt
from typing import Tuple
import cv2


image_msg = CompressedImage()
image = np.empty(shape=[0])
binary_img = np.empty(shape=[0])
bridge = CvBridge()
flag = True
steer_msg = Float64()
speed_msg = Float64()
#=============================================
# 콜백함수 - 카메라 토픽을 처리하는 콜백함수
# 카메라 이미지 토픽이 도착하면 자동으로 호출되는 함수
# 토픽에서 이미지 정보를 꺼내 image 변수에 옮겨 담음.
# img shape는 480.640.3
#=============================================
def cam_CB(msg):
    global image_msg
    global image
    global binary_img

    image_msg = bridge.compressed_imgmsg_to_cv2(msg)
    #cv2.imshow("image", image_msg)
    #cv2.waitKey(1)
    img = image_msg.copy()

#=============================================
# 정면을 바라보는 카메라 이미지를 위에서 보는
# bird eye view 로 transform 하는 부분
#=============================================
    y, x = image_msg.shape[0:2]
    """
    src_point1 = [270, 260] # 왼쪽 위
    src_point2 = [x-270, 260] # 오른쪽 위
    src_point3 = [0, y] # 왼쪽 아래
    src_point4 = [x, y] # 오른쪽 아래
    """

    src_point1 = [210, 300] # 왼쪽 위
    src_point2 = [x-210, 300] # 오른쪽 위
    src_point3 = [20, 420] # 왼쪽 아래
    src_point4 = [620, 420] # 오른쪽 아래
    src_points = np.float32([src_point1, src_point2, src_point3, src_point4])
    dst_point1 = [0, 0]
    dst_point2 = [x, 0]
    dst_point3 = [0, y]
    dst_point4 = [x, y]
    dst_points = np.float32([dst_point1, dst_point2, dst_point3, dst_point4])

    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    image = cv2.warpPerspective(img, matrix, [x, y])
    #cv2.imshow("Brid_eye_view",image)
    #cv2.waitKey(1)

#=============================================
# 이미지를 그레이스케일로 바꾸고 이진화하여
# 이미지상에 차선만 남게하는 함수
#=============================================

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    """ 방법 1
# 이미지를 binarization 하는 과정
    threshold = 200
    maxValue = 255
    _, white_img = cv2.threshold(gray, threshold, maxValue, cv2.THRESH_BINARY)

    # 노란차선
    yellow_lower = np.array([15, 128, 0])
    yellow_upper = np.array([40, 255, 250])
    yellow_img = cv2.inRange(hsv, yellow_lower, yellow_upper)

    binary_img = cv2.bitwise_or(white_img, yellow_img)
    """

    #방법 2
    # 흰색 차선 (채도 낮고, 명도 높은 영역)
    white_lower = np.array([0, 0, 200])
    white_upper = np.array([179, 50, 255])
    white_mask = cv2.inRange(hsv, white_lower, white_upper)

# 노란색 차선
    yellow_lower = np.array([15, 100, 100])
    yellow_upper = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

# 합치기
    combined_mask = cv2.bitwise_or(white_mask, yellow_mask)

# 노이즈 제거
    kernel = np.ones((5,5), np.uint8)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)

    binary_img = combined_mask

    #cv2.imshow("combined_range", binary_img) 
    #cv2.imshow("binary image__", binary_img)
    #cv2.waitKey(1)

    kernel = np.ones((5,5),np.uint8)

# 이미지에서 차선 외에 다른 sign이 인식되지 않도록 
# 도로 사인을 검출하기 위해 corner가 5개 이상인
# 다각형을 검출하여 마스킹 처리하는 과정
    
    contours, _ = cv2.findContours(binary_img,cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
    for cont in contours:
        approx = cv2.approxPolyDP(cont, cv2.arcLength(cont,True) * 0.02, True)
        vtc = len(approx)
        
        if vtc >= 5:
            sign_mask = make_mask(binary_img, cont)
            binary_img = binary_img - sign_mask
    
    binary_img = cv2.dilate(binary_img,kernel, iterations = 2)
    # 차선 검출 이미지
    #cv2.imshow("result", binary_img)
    #cv2.waitKey(1)
    return binary_img

# processing img => binary_img
# bev img => image
def sliding_window(binary_img, image):

    global pre_lx
    global pre_rx
    global pre_left_x
    global pre_right_x
    global flag 
    nwindows = 15
    margin = 30
    minpix = 30
    histogram = np.sum(binary_img[binary_img.shape[0]//2:,:], axis=0)      
    midpoint = np.int32(histogram.shape[0]/2)
    leftx_current = np.argmax(histogram[:midpoint])
    rightx_current = np.argmax(histogram[midpoint:]) + midpoint

    left_0 = np.max(histogram[:midpoint])
    right_0 = np.max(histogram[midpoint:])

    if(rightx_current == 320):
        rightx_current = 640

    window_height = np.int32(binary_img.shape[0]/nwindows)
    nz = binary_img.nonzero()

    left_lane_inds = []
    right_lane_inds = []
    
    lx, ly, rx, ry = [], [], [], []

    # out_img = np.dstack((binary_img, binary_img, binary_img))*255
    out_img = binary_img

    for window in range(nwindows):

        win_yl = binary_img.shape[0] - (window+1)*window_height
        win_yh = binary_img.shape[0] - window*window_height

        win_xll = leftx_current - margin
        win_xlh = leftx_current + margin
        win_xrl = rightx_current - margin
        win_xrh = rightx_current + margin

        cv2.rectangle(out_img,(win_xll,win_yl),(win_xlh,win_yh),(0,255,0), 2) 
        cv2.rectangle(out_img,(win_xrl,win_yl),(win_xrh,win_yh),(0,255,0), 2) 

        good_left_inds = ((nz[0] >= win_yl)&(nz[0] < win_yh)&(nz[1] >= win_xll)&(nz[1] < win_xlh)).nonzero()[0]
        good_right_inds = ((nz[0] >= win_yl)&(nz[0] < win_yh)&(nz[1] >= win_xrl)&(nz[1] < win_xrh)).nonzero()[0]

        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)

        if len(good_left_inds) > minpix:
            leftx_current = np.int32(np.mean(nz[1][good_left_inds]))
        if len(good_right_inds) > minpix:        
            rightx_current = np.int32(np.mean(nz[1][good_right_inds]))

        if(left_0==0):
            lx.append(pre_lx[window])
        else:
            lx.append(leftx_current)
        ly.append(int((win_yl + win_yh)/2))

        if(right_0==0):
            rx.append(pre_rx[window])
        else:
            rx.append(rightx_current)
        ry.append(int((win_yl + win_yh)/2))

        mid_y = int((win_yl + win_yh)/2)
        image = cv2.line(image, (leftx_current,mid_y), (leftx_current,mid_y), (255, 255, 255), 10)
        image = cv2.line(image, (rightx_current,mid_y), (rightx_current,mid_y), (255, 255, 255), 10)


    left_lane_inds = np.concatenate(left_lane_inds)
    right_lane_inds = np.concatenate(right_lane_inds)


# 이전 sliding window된 값에서 너무 크게 벗어날 경우 
    # 너무 튀는 값이라고 판단하고 sliding window 중점의 
    # 평균에서 제외시키는 과정

    cnt_l = 0
    cnt_r = 0

    temp_l = 0
    temp_r = 0

    target_x = 320
    left_x = 0
    right_x = 640
    sum_left_x = 0
    sum_right_x = 0

    # 처음 슬라이딩 윈도우가 돌때 pre 값을 설정하기 위해 flag 사용

    if(flag):  
        pre_lx = lx
        pre_rx = rx
        for i in range(nwindows):
            temp_l = temp_l + lx[i]
        left_x = temp_l / nwindows

        for i in range(nwindows):
            temp_r = temp_r + rx[i]
        right_x = temp_r / nwindows

        flag = False

    for i in range(nwindows):
        if(lx[i]==0):
            lx[i] = pre_lx[i]

        sum_left_x = sum_left_x + lx[i]
        cnt_l = cnt_l + 1
        image = cv2.line(image, (lx[i],ly[i]), (lx[i],ly[i]), (0, 0, 255), 10)
        if(rx[i]==0):
            rx[i] = pre_rx[i]
            
        sum_right_x = sum_right_x + rx[i]
        cnt_r = cnt_r + 1
        image = cv2.line(image, (rx[i],ry[i]), (rx[i],ry[i]), (0, 0, 255), 10)




    if(cnt_l==0):
        left_x = pre_left_x
    else:
        left_x = sum_left_x / cnt_l

    if(cnt_r==0):
        right_x = pre_right_x
    else:
        right_x = sum_right_x / cnt_r

        
    target_x = (left_x + right_x) / 2
    image = cv2.line(image, (320,0), (320,480), (0, 120, 255), 3)
    image = cv2.line(image, (int(target_x),240), (int(target_x),240), (0, 255, 255), 5)

    pre_lx = lx
    pre_rx = rx
    pre_left_x = left_x
    pre_right_x = right_x
    # 켜야함
    cv2.imshow("bird_img", image)
    cv2.waitKey(1)
    
    return target_x, image




#=============================================
# 카메라 이미지 상에 불필요한 이미지를 지우기 위해
# 마스크를 만드는 함수
#=============================================
def make_mask(image, pts):

    mask = np.zeros(image.shape, dtype=np.uint8)

    (x, y, w, h) = cv2.boundingRect(pts)
    roi_corners = np.array([pts], dtype=np.int32)
    w = (255, 255, 255)
    cv2.fillPoly(mask, roi_corners, w)
    crop = cv2.bitwise_and(image, mask)
    return crop



#=============================================
# imu 센서를 통해 얻은 yaw값을 통하여
# 원하는 지점과의 차이인 yaw error를 계산하고
# PID 제어에서 P 제어를 통하여
#=============================================
def getYawError(x):

    yaw_error = ((x - 320) / 32000.0) * 100.0
    yaw_error += 0.5
    return yaw_error



def main():
    global image_msg
    rospy.init_node("turtle_sub_mode")
    warped = rospy.Subscriber("/image_jpeg/compressed",CompressedImage,cam_CB)
    rospy.wait_for_message("/image_jpeg/compressed", CompressedImage)
    steer = 0
    speed = 0
    
    try:
        while not rospy.is_shutdown():
            cv2.imshow("bird_img", image)
            cv2.waitKey(1)
            cv2.imshow("image", image_msg)
            cv2.waitKey(1)
            target_x,line_img = sliding_window(binary_img,image)
            steer = getYawError(target_x)
            Vehicle.steer(steer)
            Vehicle.accel(1000)
            
            #pass
            
        
    except rospy.ROSInterruptException:
        pass



if __name__ == "__main__" :
    pre_lx = [0]*15
    pre_rx = [0]*15
    pre_left_x = 106
    pre_right_x = 550
    main()
