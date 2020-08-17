def has_negatives(a):
    """
    Return a list of integers in a that have a corresponding negative
    equivalent in the list
    """
    # Create a set for the absolute value of each number
    # If a negative equivalent is found, it will entered in the set for
    # that number. This will handle repeats and make it more readable
    # than having multiple negative and positive copies of the target num
    counts = {abs(num): set() for num in a}
    for num in a:
        counts[abs(num)].add(num)

    # Any number with two entries (a positive and a negative) in the list
    # would be returned in result
    result = [num for num in counts if len(counts[num]) == 2]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
