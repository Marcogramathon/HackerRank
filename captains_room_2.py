import collections
K = int(input())
l1 = list(map(int, input().split()))
d = collections.Counter(l1)
s = min(d, key = d.get)

print(s)