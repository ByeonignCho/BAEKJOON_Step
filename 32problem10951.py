
import sys
input = sys.stdin.readline
ans = []
while True:

  try:

     a, b = map(int, input().split())

     ans.append(a + b)

  except:

     break
  
for i in range(len(ans)):
   
   print("{}".format(ans[i]))