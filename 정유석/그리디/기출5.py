n,m = map(int, input().split())
w = list(map(int, input().split()))

arr = [0] * 11

for i in w:
    arr[i] += 1

result = 0
for i in range(1, m+1):
    n -= arr[i]
    result += arr[i] * n

print(result)