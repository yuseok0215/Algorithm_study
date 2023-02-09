s = input()

result = []
_sum = 0
for elem in s:
    if elem.isalpha():
        result.append(elem)
    else:
        _sum += int(elem)

result.sort()
result.append(str(_sum))

print(''.join(result))