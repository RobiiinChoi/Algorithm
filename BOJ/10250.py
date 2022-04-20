T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())
    height = n % h
    room = n // h + 1
    if height == 0:
        room = n // h
        height = h
    print(height*100 + room)