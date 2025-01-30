a = input()
b = input()
a = int(a)
ans = []
ans.append(a*int(b[2]))
ans.append(a*int(b[1]))
ans.append(a*int(b[0]))
ans.append(a*int(b))
for i in ans:
    print(i)
