def solution(n, stages):
    length = len(stages)

    arr = []
    for i in range(1,n+1):
        cnt = stages.count(i)

        if length == 0:
            tmp = 0
        else:
            tmp = cnt/length

        arr.append([i,tmp])
        length -= cnt
    
    arr = sorted(arr, key=lambda x:x[1], reverse=True)

    result = []
    
    for i in range(len(arr)):
        result.append(arr[i][0])

    return result

n = int(input())
arr = [2,1,2,6,2,4,3,3]

a = solution(n,arr)

print(a)