def insertion_sort_iterative(arr):
    """Sort an array using insertion sort algorithm."""
    for index in range(1, len(arr)):
        current_position = index
        while (arr[current_position] < arr[current_position - 1] and current_position > 0):
            # Swap elements
            temp = arr[current_position - 1]
            arr[current_position - 1] = arr[current_position]
            arr[current_position] = temp
            current_position -= 1


def _merge_sort_helper(arr, left_start, left_end, right_start, right_end):
    """Merge two sorted subarrays."""
    left_subarray = []
    right_subarray = []
    
    # Fill temporary subarrays
    for i in range(left_start, left_end + 1):
        left_subarray.append(arr[i])

    for i in range(right_start, right_end + 1):
        right_subarray.append(arr[i])

    left_index = 0
    right_index = 0
    merge_index = left_start
    left_size = left_end - left_start + 1
    right_size = right_end - right_start + 1

    # Merge subarrays
    while left_index < left_size and right_index < right_size:
        if left_subarray[left_index] <= right_subarray[right_index]:
            arr[merge_index] = left_subarray[left_index]
            left_index += 1
            merge_index += 1
        else:
            arr[merge_index] = right_subarray[right_index]
            right_index += 1
            merge_index += 1

    # Copy remaining elements
    while left_index < left_size:
        arr[merge_index] = left_subarray[left_index]
        left_index += 1
        merge_index += 1
    
    while right_index < right_size:
        arr[merge_index] = right_subarray[right_index]
        right_index += 1
        merge_index += 1


def merge_sort_iterative(arr):
    """Sort an array using iterative merge sort algorithm."""
    arr_size = len(arr)
    subarray_size = 1

    while subarray_size < arr_size:
        current_index = 0
        while current_index < arr_size:
            left_start = current_index
            left_end = min(current_index + subarray_size - 1, arr_size - 1)
            right_start = left_end + 1
            right_end = min(right_start + subarray_size - 1, arr_size - 1)
            
            if right_start < arr_size:
                _merge_sort_helper(arr, left_start, left_end, right_start, right_end)
            
            current_index = right_end + 1
        
        subarray_size *= 2


def bubble_sort_iterative(arr):
    """Sort an array using bubble sort algorithm."""
    for i in range(0, len(arr) - 1):
        is_sorted = True
        for j in range(0, len(arr) - 1):
            if (arr[j + 1] < arr[j]):
                is_sorted = False
                
                arr[j] = arr[j] + arr[j + 1]
                arr[j + 1] = arr[j] - arr[j + 1]
                arr[j] = arr[j] - arr[j + 1]

        if is_sorted:
            break


import sys

numbers = list(map(int, sys.stdin.readline().split()))

bubble_sort_iterative(numbers)

for num in numbers:
    print(f"{num}", end=" ")