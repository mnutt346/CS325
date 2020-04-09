import math
import random
import timeit
from fractions import Fraction


# Creates list of n random integers
def random_list(n):
    return [random.randint(0, 10000) for i in range(n)]


data_100 = random_list(20)
data_200 = random_list(40)
data_300 = random_list(60)
data_400 = random_list(80)
data_500 = random_list(100)
data_600 = random_list(120)
data_700 = random_list(140)


def bad_sort(arr, left, right, alpha):
    n = right - left + 1
    if n == 2 and arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    elif n > 2:
        m = math.ceil(alpha * n)
        if m == n:
            m -= 1
        bad_sort(arr, left, left + m - 1, alpha)
        bad_sort(arr, right - m + 1, right, alpha)
        bad_sort(arr, left, left + m - 1, alpha)


def main():
    # Get alpha value from user
    print("Please enter an alpha fraction < 1: ")
    # Python 2.7
    alpha = float(Fraction(raw_input()))
    # Python 3
    # alpha = float(Fraction(input()))

    start_time_1000 = timeit.default_timer()
    bad_sort(data_100, 0, 19, alpha)
    elapsed_time_1000 = timeit.default_timer() - start_time_1000
    print("Elapsed time (100): ", elapsed_time_1000)

    start_time_2000 = timeit.default_timer()
    bad_sort(data_200, 0, 39, alpha)
    elapsed_time_2000 = timeit.default_timer() - start_time_2000
    print("Elapsed time (200): ", elapsed_time_2000)

    start_time_3000 = timeit.default_timer()
    bad_sort(data_300, 0, 59, alpha)
    elapsed_time_3000 = timeit.default_timer() - start_time_3000
    print("Elapsed time (300): ", elapsed_time_3000)

    start_time_4000 = timeit.default_timer()
    bad_sort(data_400, 0, 79, alpha)
    elapsed_time_4000 = timeit.default_timer() - start_time_4000
    print("Elapsed time (400): ", elapsed_time_4000)

    start_time_5000 = timeit.default_timer()
    bad_sort(data_500, 0, 99, alpha)
    elapsed_time_5000 = timeit.default_timer() - start_time_5000
    print("Elapsed time (500): ", elapsed_time_5000)

    start_time_6000 = timeit.default_timer()
    bad_sort(data_600, 0, 119, alpha)
    elapsed_time_6000 = timeit.default_timer() - start_time_6000
    print("Elapsed time (600): ", elapsed_time_6000)

    start_time_7000 = timeit.default_timer()
    bad_sort(data_700, 0, 139, alpha)
    elapsed_time_7000 = timeit.default_timer() - start_time_7000
    print("Elapsed time (700): ", elapsed_time_7000)


main()
