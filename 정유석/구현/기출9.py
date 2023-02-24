def solution(s):
    answer = len(s)
    # 1~mid 까지 검사    
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:i] # 초기 문자를 설정
        count = 1
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(i, len(s), i):
            # 초기 문자와 동일하다면
            if prev == s[j:j+i]:
                count += 1
            else:
                # if count >= 2:
                #     compressed += str(count) + prev 
                # else:
                #     compressed += prev
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+i] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대한 처리
        # if count >= 2:
        #     compressed += str(count) + prev 
        # else:
        #     compressed += prev
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer