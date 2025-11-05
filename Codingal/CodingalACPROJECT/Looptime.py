def myfunction(n):
    print("Code Analysis for Time Complexity\n")

    # First Loop
    print(" First Loop: for i in range(0, n+1)")
    print("   → Runs (n + 1) times")
    print("   → Time Complexity: O(n)\n")

    # Second Loop
    print(" Second Loop: while (j <= n+1)")
    print("   → j doubles each iteration (1, 2, 4, 8, ...)")
    print("   → Runs approximately log₂(n) times")
    print("   → Time Complexity: O(log n)\n")

    # Third Loop
    print(" Third Loop: for i in range(0, 100)")
    print("   → Runs fixed number of times (100 iterations)")
    print("   → Time Complexity: O(1)\n")

    # Total
    print("✅ Total Time Complexity = O(n) + O(log n) + O(1) = O(n)")


# Example call
n = 10
myfunction(n)
