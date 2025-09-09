# Cumulative sum array -> The i'th element of array is the cumulative sum of previous elements and itself. 

def cumulative_sum(arr: list) -> list:

    """
    Suppose:
    Original arr = [1,2,3,4]
    Cumulative_sum_array: [1,3,6,10] 
    
    Steps:
    1. Iterate through the array and add it's cumulative_sum_elements into a new array. \
    
    Time complexity: O(n), Beacuse we iterate through each element only once. """

    new_arr = []
    pre = 0

    for i in range(len(arr)):
        pre += arr[i]
        new_arr.append(pre)

    return new_arr

arr = [2,4,6,8] 
c_s = cumulative_sum(arr)
print(c_s) # Output: [2, 6, 12, 20]