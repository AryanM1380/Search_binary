def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid, comparisons
    
    return -1, comparisons

# Example usage:
arr = [1,2,3,4,5,6,7,8,9,10]
x = 2
index, comparisons = binary_search(arr, x)

if index != -1:
    print(f"Element {x} found at index {index}.")
else:
    print(f"Element {x} not found.")

print(f"Number of comparisons: {comparisons}")
