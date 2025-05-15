import sys
# 12점 받음 시간초과과
in_put = list(map(int, sys.stdin.readline().rstrip().split()))
matrix = []

for i in range(in_put[0]):
    row = sys.stdin.readline().rstrip()
    matrix.append(row)
cnt = 0
for i in range(in_put[0]):
    for k in range(i+1,in_put[0]):
        differ = 0
        for j in range(in_put[1]):
            if (matrix[i][j]!=matrix[k][j]):
                differ+=1
            if ((j==in_put[1]-1)and(differ<3)):
                cnt += 1
        
print(cnt)