if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        command = input().split()[0]
        b = set(map(int, input().split()))
        getattr(a, command)(b)
    print(sum(a))