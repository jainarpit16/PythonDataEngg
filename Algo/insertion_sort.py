def insertion_sort(arr):
    """
    Optimized insertion sort implementation with best performance practices.
    Time complexity: O(n²) worst case, O(n) best case
    Space complexity: O(1)
    """
    if len(arr) <= 1:
        return arr
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test with sample data
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    
    sorted_array = insertion_sort(test_array.copy())
    print(f"Sorted array: {sorted_array}")
