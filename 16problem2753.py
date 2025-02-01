a= int(input())
if a%4==0 and a%100!=0 or a%400==0 :# boolean 에서 a and b or c == (a and b) or c
    print(1)
else:
    print(0)