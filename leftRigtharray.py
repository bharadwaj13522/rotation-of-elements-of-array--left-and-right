n = list(map(int, input().split()))
k = int(input())

k = k % len(n)

for i in range(k):
    x = n.pop(-1)
    n.insert(0, x)
print(*n)
