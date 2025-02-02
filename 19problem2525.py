h, m = map(int, input().split())
t = int(input())
def min2hour(h, m):
    while m >= 60 :
        m = m - 60
        h = h + 1
    return h, m
m = m + t
h, m = min2hour(h, m)
if h >= 24 :
    h = h - 24

print("{} {}".format(h, m))
