'''
 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다.
 이 수를 큰 수부터 작은수의 순서로 정렬해야 한다.

'''
print(' '.join(sorted([input() for _ in range(int(input()))], reverse=True, key = int)))

