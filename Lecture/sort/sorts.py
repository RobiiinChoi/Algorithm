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

# 머지소트의 머지부분 구현
def merge(arr1, arr2):
    # 구현할 어레이 외에 하나 더 빈 리스트를 만든다(머지할 리스트 변수)
    result = []
    # i, j로 각 배열의 포인터 변수를 만들고 0으로 설정
    i = j = 0
    # i의 포인터가 전체보다 작고 j의 포인터가 전체보다 작을 때 (아직 머지할 원소들이 남았을 때)
    while i < len(arr1) and j < len(arr2):
        # 각 배열에서 더 작은 값을 병합하는 과정
        # arr1이 arr2보다 작을 때 result에 arr1을 붙이고 포인터를 1 올린다
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        # 반대의 경우 arr2를 result에 붙이고 포인터를 1 올린다
        else:
            result.append(arr2[j])
            j +=1

    # i의 값이 arr1 길이보다 작을 때 (위의 병합정렬에서 이 케이스는 arr2가 먼저 다 result안에 들어간 경우)
    while i < len(arr1):
        # 마찬가지로 arr1의 원소를 result로 어펜드하고 포인터를 1 올린다
        result.append(arr1[i])
        i+=1

    # j의 값이 arr2 길이보다 작을 때( arr1이 다 들어감)
    while j < len(arr2):
        # arr2의 원소를 어펜드하고 포인터 1올린다
        result.append(arr2[j])
        j+=1

    return result

# 머지 소트 (머지 전 나누는 부분 구현)
def mergesort(lst):
    # 리스트 길이가 1일 때는 그냥 리스트 리턴 (정렬할 게 없다)
    if len(lst)<=1:
        return lst

    # 리스트를 반으로 나눈 인덱스를 mid라는 포인트로 지정하고 미드를 기준으로 오른쪽 왼쪽 부분을 나눈다 (정렬 나누는 과정)
    mid = len(lst)//2
    L = lst[:mid]
    R = lst[mid:]

    return merge(mergesort(L), mergesort(R))