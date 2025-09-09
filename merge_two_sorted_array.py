def two_merge(arr1,arr2):
    """
        This merges Swo Sorted array Using Two pinter Technique.
        two pointer traversal the while loop. check for smaller element to add.
        .extend use to add any leftover. 

        Time complexity: O(n+m)
        space complexity: O(n+m) because of final_array. 

    """
    final_arr = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            final_arr.append(arr1[i])
            i += 1
        else:
            final_arr.append(arr2[j])
            j += 1
    final_arr.extend(arr1[i:])
    final_arr.extend(arr2[j:])
    return final_arr

arr1 = [1,3,5,14]
arr2 = [0,0,2,4,6,7]
print(two_merge(arr1,arr2))