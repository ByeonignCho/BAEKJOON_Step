import sys
num = int(sys.stdin.readline().rstrip())
ans = []



for _ in range(num):
    in_put = list(map(int, sys.stdin.readline().rstrip().split('.')))
    ans.append(in_put)
idx = []
iter = list(range(num))

ans.sort()


for i in range(num):
    if len(ans[i])==2:
        print("{}.{}".format(ans[i][0],ans[i][1]))
    elif len(ans[i])==1:
        print("{}".format(ans[i][0]))

