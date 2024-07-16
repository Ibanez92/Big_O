def linear_search(arr, target):
    # The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
    # The enumerate() function adds a counter as the key of the enumerate object.
    # enumerate(iterable, start)
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Tests
array = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search(array, target)}")  # Output: -1