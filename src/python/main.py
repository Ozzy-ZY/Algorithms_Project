# Insertion Sort - Iterative Implementation
def insertion_sort_iterative(array):
    # Start from the second element (index 1) as we consider the first element as already sorted
    for current_index in range(1, len(array)):
        current_element = array[current_index]
        insertion_position = current_index
        
        # Keep moving the current element left as long as it's smaller than the element to its left
        # This creates a "gap" that moves left until we find the right spot for our current element
        while (insertion_position > 0 and current_element < array[insertion_position - 1]):
            # Swap the current element with the one to its left
            # Think of this like sliding cards in a hand of cards - we're making room for our card
            temp_element = array[insertion_position - 1]
            array[insertion_position - 1] = array[insertion_position]
            array[insertion_position] = temp_element
            insertion_position -= 1  # Move left to continue comparing

# Insertion Sort - Recursive Implementation
def insertion_sort_recursive(array, array_size=None):
    # On first call, if array_size isn't provided, set it to the array length
    if array_size is None:
        array_size = len(array)
    
    # Base case: If we're down to 1 element, it's already sorted - nothing to do
    if array_size <= 1:
        return
    
    # The magic of recursion! First, make sure the first n-1 elements are sorted
    # This is like saying "I trust my past self to have already sorted this portion"
    insertion_sort_recursive(array, array_size - 1)
    
    # Now, insert the nth element (which is at index n-1) into its correct position
    # among the previously sorted elements
    element_to_insert = array[array_size - 1]  # This is the element we're trying to place correctly
    comparison_position = array_size - 2  # Start comparing with the element to its left
    
    # Shift elements right until we find where our current element belongs
    # Like making space in a bookshelf by pushing books to the right
    while comparison_position >= 0 and array[comparison_position] > element_to_insert:
        array[comparison_position + 1] = array[comparison_position]  # Shift this element right
        comparison_position -= 1
    
    # We've found the right spot - place our element there
    array[comparison_position + 1] = element_to_insert

# Helper function for merge sort - merges two sorted subarrays into one
def _merge_sort_helper(array, left_start_idx, left_end_idx, right_start_idx, right_end_idx):
    # Create temporary arrays to hold our sorted subarrays
    # Think of these as two sorted piles of cards on a table
    left_subarray = []
    right_subarray = []
    
    # Copy the left subarray (the first sorted pile)
    for idx in range(left_start_idx, left_end_idx + 1):
        left_subarray.append(array[idx])
    
    # Copy the right subarray (the second sorted pile)
    for idx in range(right_start_idx, right_end_idx + 1):
        right_subarray.append(array[idx])
    
    # Keep track of our position in each pile and where we're placing cards in the final array
    left_position = 0
    right_position = 0
    merge_position = left_start_idx
    left_size = left_end_idx - left_start_idx + 1
    right_size = right_end_idx - right_start_idx + 1
    
    # Compare the top cards from each pile, and take the smaller one each time
    # This is like taking cards from two sorted piles to create one bigger sorted pile
    while left_position < left_size and right_position < right_size:
        if left_subarray[left_position] <= right_subarray[right_position]:
            # Left card is smaller (or equal), so take it
            array[merge_position] = left_subarray[left_position]
            left_position += 1
        else:
            # Right card is smaller, so take it
            array[merge_position] = right_subarray[right_position]
            right_position += 1
        merge_position += 1
    
    # If we've gone through one pile but not the other, just take all remaining cards
    # from the non-empty pile (they're already in order)
    while left_position < left_size:
        array[merge_position] = left_subarray[left_position]
        left_position += 1
        merge_position += 1
    
    while right_position < right_size:
        array[merge_position] = right_subarray[right_position]
        right_position += 1
        merge_position += 1

# Merge Sort - Iterative Implementation
def merge_sort_iterative(array):
    array_length = len(array)
    # Start by treating each element as a sorted 1-element subarray
    subarray_size = 1
    
    # Double the size of subarrays we're merging in each pass
    # First we merge 1-element subarrays into 2-element subarrays,
    # then 2-element into 4-element, and so on
    while subarray_size < array_length:
        # Walk through the array, merging adjacent subarrays of the current size
        current_position = 0
        while current_position < array_length:
            # Define the boundaries of our two subarrays to merge
            left_start = current_position
            left_end = min(current_position + subarray_size - 1, array_length - 1)
            right_start = left_end + 1
            right_end = min(right_start + subarray_size - 1, array_length - 1)
            
            # Only merge if we have elements in the right subarray
            # (we might hit the end of the array with an incomplete pair)
            if right_start < array_length:
                _merge_sort_helper(array, left_start, left_end, right_start, right_end)
            
            # Move to the next pair of subarrays
            current_position = right_end + 1
        
        # Double the subarray size for the next pass
        subarray_size *= 2

