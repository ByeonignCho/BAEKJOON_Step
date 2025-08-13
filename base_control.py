from math  import asin, cos, radians, sin
import rospy
from std_msgs.msg import Float64

import LaneMap
import Vehicle
from LaneMap import LaneType
from Subscribers import VehicleStatus
from utils import calcDistance


class base_control:
    def __init__(self):
        #self.VEHICLE_WIDTH = 0.2
        #self.VEHICLE_LENGTH = 0.43
        self.VEHICLE_WHEEL_BASE = 0.25 # m (0.36162852)
        self.STEER_MAX = 19.48
        self.STEER_MIN = -19.48
        #self.RATE_HZ = 30
        #self.MAX_SPEED = 10000

speed_pub = rospy.Publisher("commands/motor/speed", Float64, queue_size = 1)
steer_pub = rospy.Publisher("commands/servo/position", Float64, queue_size = 1)

def brake():
    accel(0)

def accel(speed=SPEED):
    """
    set speed
    speed : Float 64 
    return : None
    """
    speed_pub.publish(speed)
