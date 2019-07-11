import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

mysetup = """import numpy as np
from pychallenge.sort.merge import merge_sort
from pychallenge.sort.bubble import bubble_sort
shortlist = np.random.random(10)
longlist = np.random.random(1000)
"""
n = 10


def main():
    print("SPEED COMPARISON OF SHORT LIST")
    t = timeit.timeit(setup=mysetup, stmt='bubble_sort(shortlist)', number=n) / n
    print(f"Bubble sort: {t}")
    t = timeit.timeit(setup=mysetup, stmt='merge_sort(shortlist)', number=n) / n
    print(f"Merge sort: {t}")

    print("SPEED COMPARISON OF LONG-ISH LIST")
    t = timeit.timeit(setup=mysetup, stmt='bubble_sort(longlist)', number=n) / n
    print(f"Bubble sort: {t}")
    t = timeit.timeit(setup=mysetup, stmt='merge_sort(longlist)', number=n) / n
    print(f"Merge sort: {t}")


if __name__ == "__main__":
    main()
