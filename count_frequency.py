# Count frequency of elements in a list

def count_frequency(arr:list) -> dict:

    """
    This function counts the frequency of each element in the input list 'arr'.  
    
    Steps:
    1. First we Initialize an empty dictionary to uniquely identify and store each element. Hence we collect all unique elements. 
    2. We Initialize counter for each unique element to zero.
    3. We traverse the again and for each element we increment it's counter in the dictionary.
    
    Time Complexity: We loop through each and every element of the arr.
                    First Loop -> Loop through each element -> O(n)
                    Second Loop -> Loop through each element -> O(n)
                    Total -> O(n) + O(n) = O(2n) = O(n)
    Finallly, O(n), Where n is the number of elements in the arr. 

    We can also use Python's collections.Counter library to count frequency.
    
    import collections
    
    frequency = collection.Counter(arr)
    
    """

    frequency = {}

    for num in arr:
        frequency[num] = 0 # num is the key and 0 is the value; because dictionary stores key-value pairs

    for num in arr:
        frequency[num] += 1 # Increment the count for each occurrence of num

    return frequency

# Example usage:
print(count_frequency([1, 2, 2, 3, 1, 4, 5, 3, 2])) # Output: {1: 2, 2: 3, 3: 2, 4: 1, 5: 1}
