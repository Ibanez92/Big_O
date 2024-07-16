def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the numbers if new number is less than the old one
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Tests
array = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(array))  
# Output: [11, 12, 22, 25, 34, 64, 90]

array = [5, 1, 4, 2, 8]
print(bubble_sort(array))  
# Output: [1, 2, 4, 5, 8]
