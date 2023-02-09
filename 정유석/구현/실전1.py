str_ = input() # a1

row = int(ord(str_[0])) - int(ord('a')) + 1
column = int(str_[1])

# 총 갈 수 있는 횟수
dx = [1,-1,1,-1,-2,-2,2,2]
dy = [2,2,-2,-2,1,-1,1,-1]

cnt = 0
for i in range(8):
    nx = row + dx[i]
    ny = column + dy[i]

    if 1<=nx<=8 and 1<=ny<=8:
        cnt += 1

print(cnt)


