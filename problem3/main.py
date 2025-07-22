# 🧮 Coin Change Problem — Minimum Number of Coins (Bottom-Up DP)
# Based on algorithm from GeeksforGeeks :contentReference[oaicite:1]{index=1}

def min_coins_with_breakdown(coins, target):
    """
    Returns the minimum number of coins needed and the breakdown of coins used.
    Returns (min_coins, coin_breakdown) where coin_breakdown is a dict.
    Returns (-1, {}) if it's impossible.
    """
    # Initialize DP table: dp[i] = min coins to reach sum i
    INF = float('inf')
    dp = [INF] * (target + 1)
    dp[0] = 0  # base case: 0 coins needed to make sum 0
    
    # Track which coin was used to achieve minimum for each amount
    parent = [-1] * (target + 1)

    # Bottom-up build: for each coin, update dp
    for coin in coins:
        for amount in range(coin, target + 1):
            # If we can form (amount - coin), try to use this coin
            if dp[amount - coin] != INF:
                if dp[amount - coin] + 1 < dp[amount]:
                    dp[amount] = dp[amount - coin] + 1
                    parent[amount] = coin

    # If dp[target] remains INF, it's not possible to form
    if dp[target] == INF:
        return -1, {}
    
    # Reconstruct the solution
    coin_count = {}
    for coin in coins:
        coin_count[coin] = 0
    
    current = target
    while current > 0:
        coin_used = parent[current]
        coin_count[coin_used] += 1
        current -= coin_used
    
    return dp[target], coin_count

def min_coins(coins, target):
    """
    Returns the minimum number of coins needed to make 'target' sum using
    denominations in 'coins'. Returns -1 if it's impossible.
    """
    result, _ = min_coins_with_breakdown(coins, target)
    return result


def main():
    # Predefined coin denominations (in cents for internal calculation)
    # 1¢, 5¢, 10¢, 20¢, 50¢, $1, $5, $10, $20, $50, $100
    coins = [1, 5, 10, 20, 50, 100, 500, 1000, 2000, 5000, 10000]
    
    # Coin labels for display
    coin_labels = {
        1: "1¢",
        5: "5¢", 
        10: "10¢",
        20: "20¢",
        50: "50¢",
        100: "$1",
        500: "$5",
        1000: "$10",
        2000: "$20",
        5000: "$50",
        10000: "$100"
    }
    
    print("Available coin denominations:")
    print("1¢, 5¢, 10¢, 20¢, 50¢, $1, $5, $10, $20, $50, $100")
    
    # Input: target amount in dollars
    try:
        target_dollars = float(input("Enter target amount in dollars (e.g., 5.75): $"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if target_dollars < 0:
        print("Target amount must be non-negative.")
        return
    
    # Convert dollars to cents for internal calculation
    target = int(round(target_dollars * 100))

    result, coin_breakdown = min_coins_with_breakdown(coins, target)
    if result == -1:
        print(f"It is not possible to make ${target_dollars:.2f} with the available coin denominations.")
    else:
        print(f"\nTo make ${target_dollars:.2f}, you need {result} coins:")
        print("Coin breakdown:")
        for coin in coins:
            count = coin_breakdown.get(coin, 0)
            print(f"{coin_labels[coin]}:{count}")
        
        # Calculate total value as verification
        total_value = sum(coin * count for coin, count in coin_breakdown.items())
        print(f"\nVerification: Total value = ${total_value/100:.2f}")


if __name__ == "__main__":
    main()
