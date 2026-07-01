def backpack(capacity, weights, values, n):
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return backpack(capacity, weights, values, n - 1)

    return max(backpack(capacity, weights, values, n - 1),
               values[n - 1] + backpack(capacity - weights[n - 1], weights, values, n - 1))

def main():
    weights = [1,3,4,5]
    values = [10,40,50,70]
    capacity = 4

    result = backpack(capacity, weights, values, len(weights))
    print(result)
main()