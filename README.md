
# Big O

## Linear search O(n)

**Optimizations, Analysis, and Explanations**:

The linear search algorithm is pretty good for unsorted arrays because you have to check each element one by one in the worst case. But if the array is sorted, you can use a faster algorithm like binary search. For unsorted arrays, there's not much we can do to make it faster without adding some extra steps or changes.

## Bubble Sort O(n^2)

**Optimizations, Analysis, and Explanations**:

The bubble sort algorithm sorts an array by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. This process continues until the array is sorted. We always go through the whole array, even if it’s already sorted. This can be improved by adding a check to stop early if no swaps are made during a pass. If no swaps are made, it means the array is already sorted, and there’s no need for further passes.