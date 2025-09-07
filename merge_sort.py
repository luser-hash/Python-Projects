# Merge Sort
""" It divides the array into smaller subarray until it reach size of 1
    Then it merges the subarrays into sorted Order. This process is repeated until all subarrays
    are merged into a single sorted array. It is based on Divide and conquer algorithm.
    Time Complexity is O(n Log n) in all Cases. Log n is for dividing because it always 
    divides the array into two halves and n is for merging the divided arrays."""

""" Workflow:

    1. Divide the unsorted array into n subarrays, each containing one element.
    2. Repeteadly mege subarrays to produce new sorted subarrays until there is only one subarray remaining.
    3. The remaining subarray is the sorted array.
    
    Pseudo Code:
    MergeSort(arr[]):
        if len(arr) <= 1:
            return arr

        mid -> len(arr) // 2
        left -> MergeSort(arr[:mid])
        right -> MergeSort(arr[mid:])

        return (left, right)

        This process Recursivley divides the aeeay into halves until it reaches size of One.
        This time complexity is O(Log n).

    Merge(left, right):
        result -> []
        i -> j -> 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        Add the remaining elements of left and right ( if any)
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    """

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add the remaining
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example Usage

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Unsorted Array:", arr)
print("Sorted Array:", sorted_arr)





