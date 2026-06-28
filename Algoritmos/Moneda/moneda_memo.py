def coin_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    minimum = float('inf')
    for coin in coins:
        minimum = min(minimum, coin_change(amount - coin, coins, memo) + 1)
    memo[amount] = minimum
    return minimum

def main():
    coins = [1,2,5]
    amount = 40
    memo = {}
    number_coins = coin_change(amount, coins, memo)
    print(number_coins)
main()