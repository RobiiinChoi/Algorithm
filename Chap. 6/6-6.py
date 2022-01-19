# # Chapter06_06. 가장 진 팰린드롬 부분 문자열 (159p)
# # 난이도 : ★★
# # Leet code Num. : 5
#
# # 가장 긴 팰린드롬 부분 문자열을 출력하라.
# # 예제 1.
# # 입력 >> "babad"
# # 출력 >> "bab" (또는 "aba")
# # 예제 2.
# # 입력 >> "cbbd"
# # 출력 >> "bb"
#
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]
#
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         result = ''
#         for i in range(len(s) - 1):
#             result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
#         return result
#
#
# if __name__ == "__main__":
#     s = Solution()
#     print(s.longestPalindrome("abbacd"))

##제한사항

## 프로그래머스에 적힌 제한 사항
##문자열 s의 길이 : 2,500 이하의 자연수  - bigO 관련
##문자열 s는 알파벳 소문자로만 구성   - 프로그레밍 조건

## 어떻게 풀까??
##
## 그렇게 하면 bigO는 어떻게 될까?
##
## 더 효율좋개 짤 수 있을까?

## str 값 입력
##str = input()

## 풀이 방법
## 기준점을 기준으로 palin이 홀수개로 이루어질 경우와 짝수개로 이루어질 경우를 나눈다
## 홀 수 일 때는 i와 i+2를 비교
## 짝 수 일 때는 i와 i+1을 비교
## ex) dad 의 펠린은 홀수 길이는 2  list에서 보이는 값은[1, 2, 1]
## ex) abccbac 의 펠린은 짝수, 길이는 2  list에서 보이는 값은[0, 1, 3, 1, 0]

str = "abcdcba" ##입력 예제 1 [1, 1 ,1 ,4 ,1,1,1]
##str = "abacde"  ##입력 예제 2

palins = []  #단어 길이가 홀 수 일 경우 인덱스 값을 기준으로 펠린의 길이를 담는 리스트
palins2 = [] #단어 길이가 짝 수 일 경우 인덱스 값을 기준으로 펠린의 길이를 담는 리스트

## 인덱스 i를 기준으로 펠린 일 경우를 비교
for i in range(len(str)):
    palin_count = 0
    print("시작 인덱스 : ", i, "\t")
    for j in range(len(str)-i):
        if i-j >= 0 and i+j < len(str):
            if str[i-j] == str[i+j]:
                print("left : ", i-j, "right :", i+j, "\t")
                palin_count = palin_count + 1
            else:
                print("펠린 길이", palin_count)
                break
    palins.append(palin_count)
print("palins의 i번째 인덱스에가 기준인 있는 펠린 길이", palins)

## i와 i+1을 비교
for i in range(len(str)-1):
    palin_count = 0
    print("시작 인덱스 : ", i, "\t")
    for j in range(len(str)-1-i):
        if i-j >= 0 and i+j+1 < len(str):
            if str[i-j] == str[i+j+1]:
                print("left : ", i-j, "right :", i+j, "\t")
                palin_count = palin_count + 1
            else:
                print("펠린 길이", palin_count)
                break
    palins2.append(palin_count)
print("palins2의 i번째 인덱스에가 기준인 펠린 길이", palins2)

##출력부
## palins, palins2 두 리스트의 최댓값을 비교 (펠린드롬의 최댓값을 비교) 해
## 큰 값이 들어 있는 리스트에서 펠린드롬 중심을 기준으로 출력
## ex) palins[1, 1, 1, 2, 1, 1] palins2[이면 0, 0, 1, 0, 0]이면 palins[3-2+1, 3+2]
## ex) palins[1, 1, 1, 1, 1, 1] palins2[이면 0, 0, 2, 0, 0]이면 palins2[2-2+1, 3+2+1] 값 출력
if max(palins) < max(palins2):
    middleidx = palins2.index(max(palins2))
    temp = max(palins2)
    print(str[middleidx-temp+1:middleidx+temp+1])

else:
    middleidx = palins.index(max(palins))
    temp = max(palins)
    print(str[middleidx-temp+1:middleidx+temp])
