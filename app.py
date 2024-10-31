

def rabbit_population(n):
    if n <= 2:
        return 1

    population = [1, 1]

    for _ in range(2, n):
        total_pairs = population[-1] + population[-2]  # Total pairs
        population.append(total_pairs)

    return population[-1]


def print_rabbit_population_table(months):
    """
    Print a table showing rabbit population growth

    Parameters:
    months (int): Number of months to calculate
    """
    print("Month | Rabbit Pairs")
    print("-" * 20)
    for month in range(1, months + 1):
        pairs = rabbit_population(month)
        print(f"{month:5} | {pairs:12}")


# Recurrence Relation Explanation
"""

Let R(n) be the number of rabbit pairs in month n

Recurrence Relation:
R(1) = 1  # Initial pair
R(2) = 1  # First pair matures
R(n) = R(n-1) + R(n-2) for n > 2

Reasoning:
- R(n-1): Mature pairs from previous month
- R(n-2): New pairs produced by mature pairs 
  (pairs that became mature 2 months ago)

This is similar to Fibonacci, but with the key difference 
of the 2-month maturation period before breeding begins.
"""


def main():
    # Interactive user input
    while True:
        try:
            months = int(
                input("Enter number of months to calculate rabbit population (or 0 to exit): "))

            # Exit condition
            if months == 0:
                break

            # Validate input
            if months < 0:
                print("Please enter a non-negative integer.")
                continue

            # Calculate and display results
            population = rabbit_population(months)
            print(f"\nRabbit pairs after {months} months: {population}")

            # Optional: Print full population table
            print("\nPopulation Growth Table:")
            print_rabbit_population_table(months)

            print("\n" + "="*40)

        except ValueError:
            print("Invalid input. Please enter a valid number.")


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
