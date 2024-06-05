# Binary Search Algorithm

This repository contains an implementation of the Binary Search algorithm in Python. The Binary Search algorithm is an efficient way to find the position of a target value within a sorted array. The time complexity of this algorithm is O(log n), making it suitable for large datasets.

## Function

### `binary_search(arr, x)`

Performs binary search on a sorted array `arr` to find the element `x`.

#### Parameters:

- `arr` (list): A list of sorted elements.
- `x` (int/float/str): The element to search for in the array.

#### Returns:

- `index` (int): The index of the element `x` in the array `arr`. If `x` is not found, returns -1.
- `comparisons` (int): The number of comparisons made during the search process.

## Example Usage

```python
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
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 2
index, comparisons = binary_search(arr, x)

if index != -1:
    print(f"Element {x} found at index {index}.")
else:
    print(f"Element {x} not found.")

print(f"Number of comparisons: {comparisons}")
```

### Output

```
Element 2 found at index 1.
Number of comparisons: 2
```

## How to Use

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/binary-search-algorithm.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd binary-search-algorithm
   ```

3. **Run the script:**
   ```sh
   python binary_search.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- The binary search algorithm is a classic algorithm in computer science, and its implementation is widely available in various forms. This implementation is a basic version for educational purposes.

---

Feel free to modify the `binary_search` function or the example usage to fit your specific needs. Happy coding!
