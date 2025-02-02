"""
#시간초과 걸림
num = int(input())
ans = []
for i in range(num):
    a, b = map(int, input().split())
    ans.append(a + b)

for i in range(len(ans)): 
    print(ans[i])
"""
# sys.stdin.readline() 은 \n까지 받기 때문에 .rstrip()으로 제거해줘야 한다.
# .split() 으로 공백을 기준으로 행렬원소로 만든다.
# sys.stdout.write() 은 print()보다 빠르며 \n가 포함되어 있지 않다.
import sys
num = sys.stdin.readline().rstrip() 
ans = []
for i in range(int(num)):
    a = sys.stdin.readline().rstrip()
    res = a.split()
    ans.append(int(res[0])+int(res[1]))

for i in range(len(ans)): 
    sys.stdout.write("{}\n".format(ans[i]))