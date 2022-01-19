
#pip 8을 따르기 떄문에 이게 없으면 오류가 뜸 (자바 메인 클래스 느낌)
if __name__ == "__main__" :
    #데이터 타입이 없기 때문에 타입 힌트를 줌으로써 어떤 타입인지 알려줌. 이렇게 지정하면 다른 타입이 들어올 수 없음 (이미 str로 박아놨기 떄문에)
    s: str = "hello"
    print(s[1]) # indexing
    print(s[1:]) # slicing (***) (substring())
    print(s[-1]) #indexing reverse order
    print(s[1:len(s)]) # slicing #[start : end] (end 미포함)
    # start <=     < end
    # start : 0 (default) end : len(s) (default)

    # in 연산자 (문자열 안에 문자열 포함되는지?)
    print("s" in "str")

    #idx = s.index('t') # return index

    # list, str
    # join : list -> str
    # '1' + '2' + '3' + '4'
    # split : str -> list
    li = [1,2,3,4]
    s1 = s.join(li)
    print(s1)

    #immutable (수정 불가)
    s1[0] = '10' # 조인을 하면 인덱싱으로 추가가 불가

