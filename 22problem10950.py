a = int(input())
ans = []
for i in range(a):
    b, c = map(int, input().split())
    ans.append(b + c)
# 배열 뽑기기
for i in range(len(ans)): 
    print(ans[i])