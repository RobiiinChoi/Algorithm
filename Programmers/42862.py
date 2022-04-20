def solution(n, lost, reserve):
    answer = 0
    # 여벌의 체육복을 가져왔으나 도난당했을 케이스 소거
    reserved_set = set(reserve)-set(lost)
    lost_set = set(lost)-set(reserve

    for i in reserved_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    return n-len(lost_set)