"""
Task 09: Prime Number Analyzer
Objective:
    Take two numbers representing an inclusive range [start, end].
    Create functions to:
    - Determine if an individual number is prime
    - Find all prime numbers within the range
    - Count the total number of primes
    - Calculate the sum of all found primes
    - Identify the largest prime found in the range
    - Display comprehensive analytical summary
"""

from typing import List, Dict, Any, Optional


def is_prime(number: int) -> bool:
    """
    Determines whether an integer is prime using optimized trial division loop.

    Args:
        number (int): Integer to test.

    Returns:
        bool: True if prime, False otherwise.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check divisors from 5 up to sqrt(number), stepping by 6 (6k +/- 1 rule)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def find_prime_numbers(start: int, end: int) -> List[int]:
    """
    Finds all prime numbers within an inclusive range [start, end].

    Args:
        start (int): Lower bound.
        end (int): Upper bound.

    Returns:
        List[int]: List of prime numbers in ascending order.
    """
    # Ensure start <= end
    low = min(start, end)
    high = max(start, end)

    primes: List[int] = []
    for num in range(low, high + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def count_primes(primes_list: List[int]) -> int:
    """
    Counts total primes in the list using a loop.

    Args:
        primes_list (List[int]): List of prime numbers.

    Returns:
        int: Count of elements.
    """
    count = 0
    for _ in primes_list:
        count += 1
    return count


def calculate_prime_sum(primes_list: List[int]) -> int:
    """
    Calculates the sum of all prime numbers in the list using a loop.

    Args:
        primes_list (List[int]): List of prime numbers.

    Returns:
        int: Cumulative sum.
    """
    total = 0
    for prime in primes_list:
        total += prime
    return total


def get_largest_prime(primes_list: List[int]) -> Optional[int]:
    """
    Finds the largest prime number in the list.

    Args:
        primes_list (List[int]): List of prime numbers.

    Returns:
        Optional[int]: Largest prime or None if list is empty.
    """
    if not primes_list:
        return None

    largest = primes_list[0]
    for prime in primes_list:
        if prime > largest:
            largest = prime
    return largest


def analyze_primes_in_range(start: int, end: int) -> Dict[str, Any]:
    """
    Runs complete prime analysis pipeline for a given range.

    Args:
        start (int): Start of range.
        end (int): End of range.

    Returns:
        Dict[str, Any]: Detailed metrics dictionary.
    """
    low = min(start, end)
    high = max(start, end)
    primes = find_prime_numbers(low, high)
    count = count_primes(primes)
    total_sum = calculate_prime_sum(primes)
    largest = get_largest_prime(primes)
    avg = (total_sum / count) if count > 0 else 0.0

    return {
        "range_start": low,
        "range_end": high,
        "primes": primes,
        "count": count,
        "sum": total_sum,
        "largest": largest,
        "average": round(avg, 2)
    }


def display_prime_analysis(analysis: Dict[str, Any]) -> None:
    """
    Displays formatted prime analysis report.

    Args:
        analysis (Dict[str, Any]): Result from analyze_primes_in_range.
    """
    start = analysis["range_start"]
    end = analysis["range_end"]
    primes = analysis["primes"]
    count = analysis["count"]
    total = analysis["sum"]
    largest = analysis["largest"]

    print("\n" + "=" * 65)
    print(f"{'PRIME NUMBER ANALYSIS REPORT':^65}")
    print("=" * 65)
    print(f"Evaluated Range       : [{start} to {end}] (Total integers: {end - start + 1})")
    print(f"Total Primes Found    : {count}")

    if count == 0:
        print(f"Primes in Range       : None")
        print(f"Sum of Primes         : 0")
        print(f"Largest Prime         : None")
    else:
        # Format list nicely if long
        if count <= 25:
            primes_str = ", ".join(map(str, primes))
        else:
            first_few = ", ".join(map(str, primes[:12]))
            last_few = ", ".join(map(str, primes[-5:]))
            primes_str = f"{first_few} ... [+{count - 17} more] ... {last_few}"

        print(f"Primes in Range       : {primes_str}")
        print(f"Sum of Primes         : {total:,}")
        print(f"Average of Primes     : {analysis['average']:.2f}")
        print(f"Largest Prime Found   : {largest}")
    print("=" * 65 + "\n")


def main():
    """Interactive CLI runner for Prime Analyzer."""
    print("=== Super30 Prime Number Analyzer ===")
    
    # Demonstration run
    print("Demonstration on range [10, 50]:")
    demo_res = analyze_primes_in_range(10, 50)
    display_prime_analysis(demo_res)

    while True:
        try:
            start_in = input("Enter range start number (or 'exit' to quit): ").strip()
            if start_in.lower() == 'exit':
                print("Exiting Prime Number Analyzer. Goodbye!")
                break
            start_num = int(start_in)

            end_in = input("Enter range end number: ").strip()
            end_num = int(end_in)

            result = analyze_primes_in_range(start_num, end_num)
            display_prime_analysis(result)

            again = input("Analyze another range? (y/n): ").strip().lower()
            if again != 'y':
                print("Session ended.")
                break
        except ValueError:
            print("[!] Invalid integer. Please enter whole numbers.")


if __name__ == "__main__":
    main()
