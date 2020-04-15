def knapsack(W, P, N, M, table):
    K = [[0 for x in range(M + 1)] for x in range(N + 1)]

    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif W[i - 1] <= j:
                K[i][j] = max(P[i - 1] + K[i - 1][j - W[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    result = K[N][M]
    weight = M

    # Add items gathered by family members to the table
    for q in range(N, 0, -1):
        if result <= 0:
            break
        elif result > 0 and result == K[q - 1][weight]:
            continue
        else:
            table.append(q)
            result -= P[q - 1]
            weight -= W[q - 1]

    return K[N][M]


def main():
    input_file = open("shopping.txt")
    test_cases = 0
    items = 0
    family_members = 0
    max_weight = 0
    with open("results.txt", "w") as output_file:
        output_file.write("")
    output_file.close()

    # Get the number of test cases from the input file
    test_cases = int(input_file.readline())

    # Gather data from each test case
    for test in range(test_cases):
        prices = []
        weights = []

        with open("results.txt", "a+") as output_file:
            output_file.write("Test Case " + str(test + 1) + "\n")
        output_file.close()
        items = int(input_file.readline())

        # For each item, collect the corresponding prices and weights
        for item in range(items):
            item_attributes = input_file.readline().split(' ')
            prices.append(int(item_attributes[0]))
            weights.append(int(item_attributes[1]))

        # Initialize the current maximum calculated price to 0
        curr_max_price = 0

        # Get the total number of family members
        family_members = int(input_file.readline())

        data_table = [[] for i in range(family_members)]

        # Get the maximum value that can be carried by each family member
        for member in range(family_members):
            max_weight = int(input_file.readline())
            curr_max_price += knapsack(weights, prices, items, max_weight, data_table[member])

        for element in data_table:
            element.sort()

        with open("results.txt", "a+") as output_file:
            output_file.write("Total Price " + str(curr_max_price) + "\n")
            output_file.write("Member Items\n")
            for member in range(family_members):
                output_file.write(str(member + 1) + ": "),
                for item in data_table[member]:
                    output_file.write(str(item) + " ")
                output_file.write("\n")



main()
