heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
heights_copy = heights[:]
sum = 0 # 빗물 저장값 담을 변수
maxval = max(heights) # 높이 최대값 저장
count = 0
i = 0
while i < len(heights):
    heights_copy.pop(0) # 비교값 요소 제거
    if heights[i] > max(heights_copy):
        continue
    else:
        for j in range(len(heights_copy)):
            if heights[i] <= heights_copy[j]:
                i += count
                count = 0
                i += 1
                break
            else :
                sum += heights[i] - heights_copy[j]
                print(heights[i], heights_copy[j], heights[i] - heights_copy[j])
                print(sum)
            count += 1


print(sum)