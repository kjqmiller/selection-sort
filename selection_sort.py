# Selection sort, find smallest element and place it up front, repeat until on last index
# Start on current start index, look through rest of array, swap index as needed, move up one index
arr = [5, 36, 1, 1, 8885, 43, 77, 102, 19, -5, 14.8, 0]
print(f'Unsorted array: {arr}')

# Outer loop sets current lowest unsorted index
for i in range(0, len(arr)):
    # Search rest of array for something smaller than arr[i]
    for ii in range(i + 1, len(arr)):
        if arr[ii] < arr[i]:
            # Swap the two if a smaller value is found
            arr[i], arr[ii] = arr[ii], arr[i]

# Print array as proof it was sorted
print(f'Sorted array: {arr}')
