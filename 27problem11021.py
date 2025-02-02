"""
a = int(input())
ans = []
for i in range(a):
    b, c = map(int, input().split())
    ans.append(b + c)

for i in range(len(ans)): 
    print("Case #{}: {}".format(i+1, ans[i]))
"""
import sys
num = sys.stdin.readline().rstrip()
ans = []
for i in range(int(num)):
    a = sys.stdin.readline().rstrip()
    n = a.split()
    ans.append(int(n[0])+int(n[1]))
for i in range(int(num)):
    sys.stdout.write("Case #{}: {}\n".format(i+1, ans[i]))