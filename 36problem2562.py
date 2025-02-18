import sys
input = sys.stdin.readline

def main():
   max = 0
   idx = 0

   for i in range(1,10):
      a = int(input().rstrip())
      if a >= max :
          max = a
          idx = i 
   print("{}\n{}".format(max, idx))

if __name__ == "__main__" :
    main()
   