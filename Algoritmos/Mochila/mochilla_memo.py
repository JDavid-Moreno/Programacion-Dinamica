def backpack(capacity, weights, values, n, memo):
    if (capacity, n) in memo:
        return memo[(capacity, n)]

    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        result = backpack(capacity, weights, values, n - 1, memo)
    else:
        result = max(backpack(capacity, weights, values, n - 1, memo),
                         values[n - 1] + backpack(capacity - weights[n - 1], weights, values, n - 1, memo))

    memo[(capacity, n)] = result
    return result

def main():
    weights = [1,3,4,5]
    values = [10,40,50,70]
    capacity = 4
    memo = {}

    result = backpack(capacity, weights, values, len(weights), memo)
    print(result)

main()