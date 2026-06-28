def coin_change(coins, amount):
    if amount < 0:
        return float('inf')
    array = [float('inf')] * (amount + 1)
    array[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                array[i] = min(array[i], array[i - coin] + 1)

    return array[amount]

def main():
    coins = [1,2,5]
    amount = 11
    number_coins = coin_change(coins, amount)
    print(number_coins)
main()