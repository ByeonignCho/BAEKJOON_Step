a = int(input())
ans = []
for i in range(a):
    b, c = map(int, input().split())
    ans.append(b + c)

for i in range(len(ans)): 
    print("Case #{}: {}".format(i+1, ans[i]))