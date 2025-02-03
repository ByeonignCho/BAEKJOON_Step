import sys
input = sys.stdin.readline

def main() :
   
   a = input().split()
   list1 = input().split() 
   for i in range(int(a[0])):
       if int(list1[i]) < int(a[1]) :
           print(list1[i], end = " ")
   
if __name__ == "__main__" :
    
    main()