import sys
a = sys.stdin.readline().rstrip()
add1 = []
addplus = []
for i in range(len(a)-1):
    if a[i] =='(':
        if a[i+1]==')':
            print('(1',end='')
        elif a[i+1]=='(':
            print('(',end='')
    if a[i]==')':
        if a[i+1]=='(':
            print(')+',end='')
        elif a[i+1]==')':
            print(')',end='')
print(')')


