# 아직 하는 중중
import sys
n = int(sys.stdin.readline().rstrip())
matrix=[]
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(row)
ans = [[0 for _ in range(n)] for _ in range(n)]


def find(list, num):
    for i in range(len(list)):
        if list[i]==num:
            return i

while(1):
    c = 0
    num = 1
    while(1):
        idx = find(matrix[c], 1)
        ans[c][idx] = num
        
        
        






# 결과 
for i in range(n):
    for k in range(n):
        print(ans[i][k],end=' ')
    print()
    
    