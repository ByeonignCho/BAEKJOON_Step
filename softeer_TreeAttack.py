import sys
n, m = sys.stdin.readline().rstrip().split()
n = int(n)
m = int(m)
grid = []
for i in range(n):
    a = sys.stdin.readline().rstrip().split()
    grid.append(a)
for _ in range(2):
    L, R = sys.stdin.readline().rstrip().split()
    L = int(L)
    R = int(R)
    LR = [ 1 for _ in range(4)]
    for i in range(L-1,R):
        for k in range(m):
            if grid[i][k]=='1':
                grid[i][k]='0'
                break
cnt =  0
for i in range(n):
    cnt1 = grid[i].count('1')
    cnt+= cnt1
print(cnt)