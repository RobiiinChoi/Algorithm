# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Input digits = "23"
# Output : ["ad", "ae", "af", "bd","be","bf","cd","ce","cf"]

class Solution:
    def letterCombinations(self, digits: str):
        def dfs(index, path):
            if len(path) == len(digits): #끝까지 탐색(2자리로 path가 맞춰질 때) 하면
                result.append(path) #path를 최종 리스트인 result에 붙인다
                return

            for i in range(index, len(digits)): #digit의 길이 만큼 돌린다. 왜? digit[0]번에 해당하는 알파벳 1개와 digit[1]번에 해당하는 알파벳 한개 붙여서 조합하니까
                for j in dic[digits[i]]: # digit[0]이면 입력된 수가 56이라면 dic[5]에 해당하는 키값의 0번째 인덱스부터 가지고 온다.
                    dfs(i+1, path+j) #다시 i값을 1로 만들고 path에 digit[0]의 알파벳 1개를 붙여서 재귀함수 진행
        if not digits:
            return []

        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result =[]
        dfs(0,"")
        print(result)
        return result

if __name__ == "__main__":
    s = Solution()
    s.letterCombinations("56")