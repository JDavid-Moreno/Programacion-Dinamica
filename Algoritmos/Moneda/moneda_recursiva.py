def coin_change(amount, coins):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    minimum = float('inf')
    for coin in coins:
        minimum = min(minimum, coin_change(amount - coin, coins) + 1)

    return minimum

def main():
    coins = [1,2,5]
    amount = 11
    number_coins = coin_change(amount, coins)
    print(number_coins)
main()