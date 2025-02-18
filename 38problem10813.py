import sys

input = sys.stdin.readline

def main() :

   N, M = map(int, input().split())
   arr = list(range(1, N+1))

   for _ in range(M) : 
      i, j = map(int, input().split()) # sys.stdin이여도 map가능능
      temp = arr[i-1]
      arr[i-1] = arr[j-1]
      arr[j-1] = temp

   for i in arr :
      print(i, end = " ")

if __name__ == "__main__" :
    
    main()
