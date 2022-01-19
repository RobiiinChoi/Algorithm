# 1 ~ N 까지의 수를 스택에 넣었다가 뽑아 늘어놓아서 하나의 수열을 만든다.
# push하는 순서는 오름차순 (매우 중요!!!!!!!)
# 임의의 수열이 주어졌을 때 수열을 만들 수 있는지, 있다면 어떤 순서로 연산을 수행해야하는지

# 8 = 총 개수
# 4 3 6 8 7 5 2 1

# + + + + / - - / + + / - / + + / - - - - - /
# 1 2 3 4 + + + +
# 1 2 - - (4 pop, 3 pop)
# 1 2 5 6 + +(5, 6 push)
# 1 2 5 - (6 pop)
# 1 2 5 7 8 + +(7, 8 push)
# None (8, 7, 5, 2, 1 pop)

# #sudo
# 스택과 정답을 담을 리스트, 그리고 오름차순 숫자 변수를 초기화한다.
# 배열의 총 개수만큼 for문이 돌아가며, 수열의 숫자를 한줄 씩 num 변수에 받는다
# 오름차순의 숫자가 num 변수의 숫자보다 작을 경우 스택에 해당 숫자를 쌓고, 정답 리스트에는 push 표시인 (+)를 answer에 추가하고 오름차순 숫자를 1 추가한다
# 스택 맨위 숫자와 num 변수가 같을 경우 pop 표시인 (-)를 answer에 추가하고 해당 스택을 pop한다.
# 만약 예외케이스 (스택 맨위 숫자가 num 변수보다 클 경우)가 발생하면 “NO”를 출력한다
# 수열이 완성되어 스택이 비어지면, for문으로 answer를 출력해낸다.
# sys.stdin.readline()
import sys

# 오름차순을 가리키는 숫자(비교)
cur = 1
# 스택 초기화
stack = []
# 정답을 기입할 리스트 ('+', '-')
answer = []
a = int(input())
for i in range(a):
    num = int(sys.stdin.readline())  # 4 3 6 8 7 5 2 1
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
    if stack[-1] == num:
        answer.append('-')
        stack.pop()
    # 예외 처리 stack[-1] > num # 1 2 5 3 4
    else:
        print("NO")
        break


# stack이 비워져있으면 false -> not stack 이므로 true
if not stack:
    for i in answer:
        print(i)

