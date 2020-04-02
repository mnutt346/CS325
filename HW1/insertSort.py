data = []
input_file = open("data.txt")
# Convert input to integers and add each line to data
for line in input_file:
    data.append([int(x) for x in line.split() if x.isnumeric()])
# Remove the first number from each line representing the respective number of elements
for line in data:
    line.pop(0)


def insert_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


for line in data:
    insert_sort(line)

with open("insert.out", "w") as output_file:
    for line in data:
        output_file.write("%s\n" % line)