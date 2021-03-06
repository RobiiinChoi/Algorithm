'''

럭키 스트레이트 기술. 기술은 매우 강력한 대신 게임 내에서 점수가 특정 조건을 만족할 때 사용할 수 있다.
특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때, 자리수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의
각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다.
예를 들어서 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3,
오른쪽 부분의 각 자리수의 합은 4+0+2이므로 두 합이 6으로 동일하여 럭키 스트레이트 사용할 수 있다.

점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지 알려주는 프로그램 작성하세요.

첫째 줄에 점수 N이 정수로 주어집니다. 단, 점수 N의 자릿수는 항상 짝수 형태.
예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않습니다.

첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY", 사용할 수 없다면 "READY" 출력

Input : 123402
Output : LUCKY

Input : 7755
Output : READY

'''

n = input()

mid = len(n)//2
L = [int(num) for num in n[:mid]]
R = [int(num) for num in n[mid:]]

if sum(L)==sum(R):
    print("LUCKY")
else:
    print("READY")