import random
import timeit


# Creates list of n random integers
def random_list(n):
    return [random.randint(0, 10000) for i in range(n)]


data = random_list(5000)


def insert_sort(arr):
    # For each element in the given list, while the current element is less than the target element,
    # insert the target element at the next position and continue shifting the target to the left
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


start_time = timeit.default_timer()
insert_sort(data)
elapsed_time = timeit.default_timer() - start_time
print("Elapsed time: ", elapsed_time)
