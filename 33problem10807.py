import sys
input = sys.stdin.readline
def main() :
   a = int(input().rstrip())
   list = input().split()  # input() 쓸거면 list(map(int, input().split())
   f = input().rstrip()
   num = list.count(f) # 시간복잡도 O(n) 루프와 동일, C언어 구현 함수라 조금 더 빠름름 
   print(num)

if __name__ == "__main__" :
    main()