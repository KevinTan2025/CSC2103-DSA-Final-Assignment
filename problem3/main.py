# 🧮 Coin Change Problem — Minimum Number of Coins (Bottom-Up DP)
# Based on algorithm from GeeksforGeeks
#
# PROBLEM: Given a set of coin denominations and a target amount, find the minimum
# number of coins needed to make that amount, and show the exact breakdown.
#
# ALGORITHM: Dynamic Programming (Bottom-Up Tabulation)
# - Time Complexity: O(target × number_of_coins)
# - Space Complexity: O(target)
# - Uses parent tracking to reconstruct the optimal coin combination
#
# APPROACH:
# 1. Build a DP table where dp[i] = minimum coins needed for amount i
# 2. Track parent array to remember which coin was used for each amount
# 3. Reconstruct solution by backtracking through parent array
# 4. Display exact breakdown showing count of each coin denomination

def min_coins_with_breakdown(coins, target):
    """
    Returns the minimum number of coins needed and the breakdown of coins used.
    Uses Dynamic Programming (bottom-up tabulation) with parent tracking.
    
    Args:
        coins: List of coin denominations (in cents)
        target: Target amount to make (in cents)
    
    Returns:
        (min_coins, coin_breakdown) where:
        - min_coins: minimum number of coins needed (-1 if impossible)
        - coin_breakdown: dictionary showing count of each coin used
    """
    # Initialize DP table: dp[i] = minimum coins needed to make amount i
    INF = float('inf')  # Use infinity to represent impossible amounts
    dp = [INF] * (target + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
    # Parent array to track which coin was used to achieve minimum for each amount
    # This allows us to reconstruct the actual coin combination later
    parent = [-1] * (target + 1)

    # Bottom-up DP: Fill the table by considering each coin denomination
    for coin in coins:
        # For each amount from coin value to target
        for amount in range(coin, target + 1):
            # Check if we can form (amount - coin) with previous solutions
            if dp[amount - coin] != INF:
                # If using this coin gives a better solution, update dp table
                if dp[amount - coin] + 1 < dp[amount]:
                    dp[amount] = dp[amount - coin] + 1
                    parent[amount] = coin  # Remember which coin we used

    # Check if target amount is achievable
    if dp[target] == INF:
        return -1, {}  # Impossible to make the target amount
    
    # Reconstruct the solution by backtracking through parent array
    coin_count = {}
    # Initialize count for all coin denominations to 0
    for coin in coins:
        coin_count[coin] = 0
    
    # Backtrack from target to 0 to find which coins were used
    current = target
    while current > 0:
        coin_used = parent[current]  # Get the coin that was used for this amount
        coin_count[coin_used] += 1   # Increment count for this coin
        current -= coin_used         # Move to the remaining amount
    
    return dp[target], coin_count

def min_coins(coins, target):
    """
    Wrapper function that returns only the minimum number of coins needed.
    Uses the main DP function but discards the breakdown information.
    
    Args:
        coins: List of coin denominations
        target: Target amount to make
    
    Returns:
        Minimum number of coins needed (-1 if impossible)
    """
    result, _ = min_coins_with_breakdown(coins, target)
    return result

def run_tests():
    print("Running test cases...")
    # Test cases to validate the implementation
    test_cases = [
        ([1,2,5],11,3),  # 11 = 5 + 5 + 1
        ([2],3,-1),  # Impossible to make 3 with only 2s
        ([1,3,4],6,2), # 6 = 3 + 3 or 4 + 1 + 1
        ([5,10],0,0), # 0 amount requires 0 coins
        ([7],14,2) # 14 = 7 + 7 
    ]

    for i, (coins, target, expected) in enumerate(test_cases):
        result = min_coins(coins, target)
        status = "PASSED" if result == expected else f"FAILED(Got {result})"
        print(f"Test {i+1}: coins={coins}, target= {target} -> expected= {expected} -> {status}")
    print("Testing completed.\n")

def display_breakdown(coin_breakdown, coin_labels):
    for coin in sorted(coin_breakdown.keys()):
        label = coin_labels.get(coin, f"{coin}¢" if coin < 100 else f"${coin // 100}")
        print(f"{label}: {coin_breakdown[coin]}")

def main():
    # Predefined coin denominations (stored in cents for precise calculation)
    # Covers common currency: 1¢, 5¢, 10¢, 20¢, 50¢, $1, $5, $10, $20, $50, $100
    default_coins = [1, 5, 10, 20, 50, 100, 500, 1000, 2000, 5000, 10000]

    # Human-readable labels for displaying coin denominations
    coin_labels = {
        1: "1¢",      # 1 cent
        5: "5¢",      # 5 cents 
        10: "10¢",    # 10 cents 
        20: "20¢",    # 20 cents
        50: "50¢",    # 50 cents 
        100: "$1",    # 1 dollar
        500: "$5",    # 5 dollars
        1000: "$10",  # 10 dollars
        2000: "$20",  # 20 dollars
        5000: "$50",  # 50 dollars
        10000: "$100" # 100 dollars
    }

    run_tests()

    print("=== Coin Change Calculator ===")
    while True:
        # Choose coins
        choice = input("Use default coin denominations? (y/n): ").lower()
        if choice == 'y':
            print("Available coin denominations:")
            print("1¢, 5¢, 10¢, 20¢, 50¢, $1, $5, $10, $20, $50, $100")
            coins = default_coins
        else:
            try:
                coins = list(map(int, input("Enter custom coin values (space-separated, in cents): ").split()))
                if not coins or any(c <= 0 for c in coins):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter positive integers.")
                continue

        try:
            dollars = float(input("Enter target amount in dollars (e.g., 5.75): $"))
            if dollars < 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")
            continue

        target = int(round(dollars * 100))
        result, breakdown = min_coins_with_breakdown(coins, target)

        if result == -1:
            print(f"\nCannot make ${dollars:.2f} with the given denominations.\n")
        else:
            print(f"\nTo make ${dollars:.2f}, you need {result} coin(s).")
            print("Coin breakdown:")
            display_breakdown(breakdown, coin_labels)
            total_value = sum(coin * count for coin, count in breakdown.items())
            print(f"\nVerification: Total value = ${total_value / 100:.2f}\n")

        again = input("Run another calculation? (y/n): ").lower()
        if again != 'y':
            print("👋 Exiting program. Goodbye!")
            break


# Entry point of the program
if __name__ == "__main__":
    main()
