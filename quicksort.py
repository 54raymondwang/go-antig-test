def quick_sort(arr):
    """
    Python implementation of the Quick Sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(test_arr)
    print(f"Original array: {test_arr}")
    print(f"Sorted array: {sorted_arr}")
