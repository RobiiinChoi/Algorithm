from Lecture.heap.structures import BinaryMaxHeap
from Lecture.sort.sorts import bubblesort
from Lecture.sort.sorts import selectionsort
from Lecture.sort.sorts import insertionsort
from Lecture.sort.sorts import insertionsort_2
from Lecture.sort.sorts import quicksort
from Lecture.sort.sorts import mergesort

assert bubblesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert bubblesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert selectionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert selectionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert insertionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert insertionsort_2([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort_2([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert quicksort([4, 6, 2, 9, 1], 0, 1) == [4, 6, 2, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 2) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 3) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 4) == [1, 2, 4, 6, 9]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 1) == [2, 3, 1, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 2) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 3) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 4) == [1, 2, 3, 3, 5, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 5) == [1, 2, 2, 3, 3, 5, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 6) == [1, 2, 2, 3, 3, 3, 5]

assert mergesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert mergesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

def sorted_by_heap(lst):
    maxheap = BinaryMaxHeap()
    for elem in lst:
        maxheap.insert(elem)

    desc = [maxheap.extract() for _ in range(len(lst))]
    return list(reversed(desc))