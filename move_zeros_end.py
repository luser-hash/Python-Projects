def move_zeros_end(arr):
    """
        Given an array of integers we move them to the end of the array while maintaining relative order of non-zero elements.
        Steps:
            1. We use two pointer to traverse the array.
            2. We check if current element is Non zero
            3. If so, we swap the position and increment the value of j to 1
            4. After the first loop, Value of j updated and Second loop starts. 
            5. It fills the remaining indexs with zero.

        Time complexity: O(n) 
             
    """

    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1 
        
    while j < len(arr):
        arr[j] = 0
        j += 1
        
    return arr



arr = [1,0,2,3]
print(move_zeros_end(arr))