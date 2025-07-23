'''
CSC2103 Data Structures and Algorithms
Problem 3: Dynamic Programming (Bottom-Up Tabulation)
Author: Ng Ji Yeung, Wong Yu Xuan, Wong Wen Ru
UX Refinement: Tan Kok Feng

This program implements a comprehensive Coin Change Problem solution using Dynamic Programming.
It finds the minimum number of coins needed to make a target amount and provides a breakdown of the coins used.
No built-in libraries are used for core operations.

Inspired by GeeksforGeeks algorithm, this implementation includes:
- Dynamic Programming (Bottom-Up Tabulation) approach
- Parent tracking for reconstructing the coin combination
- Built-in test cases for validation
'''


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
    print("Running test cases...\n")
    # Predefined test cases to validate the correctness of the algorithm
    # Each test case is a tuple: (coins, target, expected_result, description, explanation)
    test_cases = [
        ([1,2,5], 11, 3, "Standard case", "11¢ = 5¢ + 5¢ + 1¢ (3 coins)"),
        ([2], 3, -1, "Impossible case", "Cannot make 3¢ with only 2¢ coins"),
        ([1,3,4], 6, 2, "Multiple solutions", "6¢ = 3¢ + 3¢ (2 coins) is better than 1¢+1¢+1¢+1¢+1¢+1¢ (6 coins)"),
        ([5,10], 0, 0, "Zero amount", "0¢ requires 0 coins"),
        ([7], 14, 2, "Single denomination", "14¢ = 7¢ + 7¢ (2 coins)")
    ]

    # Run each test case and compare the output to expected value
    for i, (coins, target, expected, description, explanation) in enumerate(test_cases):
        print(f"Test {i+1}: {description}")
        print(f"  Coins available: {coins}")
        print(f"  Target amount: {target}¢")
        print(f"  Expected result: {expected} coins")
        print(f"  Logic: {explanation}")
        
        result = min_coins(coins, target)
        status = "✅ PASSED" if result == expected else f"❌ FAILED (Got {result})"
        print(f"  Result: {status}\n")
    
    print("Testing completed.\n")

def display_breakdown(coin_breakdown, coin_labels):
    """
    Displays the breakdown of coins used to make the target amount.
    Formates coin denominations with appropriate labels (e.g. $1, 50¢).
    """
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

    while True:
        print("\n" + "="*70)
        print(" COIN CHANGE SOLVER - Dynamic Programming (Bottom-Up Tabulation)")
        print("="*70)
        print("💡 This program calculates the minimum number of coins needed\n"
              "   to make a target amount using dynamic programming.\n")
        print("MENU:")
        print("1. Run Coin Change Calculator")
        print("2. Run Built-in Test Cases")
        print("0. Exit")
        print("="*70)
        choice = input("Enter your choice (0-2): ")

        if choice == '0':
            print("\n👋 Thank you for using the Coin Change Solver!\n")
            break

        elif choice == '2':
            print("\n\n" + "="*40)
            print("🧪 RUNNING TEST CASES")
            print("="*40)
            run_tests()
            input("Press Enter to return to main menu...")

        elif choice == '1':
            print("\n\n" + "="*60)
            print("💰 COIN DENOMINATION SETUP")
            print("="*60)
            use_default = input("Use default coin denominations? (Y/n): ").strip().lower()

            if use_default == 'y':
                coins = default_coins
                print("✅ Using default coins:")
                print("1¢, 5¢, 10¢, 20¢, 50¢, $1, $5, $10, $20, $50, $100")
            else:
                try:
                    print("💡 Examples: 1 5 10 25 (for 1¢, 5¢, 10¢, 25¢)")
                    print("           : 1 10 50 100 500 (for 1¢, 10¢, 50¢, $1, $5)")
                    coins = list(map(int, input("Enter custom coin values (in cents, space-separated): ").split()))
                    if not coins or any(c <= 0 for c in coins):
                        raise ValueError
                    
                    # Display custom coins in user-friendly format
                    print("✅ Using custom coins:")
                    coin_display = []
                    for coin in sorted(coins):
                        if coin < 100:
                            coin_display.append(f"{coin}¢")
                        else:
                            coin_display.append(f"${coin // 100}")
                    print(", ".join(coin_display))
                except ValueError:
                    print("❌ Invalid input. Please enter positive integers only.")
                    continue

            print("\n" + "="*60)
            print("💵 TARGET AMOUNT INPUT")
            print("="*60)
            print("💡 Enter in dollar format (e.g., 3.75 for $3.75)")
            try:
                dollars = float(input("Enter target amount: $"))
                if dollars < 0:
                    raise ValueError
            except ValueError:
                print("❌ Invalid input. Please enter a non-negative number.")
                continue

            target = int(round(dollars * 100))
            result, breakdown = min_coins_with_breakdown(coins, target)

            print("\n" + "="*60)
            print("🎯 FINAL RESULT")
            print("="*60)

            if result == -1:
                print(f"❌ Cannot make ${dollars:.2f} with the given denominations.")
            else:
                print(f"✅ To make ${dollars:.2f}, you need {result} coin(s).")
                print("\n📦 Coin Breakdown:")
                display_breakdown(breakdown, coin_labels)
                total_value = sum(coin * count for coin, count in breakdown.items())
                print(f"\n🧾 Verification: Total value = ${total_value / 100:.2f}")

            print("\n\n" + "="*60)
            print("What would you like to do next?")
            print("1. Back to Main Menu")
            print("2. Exit")
            next_action = input("Enter your choice (1-2): ")
            if next_action == '2':
                print("\n👋 Thank you for using the Coin Change Solver!\n")
                break
        else:
            print("❌ Invalid choice. Please enter 0, 1, or 2.")    

# Entry point of the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thank you for using our Coin Change Solver, goodbye!")