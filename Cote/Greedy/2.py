
def bigNum():
    n, m, k = map(int, input().split())
    seq = list(map(int, input().split()))
    seq.sort(reverse=True)
    first = seq[0]
    second = seq[1]

    count = int(m/(k+1))*k
    count += m%(k+1)

    result = 0
    result += (count)*first
    result += (m-count)*second

    print(result)

if __name__ == "__main__":
    bigNum()
