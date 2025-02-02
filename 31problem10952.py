t = 1
ans = []
while t == 1 :
    a, b = map(int, input().split())
    if a == b == 0:
        break 
    ans.append(a+b)
for i in range(len(ans)):
    print(ans[i])