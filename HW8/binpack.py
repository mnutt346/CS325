def first_fit(weights, cap, n):
    bins_remaining = [cap]

    count = 1

    for i in range(n):
        fit = 0
        for j in range(count):
            # If the current bin has room for the current item, add the item to the current bin
            if bins_remaining[j] >= weights[i]:
                bins_remaining[j] = bins_remaining[j] - weights[i]
                fit = 1
                break
        # If no bins could fit the current item, add a new bin
        if fit == 0:
            bins_remaining.append(cap - weights[i])
            count += 1
    return count


def main():
    input_file = open("bin.txt", "r")
    # Get the number of test cases
    test_cases = int(input_file.readline())

    for i in range(test_cases):
        capacity = 0
        item_count = 0
        item_weights = []
        capacity = int(input_file.readline().strip())
        item_count = int(input_file.readline().strip())
        weight_strings = input_file.readline().split(' ')
        # Create a list of item weights
        for item in range(item_count):
            item_weights.append(int(weight_strings[item].strip()))

        first_fit_bins = first_fit(item_weights, capacity, item_count)
        print("FIRST FIT: ", first_fit_bins)

        # Sort the item weights in descending order for first_fit_decreasing
        item_weights_dec = item_weights.copy()
        item_weights_dec.sort(reverse=True)
        first_fit_dec_bins = first_fit(item_weights_dec, capacity, item_count)
        print("FIRST FIT DEC: ", first_fit_dec_bins)


main()
