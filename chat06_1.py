

def isPalaindrm(str):

    # 홀수는 가운데 숫자들을 볼 필요가 없고 짝수는 동일하게 나눠짐
    # i는 앞에서 시작하는 포인터
    # j는 뒤에서 역순으로 진행되는 포인터
    # 초기값 설정 (예외처리 - 대소문자 구분x, 영문자와 숫자를 대상으로 함)
    # 영문자 , 숫자 대상 (isalnum(), alphabet+number)
    # 1-1 ) 영문자와 숫자인 문자열만 타겟으로 보겠다 ( 만약 특수기호가 들어가면 False)
    # 1-2 ) 만약에 특수기호가 들어가면 특수기호는 무시하고 보겠다 mom => palindrome

    str = str.lower()
    # str.lower()
    # if not str.isalnum():
    #     return False

    # li = [10, 20, 50, 30, 0]
    # li_sort1 = li.sort() 리턴값 있음
    # li_sort2 = sorted(li) 리턴값 없음

        i = 0
        j = -i-1
        isPalin = True
        while True:

        if str[i].isalnum() and str[j].isalnum():
            if str[i] != str[-i - 1]:
                isPalin = False
                break;

    isPalin = True
    for i in range(len(str)//2):
        print('inner: ', 1)
        # j = len(str)-1-i
        if str[i].isalnum() and str[-i-1].isalnum():

        if str[i] != str[-i-1]:
            isPalin = False
            break;
    return isPalin

if __name__ == "__main__" :
    isPalaindrm("rotator")
