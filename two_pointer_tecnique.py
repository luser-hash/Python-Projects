# Two Sum problem - Pair Sum in sorted array

def two_sum(arr: list, target: int) -> list:
    """
    Two Pointer Technique: This approach uses two pointers to traverse a data structure either toward each other or 
    in the same direction to solve the problem efficiently. 
    
    Steps: 
        1. Set two pointer at the begining and end of the array.
        2. While loop to run as mush as it needs to run. 
        3. Conditions to check if there is a pair that matched the target Value.
        4. No pair that match return None. 

    Time complexity: O(n)
    """

    left, right = 0, len(arr) -1

    while left < right:
        current_sum  = arr[left] + arr[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else: 
            right -= 1

    return None #if no match found, it returns None.

arr = [2,7,8,9]
target = 20
print(two_sum(arr,target)) # output: None