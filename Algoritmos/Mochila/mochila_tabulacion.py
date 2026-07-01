def backpack(capacity, weights, values, n):
    array = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                array[i][j] = max(array[i - 1][j], values[i - 1] + array[i - 1][j - weights[i - 1]])
            else:
                array[i][j] = array[i - 1][j]

    return array[n][capacity]

def main():
    weights = [1, 3, 4, 5]
    values = [10, 40, 50, 70]
    capacity = 4
    print(backpack(capacity, weights, values, len(weights)))

main()