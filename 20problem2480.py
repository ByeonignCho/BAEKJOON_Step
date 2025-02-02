a, b, c = map(int, input().split())
b1 = a == b == c
b2 = b == c
b3 = a == c
b4 = a == b
if b1 :
    print(10000+a*1000)
elif b2 :
    print(1000+b*100)
elif b3 : 
    print(1000+a*100)
elif b4 : 
    print(1000+a*100)
elif not b2 and not b3 and not b4 :
    if a > b :
        if a > c :
            print(a*100)
        else : 
            print(c*100)
    else : 
        if b > c :
            print(b*100)
        else : 
            print(c*100)
"""
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(max(a, b, c)*100) # max()함수 사용
"""