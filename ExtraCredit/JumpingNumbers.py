def jumping_numbers(N):
    q = []
    i = 1
    results = []
    for i in range(10):
        q.append(i)
        while len(q) != 0:
            temp = q.pop(0)
            if temp > N:
                continue
            results.append(temp)
            front = temp % 10
            if front > 0:
                q.append(temp * 10 + (front - 1))
            if front < 9:
                q.append(temp * 10 + (front + 1))
    return results


def main():
    print("Please enter an integer from 50 to 300.")
    num = int(input())
    jumping_numbers(num)
    jumped = jumping_numbers(num)
    # Sort results
    jumped.sort()
    # Remove duplicates
    jumped = list(dict.fromkeys(jumped))
    for number in jumped:
        print(number)


main()
