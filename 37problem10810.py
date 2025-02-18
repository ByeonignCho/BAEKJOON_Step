import sys

input = sys.stdin.readline

def main() :

   N, M = map(int, input().split()) # sys.stdin이여도 map가능
   arr = [0] * N
   for _ in range(M) : 
      i, j, k = map(int, input().split())
      arr[i-1:j] = [k]*(j-i+1)

   for i in arr :
      print(i, end = " ")

if __name__ == "__main__" :
    
    main()
