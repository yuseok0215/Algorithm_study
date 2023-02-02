import sys
input = sys.stdin.readline

s = input().rstrip()

zero_cnt = 0 # 0문자열 개수
one_cnt = 0 # 1문자열 개수

if s[0] == '0':
    zero_cnt = 1
else:
    one_cnt = 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1': # 0->1  0000111000
            one_cnt += 1
        else:
            zero_cnt += 1

print(min(zero_cnt, one_cnt))
