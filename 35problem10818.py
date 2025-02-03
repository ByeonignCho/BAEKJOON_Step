import sys
input = sys.stdin.readline

def main() :

   a = input().rstrip()
   list1 = input().split()
   min = int(list1[0])
   max = int(list1[0])
   for i in range(int(a)):
      if int(list1[i]) < min :
           min = int(list1[i])
      if int(list1[i]) > max :
           max = int(list1[i])
   print(min, max)
   
if __name__ == "__main__" :
    
    main()