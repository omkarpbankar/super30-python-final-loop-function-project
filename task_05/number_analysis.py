"""
Task 05: Number Analysis Tool
Objective:
    Create a function that accepts a list of numbers and returns:
    - largest number
    - smallest number
    - total
    - average
    - even count
    - odd count
    - positive count
    - negative count

CRITICAL CONSTRAINT:
    Do NOT use Python's built-in min(), max(), or sum() functions.
    All aggregations, extrema, and counts are implemented from first principles
    using loops and conditionals.
"""

from typing import List, Dict, Union, Optional, Any


def analyze_numbers(numbers: List[Union[int, float]]) -> Optional[Dict[str, Union[int, float]]]:
    """
    Analyzes a sequence of numbers and computes statistical metrics WITHOUT min(), max(), or sum().

    Args:
        numbers (List[Union[int, float]]): List of integers or floats.

    Returns:
        Optional[Dict[str, Union[int, float]]]: Dictionary containing:
            - 'largest': Largest number
            - 'smallest': Smallest number
            - 'total': Sum of all numbers
            - 'average': Arithmetic mean
            - 'even_count': Count of even integers
            - 'odd_count': Count of odd integers
            - 'positive_count': Count of numbers > 0
            - 'negative_count': Count of numbers < 0
            - 'zero_count': Count of numbers == 0
            - 'total_elements': Total count of elements
            Returns None if input list is empty.
    """
    if not numbers:
        return None

    # Step 1: Initialize accumulators and extrema from the first element
    count = 0
    total = 0.0
    largest = numbers[0]
    smallest = numbers[0]
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Step 2: Single-pass iteration across the list
    for num in numbers:
        count += 1
        total += num

        # Determine largest (Custom algorithm without max())
        if num > largest:
            largest = num

        # Determine smallest (Custom algorithm without min())
        if num < smallest:
            smallest = num

        # Positivity / Negativity / Zero
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

        # Parity check (Even / Odd for whole numbers)
        # Note: Floats with non-zero decimals are not strictly classified as even/odd integers
        if isinstance(num, int) or (isinstance(num, float) and num.is_integer()):
            int_val = int(num)
            if int_val % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Calculate average
    average = total / count if count > 0 else 0.0

    return {
        "largest": largest,
        "smallest": smallest,
        "total": round(total, 4),
        "average": round(average, 4),
        "even_count": even_count,
        "odd_count": odd_count,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "zero_count": zero_count,
        "total_elements": count
    }


def display_analysis_report(numbers: List[Union[int, float]], results: Optional[Dict[str, Any]] = None) -> None:
    """
    Prints a formatted analysis report for the numbers.

    Args:
        numbers (List[Union[int, float]]): Original input numbers.
        results (Optional[Dict[str, Any]]): Precomputed results dictionary.
    """
    if results is None:
        results = analyze_numbers(numbers)

    print("\n" + "=" * 55)
    print(f"{'NUMBER ANALYSIS REPORT':^55}")
    print("=" * 55)
    print(f"Input List       : {numbers}")
    print("-" * 55)

    if results is None:
        print("[!] Input list is empty. No analysis available.")
        print("=" * 55 + "\n")
        return

    print(f"Total Elements   : {results['total_elements']}")
    print(f"Largest Number   : {results['largest']}")
    print(f"Smallest Number  : {results['smallest']}")
    print(f"Sum / Total      : {results['total']}")
    print(f"Average (Mean)   : {results['average']:.4f}")
    print(f"Even Numbers     : {results['even_count']}")
    print(f"Odd Numbers      : {results['odd_count']}")
    print(f"Positive (> 0)   : {results['positive_count']}")
    print(f"Negative (< 0)   : {results['negative_count']}")
    print(f"Zeroes (== 0)    : {results['zero_count']}")
    print("=" * 55 + "\n")


def parse_number_list_input(raw_input: str) -> List[float]:
    """
    Parses a space or comma separated string of numbers into a list of floats/ints.

    Args:
        raw_input (str): Raw user string input.

    Returns:
        List[float]: Parsed numbers list.
    """
    delimiters_replaced = raw_input.replace(",", " ")
    tokens = delimiters_replaced.split()
    numbers: List[float] = []

    for token in tokens:
        clean_token = token.strip()
        if clean_token:
            val = float(clean_token)
            # Retain integer type if no fractional part
            if val.is_integer():
                numbers.append(int(val))
            else:
                numbers.append(val)
    return numbers


def main():
    """Interactive loop for the Number Analysis Tool."""
    print("=== Super30 Number Analysis Tool (Zero Built-in Aggregation) ===")
    print("Analyze any list of numbers without min(), max(), or sum().\n")

    # Demonstrate with a sample run
    sample = [12, -7, 45, 0, 88, -23, 14, 99, 102, -5, 30]
    print("Demonstration on sample list:")
    display_analysis_report(sample)

    while True:
        user_in = input("Enter numbers separated by spaces or commas (or 'exit' to quit): ").strip()
        if user_in.lower() == 'exit':
            print("Exiting Number Analysis Tool. Goodbye!")
            break
        if not user_in:
            print("[!] Please enter at least one number.")
            continue

        try:
            num_list = parse_number_list_input(user_in)
            if not num_list:
                print("[!] No valid numbers parsed.")
                continue
            display_analysis_report(num_list)
        except ValueError:
            print("[!] Error: Could not parse input. Please ensure all values are numbers.")


if __name__ == "__main__":
    main()
