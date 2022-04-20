def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        # 배열을 정렬했으므로 같은 인덱스로 값이 나오지 않을 경우, 참가자에서 해당 인덱스 값을 리턴
        if(participant[i] != completion[i]):
            print(completion[i])
            print(participant[i])
            return participant[i]

    # 전체를 비교했는데, 다른 값이 없을 경우 참가자의 맨 마지막 값이 없는 경우이므로 길이의 -1로 리턴
    return participant[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))