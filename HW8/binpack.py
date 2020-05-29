import copy


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


def best_fit(weights, cap, n):
    count = 0
    bins_remaining = [0]*n

    for i in range(n):
        j = 0
        # Initialize the minimum space remaining to one greater than the current capacity
        min_space = cap + 1
        # Used for tracking the index of the "best" bin
        best_bin_index = 0

        # Check if the current item will fit in the current bin AND if the current bin is the best fit
        for j in range(count):
            if bins_remaining[j] >= weights[i] and bins_remaining[j] - weights[i] < min_space:
                best_bin_index = j
                min_space = bins_remaining[j] - weights[i]
        # If the current item could not fit in any available bin, add a new bin
        if min_space == cap + 1:
            bins_remaining[count] = cap - weights[i]
            count += 1
        # Otherwise, add the item to the "best" bin
        else:
            bins_remaining[best_bin_index] -= weights[i]

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

        # Sort the item weights in descending order for first_fit_decreasing
        item_weights_dec = copy.copy(item_weights)
        item_weights_dec.sort(reverse=True)
        first_fit_dec_bins = first_fit(item_weights_dec, capacity, item_count)

        best_fit_bins = best_fit(item_weights, capacity, item_count)
        print("Test Case ", i + 1, " FIRST FIT: ", first_fit_bins, "FIRST FIT DEC: ", first_fit_dec_bins, "BEST FIT: ", best_fit_bins)


main()
