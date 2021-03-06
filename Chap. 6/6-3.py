# Chapter06_03. 로그파일 재정렬 (148p)
# 난이도 : ★
# Leet code Num. : 937

# 로그를 재정렬하라, 기준은 다음과 같다.
# (1) 로그의 가장 앞 부분은 식별자다.
# (2) 문자로 구성된 로그가 숫자로그보다 앞에 온다.
# (3) 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# (4) 숫자로그는 입력 순서대로 한다.

# 예제 1.
# 입력 >> logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# 출력 >>  [ "let1 art can",  "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6",]
import collections
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit

if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    s = Solution()
    print(s.reorderLogFiles(logs))

    from typing import List


    # def reorderLogFiles(logs: List[str]):
    #     letters, digits = [], []
    #     for log in logs:
    #         if log.split()[1].isdigit():
    #             digits.append(log)
    #         else:
    #             letters.append(log)
    #
    #     letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    #     return letters + digits
    #
    #
    # logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    #
    # print(reorderLogFiles(logs))