# Merge Sort - Recursive Implementation
def merge_sort_recursive(array, left_boundary=None, right_boundary=None):
    # On first call, if bounds aren't provided, sort the entire array
    if left_boundary is None and right_boundary is None:
        left_boundary = 0
        right_boundary = len(array) - 1
    
    # Base case: If the subarray has 0 or 1 elements, it's already sorted
    if left_boundary < right_boundary:
        # Find the middle point to divide the array into two halves
        middle_point = (left_boundary + right_boundary) // 2
        
        # The key insight of merge sort: divide and conquer!
        # First, recursively sort both halves
        merge_sort_recursive(array, left_boundary, middle_point)      # Sort left half
        merge_sort_recursive(array, middle_point + 1, right_boundary) # Sort right half
        
        # Then merge the sorted halves
        # Like shuffling two sorted decks of cards together
        _merge_helper_recursive(array, left_boundary, middle_point, right_boundary)

# Helper function for recursive merge sort
def _merge_helper_recursive(array, left_idx, middle_idx, right_idx):
    # Create temporary arrays to hold our sorted subarrays
    # We're making copies so we can overwrite the original array as we merge
    left_subarray = array[left_idx:middle_idx+1]
    right_subarray = array[middle_idx+1:right_idx+1]
    
    # Merge the arrays back into array[left_idx..right_idx]
    # This is like taking cards from two sorted piles to build one big sorted pile
    left_position = 0   # Tracks position in left subarray
    right_position = 0  # Tracks position in right subarray
    merge_position = left_idx  # Tracks position in the original array where we're putting elements
    
    # Compare elements from both arrays and place the smaller one first
    while left_position < len(left_subarray) and right_position < len(right_subarray):
        if left_subarray[left_position] <= right_subarray[right_position]:
            array[merge_position] = left_subarray[left_position]
            left_position += 1
        else:
            array[merge_position] = right_subarray[right_position]
            right_position += 1
        merge_position += 1
    
    # If one array is exhausted, copy the remaining elements from the other
    # These elements are already sorted, so we just need to place them in order
    while left_position < len(left_subarray):
        array[merge_position] = left_subarray[left_position]
        left_position += 1
        merge_position += 1
    
    while right_position < len(right_subarray):
        array[merge_position] = right_subarray[right_position]
        right_position += 1
        merge_position += 1

# Bubble Sort - Iterative Implementation
def bubble_sort_iterative(array):
    array_length = len(array)
    # We need at most n-1 passes through the array
    for pass_number in range(0, array_length - 1):
        # Assume the array is sorted until we find out otherwise
        is_already_sorted = True
        
        # In each pass, bubble the largest unsorted element to the end
        # Like watching bubbles in a drink rise to the top
        for comparison_idx in range(0, array_length - 1):
            # If this pair is out of order, swap them
            if (array[comparison_idx + 1] < array[comparison_idx]):
                is_already_sorted = False  # We found elements out of order, so array isn't sorted yet
                
                # Clever swap without using a temporary variable
                # This uses the properties of addition and subtraction
                array[comparison_idx] = array[comparison_idx] + array[comparison_idx + 1]      # a = a + b
                array[comparison_idx + 1] = array[comparison_idx] - array[comparison_idx + 1]  # b = a - b = (a + b) - b = a
                array[comparison_idx] = array[comparison_idx] - array[comparison_idx + 1]      # a = (a + b) - a = b
        
        # If we made a pass without any swaps, the array is already sorted!
        # This is an optimization to exit early
        if is_already_sorted:
            break

# Bubble Sort - Recursive Implementation
def bubble_sort_recursive(array, array_size=None):
    # On first call, if array_size isn't provided, set it to the array length
    if array_size is None:
        array_size = len(array)
    
    # Base case: If we're down to 1 element, it's already sorted
    if array_size == 1:
        return
    
    # One pass of bubble sort - bubble up the largest element to the end
    for comparison_idx in range(array_size - 1):
        if array[comparison_idx] > array[comparison_idx + 1]:
            # Swap using the same clever technique as in the iterative version
            array[comparison_idx] = array[comparison_idx] + array[comparison_idx + 1]
            array[comparison_idx + 1] = array[comparison_idx] - array[comparison_idx + 1]
            array[comparison_idx] = array[comparison_idx] - array[comparison_idx + 1]
    
    # At this point, the largest element is at the end
    # Now recursively sort the rest of the array (excluding the last element)
    # Think of it as "the largest bubble has risen to the top, now let's handle the rest"
    bubble_sort_recursive(array, array_size - 1)

# Main program - read numbers from standard input and sort them
import sys

# Parse space-separated integers from a single line of input
input_numbers = list(map(int, sys.stdin.readline().split()))

# Sort the numbers using one of our sorting algorithms
bubble_sort_iterative(input_numbers)

# Print the sorted numbers with spaces between them
for sorted_num in input_numbers:
    print(f"{sorted_num}", end=" ")