
def solution(progresses, speeds):
    answer = []
    temp = []
    for i in range(len(progresses)):
        finish = 100
        rest = (finish - progresses[i])
        if(rest % speeds[i] != 0):
            rest_days = rest//speeds[i] + 1
        else:
            rest_days = rest//speeds[i]
        temp.append(rest_days) # 7 3 9
        print(temp)
    finish = temp[0]
    count = 1
    for i in range(1, len(temp)):
        if finish < temp[i]:
            answer.append(count)
            finish = temp[i] # 포인터 temp[i]로 초기화
            count = 1 # 카운트 1로 다시 초기화
        else:
            count+=1
    answer.append(count)
    print(answer)
    return answer
solution([93, 30, 55],[1, 30, 5])

