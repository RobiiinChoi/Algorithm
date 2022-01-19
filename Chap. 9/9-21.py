from collections import Counter

def del_dup(s):
    stack = []
    # 1) 알파벳 갯수를 카운트 한다.
    cnter = Counter(s)

# bcabc
# bcbac
    i=0
    for char in s:  ##  cbacdbcb
        cnter[char] -= 1
        if cnter[char] == 0:
            # 위치를 변환할수 있는지 체크한다. 단 한개뿐이라면 재배치 불가능
            stack.append(char)
            print(stack)
        # 2) 다음 문자와 비교하여 크기가 작다면 append , 크다면 pop
        elif s[i] < s[i+1]:
            stack.append(char)
        else:
            stack.pop(i)


    print(stack)

if __name__ == "__main__":
    del_dup('cbacdcbc')