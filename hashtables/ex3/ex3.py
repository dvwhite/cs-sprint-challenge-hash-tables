def intersection(arrays):
    """
    Return the intersection of two array without using sets or numpy, by
    using hash tables to keep track of the counts of each number in each
    array, and returning the list of numbers with a count equal to the 
    number of arrays (the len of arrays param)
    """
    # Create an array of numbers mapped to their counts in the arrays
    counts = {}
    for array in arrays:
        for num in array:
            counts[num] = counts.get(num, 0) + 1

    # Return the numbers that were present in all arrays by identifying
    # intersections. We do so by selecting numbers incremented in each array
    # pass
    result = [num for num in counts if counts[num] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
