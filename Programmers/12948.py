def solution(phone_number):
    answer = ''
    count = len(phone_number)-4
    temp = phone_number[-4:]
    answer=(count*'*') + temp
    print(answer)
    return answer

solution('01033334444')