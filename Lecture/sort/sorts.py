def bubblesort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) - 1 만큼 반복한다.
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst

def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur

        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]

    return lst

def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst


def insertionsort_2(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        cmp = idx - 1

        while lst[cmp] > val and cmp >= 0:
            lst[cmp + 1] = lst[cmp]
            cmp -= 1

        lst[cmp + 1] = val

    return lst

# 퀵소트 구현 (정렬할 리스트, 시작, 끝을 매개변수로 받는다)
def quicksort(lst, start, end):
    # 퀵소트 부분집합 만들기(pivot 기준)
    def partition(part, ps, pe):
        # 리스트의 마지막 인덱스를 피벗으로 삼는다
        # 피벗보다 작은 부분집합을 구할 변수를 i로 삼고 -1로 초기화 한다
        pivot = part[pe]
        i = ps - 1
        # 피벗과 비교할 인덱스를 j로 받고 피벗보다 j 숫자가 작으면 i값을 1 올리고(피벗보다 작은 집합 개수카운트), 스왑
        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        # 최종적으로 피벗과 부분집합 인덱스 i의 다음칸으로 피벗을 스왑한다
        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1

    # 시작과 끝이 같거나 시작이 더 클경우(인덱스가 1개 이하)
        if start >= end:
            return None

    # 
    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end)
    return lst