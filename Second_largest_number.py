# find the second largest element in an array

"""
    This approach traverse the array only once. 
    Workflow:
    1. Initialize the variable first and second to negetive infinity.
    So that any number in the array will be larger than the initial value.
    2. Traverse the array and for each element compare with first to check it it is larger.
    Say  [5,8] -> 
        first = -inf, second = -inf
        num = 5 -> 5 > -inf -> second = old value of first = -inf, first = 5
        num = 8 -> 8 > 5 -> second = old value of first = 5, first = 8
        so at the end first = 8, second = 5

    3. If the current element is not larger than first, check if it is larger than second and smaller than first.
    Say [9, 7, 5]
        num 9 -> first = 9, second = -inf
        num 7 -> 7 > second and 7 != 9 → second = 7
        num 5 -> not greater than second (7) → no update

    4. At the end of the traversal return second.

    Full example walkthrough:
    arr = [12, 35, 1, 10, 34, 1]
    first = -inf, second = -inf
    num = 12 -> 12 > -inf -> second = -inf, first = 12
    num = 35 -> 35 > 12 -> second = 12, first = 35
    num = 1 -> not greater than first (35) 1 > second (12) is false -> no update
    num = 10 -> not greater than first (35) 10 > second (12) is false -> no update
    num = 34 -> not greater than first (35) 34 > second (12) is true -> second = 34
    num = 1 -> not greater than first (35) 1 > second (34) is false -> no update
    End of traversal -> return second = 34

    Time Complexity: O(n), where n is the number of elements in the array.
  
""" 

def second_largest(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None

# Example usage:
print(second_largest([12, 35, 1, 10, 34, 1])) # Output: 34
print(second_largest([10, 5, 10])) # Output: 5
print(second_largest([5])) # Output: None


