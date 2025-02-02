"""
a = int(input())
ans = []
oper1 = []
oper2 = []
for i in range(a):
    b, c = map(int, input().split())
    oper1.append(b)
    oper2.append(c)
    ans.append(b + c)

for i in range(len(ans)): 
    print("Case #{}: {} + {} = {}".format(i+1, oper1[i], oper2[i], ans[i]))
"""
import sys
num = sys.stdin.readline().rstrip()
ans = []
oper1 = []
oper2 = []
for i in range(int(num)):
    a = sys.stdin.readline().rstrip()
    n = a.split()
    oper1.append(n[0])
    oper2.append(n[1])
    ans.append(int(n[0])+int(n[1]))
for i in range(int(num)):
    sys.stdout.write("Case #{}: {} + {} = {}\n".format(i+1, oper1[i], oper2[i], ans[i]))