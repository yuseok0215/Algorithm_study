n,m = map(int, input().split())
cards = []
for _ in range(n):
    cards.append(list(map(int, input().split())))

max_ = 0
for i in range(n):
    min_ = 10001
    for j in range(m):
        if min_ > cards[i][j]:
            min_ = cards[i][j]
    max_ = max(min_, max_)

print(max_)     