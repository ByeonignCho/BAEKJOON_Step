import sys
matrix =[]
for i in range(3):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(row)
cost=[]
for i in range(3):
    cost.append(max(matrix[i]) - min(matrix[i]))
    
    
for i in range(3):
    col = [matrix[j][i] for j in range(3)]
    cost.append(max(col) - min(col))

cost.sort()
print(cost[0])