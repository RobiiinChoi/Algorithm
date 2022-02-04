'''

슈퍼 게임 오렐리는 큰 고민에 빠졌습니다.
그녀가 만든 프렌즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자 수가 급감했습니다.
원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였습니다.

이 문제를 어떻게 할까 고민한 그녀는 동적으로 게임 시간을 늘려서, 난이도를 조절하기로 했습니다.
역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았습니다.
오렐라를 위해 실패율을 구하는 코드를 완성하세요.

실패율은 다음과 같이 정의합니다.
- 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수/ 스테이지에 도달한 플레이어의 수

전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하세요.

'''

def solution(N, stages):
    answer = {}
    bunmo=len(stages)
    for stage in range(1, N+1):
        if bunmo != 0:
            count = stages.count(stage)
            answer[stage] = count/bunmo
            bunmo -= count
        else:
            answer[stage] = 0
    return sorted(answer, key=lambda x: answer[x], reverse = True)