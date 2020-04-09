import math
import numpy

list_data = []

input_file = open("data.txt")
# Convert input to integers and add each line to data
for line in input_file:
    list_data.append([int(x) for x in line.split() if x.isdigit()])
# Remove the first number from each line representing the respective number of elements
for line in list_data:
    line.pop(0)


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
    print("Please enter an alpha fraction < 1: ")
    num, den = input().split('/')
    alpha = float(num) / float(den)
    for element in list_data:
        length = len(element)
        bad_sort(element, 0, length - 1, alpha)

    with open("bad.out", "w") as output_file:
        for line in list_data:
            output_file.write("%s\n" % line)


main()
