food_times = list(map(int, input().split()))
k = int(input())


def solution(food_times, k):
    time = 0 # 0~1초
    dish_idx = 0

    if sum(food_times) <= k: # 3 1 2   k=6
        print(-1)
        return

    while time < k:
        if food_times[dish_idx] != 0: # 접시에 음식이 있을때
            food_times[dish_idx] -= 1
            time += 1
        
        dish_idx += 1    

        if dish_idx == len(food_times):
            dish_idx = 0     

            # 0 1 0
            # dish_idx = 0
    

    while True:
        if food_times[dish_idx] != 0:
            return print(dish_idx+1)
        
        dish_idx += 1

        if dish_idx == len(food_times):
            dish_idx = 0
        

        

solution(food_times, k)
    

            
        

        
        