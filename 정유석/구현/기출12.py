def check(answer):
    for x, y, structure in answer: 
        # 기둥(0)
        if structure == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보(1)
        elif structure == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            if [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
            return False
    return True
    
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, structure, oper = frame
        # 설치
        if oper == 1:
            answer.append([x, y, structure])
            if not check(answer):
                answer.remove([x, y, structure])
        # 삭제
        else:
            answer.remove([x, y, structure])
            if not check(answer):
                answer.append([x, y, structure])
        #print(answer)
    answer = sorted(answer)
    return answer