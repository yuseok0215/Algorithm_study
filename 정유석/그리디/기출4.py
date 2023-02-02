n = int(input())
coins = list(map(int, input().split))
coins.sort()

num = 1 # 만들 수 있는지 확인할 숫자
for coin in coins:
    if num < coin:
        break
    num += coin