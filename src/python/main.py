# Works by building a sorted portion of the array one element at a time.
# For each element, it finds the correct position in the sorted portion by shifting elements right.
# Time complexity: O(n²) average and worst case, O(n) best case (already sorted)
def insertion_sort_iterative(array):
    for current_index in range(1, len(array)):
        current_element = array[current_index]
        insertion_position = current_index
        
        while (insertion_position > 0 and current_element < array[insertion_position - 1]):
            temp_element = array[insertion_position - 1]
            array[insertion_position - 1] = array[insertion_position]
            array[insertion_position] = temp_element
            insertion_position -= 1

# Same algorithm as iterative insertion sort, but using recursion.
# First sorts the first n-1 elements recursively, then inserts the nth element in its proper position.
# Time complexity: O(n²) average and worst case, O(n) best case (already sorted)
def insertion_sort_recursive(array, array_size=None):
    if array_size is None:
        array_size = len(array)
    
    if array_size <= 1:
        return
    
    insertion_sort_recursive(array, array_size - 1)
    
    element_to_insert = array[array_size - 1]
    comparison_position = array_size - 2
    
    while comparison_position >= 0 and array[comparison_position] > element_to_insert:
        array[comparison_position + 1] = array[comparison_position]
        comparison_position -= 1
    
    array[comparison_position + 1] = element_to_insert

# Unified merge helper function that works with both iterative and recursive merge sort
# Merges two sorted subarrays into one sorted array
def _merge_helper(array, left_start, middle, right_end):
    # Extract the subarrays
    left_subarray = array[left_start:middle + 1]
    right_subarray = array[middle + 1:right_end + 1]
    
    left_position = 0
    right_position = 0
    merge_position = left_start
    
    # Merge the two subarrays
    while left_position < len(left_subarray) and right_position < len(right_subarray):
        if left_subarray[left_position] <= right_subarray[right_position]:
            array[merge_position] = left_subarray[left_position]
            left_position += 1
        else:
            array[merge_position] = right_subarray[right_position]
            right_position += 1
        merge_position += 1
    
    # Copy remaining elements from left subarray if any
    while left_position < len(left_subarray):
        array[merge_position] = left_subarray[left_position]
        left_position += 1
        merge_position += 1
    
    # Copy remaining elements from right subarray if any
    while right_position < len(right_subarray):
        array[merge_position] = right_subarray[right_position]
        right_position += 1
        merge_position += 1

# Divide and conquer algorithm that divides the array into equal halves, sorts them, then merges them.
# Iterative version uses bottom-up approach, starting with 1-element subarrays and doubling each pass.
# Time complexity: O(n log n) for all cases (best, average, worst)
def merge_sort_iterative(array):
    array_length = len(array)
    subarray_size = 1
    
    while subarray_size < array_length:
        current_position = 0
        while current_position < array_length:
            left_start = current_position
            left_end = min(current_position + subarray_size - 1, array_length - 1)
            right_end = min(left_end + subarray_size, array_length - 1)
            
            if left_end < right_end:  # Only merge if there's a right subarray
                _merge_helper(array, left_start, left_end, right_end)
            
            current_position = right_end + 1
        
        subarray_size *= 2

# Divide and conquer algorithm that divides the array into equal halves, sorts them, then merges them.
# Recursive version uses top-down approach, recursively splitting the array until reaching 1-element subarrays.
# Time complexity: O(n log n) for all cases (best, average, worst)
def merge_sort_recursive(array, left_boundary=None, right_boundary=None):
    if left_boundary is None and right_boundary is None:
        left_boundary = 0
        right_boundary = len(array) - 1
    
    if left_boundary < right_boundary:
        middle_point = (left_boundary + right_boundary) // 2
        
        merge_sort_recursive(array, left_boundary, middle_point)
        merge_sort_recursive(array, middle_point + 1, right_boundary)
        
        _merge_helper(array, left_boundary, middle_point, right_boundary)

# Simple sorting algorithm that repeatedly steps through the list, compares adjacent elements,
# and swaps them if they're in the wrong order. Largest elements "bubble" to the end.
# Includes optimization to exit early if a pass makes no swaps.
# Time complexity: O(n²) average and worst case, O(n) best case (already sorted)
def bubble_sort_iterative(array):
    array_length = len(array)
    
    for pass_number in range(0, array_length - 1):
        is_already_sorted = True
        
        for comparison_idx in range(0, array_length - 1):
            if (array[comparison_idx + 1] < array[comparison_idx]):
                is_already_sorted = False
                # swap
                array[comparison_idx] = array[comparison_idx] + array[comparison_idx + 1]
                array[comparison_idx + 1] = array[comparison_idx] - array[comparison_idx + 1]
                array[comparison_idx] = array[comparison_idx] - array[comparison_idx + 1]
        
        if is_already_sorted:
            break

# Same as iterative bubble sort, but implemented recursively.
# Each recursive call places the largest element at the end and then sorts the remaining array.
# Time complexity: O(n²) average and worst case, O(n) best case (already sorted)
def bubble_sort_recursive(array, array_size=None):
    if array_size is None:
        array_size = len(array)
    
    if array_size == 1:
        return
    
    for comparison_idx in range(array_size - 1):
        if array[comparison_idx] > array[comparison_idx + 1]:
            # swap
            array[comparison_idx] = array[comparison_idx] + array[comparison_idx + 1]
            array[comparison_idx + 1] = array[comparison_idx] - array[comparison_idx + 1]
            array[comparison_idx] = array[comparison_idx] - array[comparison_idx + 1]
    
    bubble_sort_recursive(array, array_size - 1)

import sys

input_numbers = list(map(int, sys.stdin.readline().split()))
bubble_sort_iterative(input_numbers)

for sorted_num in input_numbers:
    print(f"{sorted_num}", end=" ")