T = int(input())
for i in range(T):
    na = int(input())
    A = list(map(int, input().split()))
    nb = int(input())
    B = list(map(int, input().split()))
    subset = True
    for j in A:
        if j not in B:
            subset = False
    print(subset)