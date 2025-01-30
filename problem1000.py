"""
a, b =input().split() 
print(int(a)+int(b)) # input함수는 string으로 받기 때문에 int() 하기
"""
a, b = map(int, input().split())  # 입력 받은 값을 정수로 변환
print(a + b)