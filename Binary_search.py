def binary_search(arr, target):

    """
        Binary Search or BS is a nice concept of two pointer technique. It;s a Divide and conquer algorithm that always divides array into halves
        and halves until it finds the targeted value or the space is empty.  

        Steps: 
        1. Define two point to point low and half.
        2. Repeat halving until the target value if found. 
        3. change the positions of low and high
        4. Repeat 2 until done.

        Example:
        [1, 2, 4, 5, 5, 7, 9]
        Target = 7
        Steps:
        low=0, high=6 → mid=3 → arr[3]=5 < 7 → move right (low=4)
        low=4, high=6 → mid=5 → arr[5]=7 == target found

        Binary search works on Sorted array. So we must check before implementing BS if the array is sorted or not.
        Why? Because It checks it's mid and then decides whether the target value is higher or lower. So it makes Sense to be a sorted array. 
        For unsorted array we do linear search. 

        Time complexity: O(log n), because we always divides into halves. 
    """
    left = 0
    right = len(arr) -1
    
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:   # Time complexity: O(log2 n)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1 
    return -1

array = [1, 4, 2, 9, 7, 5]
array.sort()
target = 7

binary_search_result = binary_search(array, target)
print(binary_search_result)

