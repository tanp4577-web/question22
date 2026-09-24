def sum_list(numbers):
    """Returns the sum of all elements in the list."""
    return sum(numbers)

def count_negatives(numbers):
    """Returns the count of negative numbers in the list."""
    return sum(1 for n in numbers if n < 0)
