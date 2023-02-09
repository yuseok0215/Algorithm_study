def solution(food_times, k):
    #food_times = [3,1,2]
    food_length = len(food_times) #3
    print(food_length)
    
    i=0
    count = 0
    answer = 0
    
    while(count != k):
        if(food_times[i%3]-1 < 0):
            count -= 1
        else:
            count += 1
            food_times[i%3] = food_times[i%3]-1  
        answer = i%3 + 1
        i += 1
    
    return answer