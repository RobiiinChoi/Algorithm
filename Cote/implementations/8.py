'''
알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어짐.
모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력.
Input
K1KA5CB7

Output
ABCKK13
'''
n = sorted(input())
print(n)
for i in range(len(n)):
    if n[i].isalpha():
        break
print("".join(n[i:])+str(sum(map(int, n[:i]))))
