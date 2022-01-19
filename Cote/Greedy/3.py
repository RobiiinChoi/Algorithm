# 숫자 카드 게임
# 숫자 카드 게임은 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 게임의 룰을 지키며 카드를 뽑아야 한다
# 1. 숫자가 쓰인 카드들이 N x M 형태, N은 행의 개수, M은 열의 개수
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야한다
# 4. 따라서 처음에 카드를 골라낼 행을 선택 할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
"""
입력 : 3 3    출력 : 2
      3 1 2
      4 1 4
      2 2 2
"""

# 가장 큰 값을 가져와야 하기 때문에 변수로 잡음
max_num = 0
# n, m 값 입력받기
n, m = map(int, input().split())
# n(행)만큼 돌리기
for i in range(n):
    # 한 줄 입력받기
    row = list(map(int, input().split()))
    # 그 줄의 제일 작은 값 찾기
    min_num = min(row)
    # 그 줄의 제일 큰 값 찾기 첫 번째 : 1(0 1) / 1(1 1)/ 2(1 2)
    max_num = max(max_num, min_num)

print(max_num)


