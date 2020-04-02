data = []
input_file = open("data.txt")
# Convert input to integers and add each line to data
for line in input_file:
    data.append([int(x) for x in line.split() if x.isdigit()])
# Remove the first number from each line representing the respective number of elements
for line in data:
    line.pop(0)


def merge_sort(arr):
    if len(arr) > 1:
        # Get the middle of the given list, and split into two halves
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]

        # Recursively divide each half until there is only one element on either side
        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        current_arr_index = 0

        # "Merge" the two sides
        while left_index < len(left) and right_index < len(right):
            # If the left value is less than the right value, add the left value to the sorted list
            if left[left_index] <= right[right_index]:
                arr[current_arr_index] = left[left_index]
                left_index += 1

            else:
                arr[current_arr_index] = right[right_index]
                right_index += 1
            current_arr_index += 1
        # Add the remaining elements from the "left" to the sorted list
        while left_index < len(left):
            arr[current_arr_index] = left[left_index]
            current_arr_index += 1
            left_index += 1
        # Add the remaining elements from the "right" to the sorted list
        while right_index < len(right):
            arr[current_arr_index] = right[right_index]
            current_arr_index += 1
            right_index += 1


# Sort each line
for line in data:
    merge_sort(line)

# Write the sorted lists to "merge.out"
with open("merge.out", "w") as output_file:
    for line in data:
        output_file.write("%s\n" % line)
