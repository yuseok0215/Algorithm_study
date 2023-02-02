n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

cnt = 0
result = 0
for i in range(m):
    if cnt == k:
        cnt = 0
        result += nums[1]
        continue
    
    result += nums[0]
    cnt += 1

print(result)
