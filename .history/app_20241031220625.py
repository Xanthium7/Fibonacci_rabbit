

def rabbit_population(n):
    if n <= 2:
        return 1
    population = [1, 1]
    for _ in range(2, n):
        total_pairs = population[-1] + population[-2]  # Total pairs
        population.append(total_pairs)
    return population[-1]


"""
Let R(n) be the number of rabbit pairs in month n
R(n) = R(n-1) + R(n-2) for n > 2

Reasoning:
- R(n-1): Mature pairs from previous month
- R(n-2): New pairs produced by mature pairs 
  (pairs that became mature 2 months ago)
"""


def main():
    while True:
        months = int(
            input("Enter number of months to calculate rabbit population (or 0 to exit): "))
        if months == 0:
            break
        if months < 0:
            print("Please enter a non-negative integer.")
            continue
        population = rabbit_population(months)
        print(f"\nRabbit pairs after {months} months: {population}")


if __name__ == "__main__":
    main()

# Theoretical Analysis
"""
Time Complexity: O(n)
Space Complexity: O(n)

Mathematical Representation:
R(n) follows a recurrence relation R(n) = R(n-1) + R(n-2)
Similar to Fibonacci, but with different initial conditions

Mathematical Formula (Approximate):
Close to golden ratio growth: φ^n / √5
Where φ = (1 + √5) / 2 ≈ 1.618034 (golden ratio)

Example Sequence:
Month 1: 1 pair
Month 2: 1 pair
Month 3: 2 pairs
Month 4: 3 pairs
Month 5: 5 pairs
Month 6: 8 pairs
... and so on
"""
