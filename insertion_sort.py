def insertion_sort(arr):
    """
    Sort a list of numbers in monotonically decreasing order.

    Args:
        arr: A list of numbers.

    Returns:
        The same list, sorted from largest to smallest.
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # Shift smaller elements one position to the right.
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        # Insert the current element in its correct position.
        arr[i + 1] = key

    return arr


if __name__ == "__main__":
    numbers = [5, 2, 4, 6, 1, 3]

    print("Original array:", numbers)

    sorted_numbers = insertion_sort(numbers)

    print("Sorted array (decreasing order):", sorted_numbers)