# Sorting Algorithms in Python

# Bubble Sort (Iterative)
def bubble_sort_iterative(lst):# optim
    for i in range(0, len(lst) - 1):
        flag = True 
        for j in range(0, len(lst) - 1):
            if(lst[j + 1] < lst[j]):
                flag = False
                #swap
                lst[j] = lst[j] + lst[j + 1]
                lst[j + 1] = lst[j] - lst[j + 1]
                lst[j] = lst[j] - lst[j + 1]

        if flag == True:
            break

# Bubble Sort (Recursive)
def _bubble_sort_recursive(lst, i):
    if i == len(lst) - 1:
        return
    
    flag = False # same as iterative but false 
    
    if lst[i] > lst[i + 1]:
        #swap
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        flag = True
    
    if flag:
        _bubble_sort_recursive(lst, 0)
    else:
        _bubble_sort_recursive(lst, i + 1)

def bubble_sort_recursive(lst):
    _bubble_sort_recursive(lst, 0)

# Insertion Sort (Iterative)
def insertion_sort_iterative(lst):
    for j in range(1, len(lst)):
        i = j
        while(lst[i] < lst[i - 1] and i > 0):
            temp = lst[i - 1]
            lst[i - 1] = lst[i]
            lst[i] = temp 
            i -= 1

# Insertion Sort (Recursive)
def insert(lst, i):
    if i == 0:
        return
    
    if lst[i] < lst[i - 1]:
        lst[i], lst[i - 1] = lst[i - 1], lst[i]
        insert(lst, i - 1)

def _insertion_sort_recursive(lst, i):
    if i == len(lst):
        return
    
    insert(lst, i)
    
    _insertion_sort_recursive(lst, i + 1)

def insertion_sort_recursive(lst):
    _insertion_sort_recursive(lst, 1)

# Merge Sort (Iterative)
def _merge_sort_iterative(lst, l1, r1, l2, r2):
    L = [] 
    R = []
    for i in range(l1, r1 + 1):
        L.append(lst[i])

    for i in range(l2, r2 + 1):
        R.append(lst[i])

    i = 0
    j = 0
    k = l1
    n1 = r1 - l1 + 1
    n2 = r2 - l2 + 1

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
            k += 1
        else:
            lst[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1

def merge_sort_iterative(lst):
    size = len(lst)
    inc = 1

    while inc < size:
        i = 0
        while i < size:
            l1 = i 
            r1 = i + inc - 1
            l2 = r1 + 1 
            r2 = l2 + inc - 1
            if r1 >= size: r1 = size - 1
            if r2 >= size: r2 = size - 1
            _merge_sort_iterative(lst, l1, r1, l2, r2)
            i = r2 + 1
        inc *= 2

# Merge Sort (Recursive)
def divide(lst, l, r):
    if l < r:
        l1, r1 = l, (l + r) // 2
        l2, r2 = r1 + 1, r
        divide(lst, l1, r1)
        divide(lst, l2, r2)
        _merge_sort_recursive(lst, l1, r1, l2, r2)

def _merge_sort_recursive(lst, l1, r1, l2, r2):
    L = [] 
    R = []
    for i in range(l1, r1 + 1):
        L.append(lst[i])

    for i in range(l2, r2 + 1):
        R.append(lst[i])

    i = 0
    j = 0
    k = l1
    n1 = r1 - l1 + 1
    n2 = r2 - l2 + 1

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
            k += 1
        else:
            lst[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1

def merge_sort_recursive(lst):
    divide(lst, 0, len(lst) - 1)

# Example usage
if __name__ == "__main__":
    import sys
    
    # Read input directly as a list of numbers
    line = sys.stdin.readline().strip()
    lst = list(map(int, line.split()))
    
    # Choose which sorting algorithm to use
    # bubble_sort_iterative(lst)         # Iterative bubble sort
    # bubble_sort_recursive(lst)  # Recursive bubble sort
    # insertion_sort_iterative(lst)      # Iterative insertion sort
    # insertion_sort_recursive(lst) # Recursive insertion sort
    # merge_sort_iterative(lst)          # Iterative merge sort
    merge_sort_recursive(lst)    # Recursive merge sort
    
    for i in lst:
        print(f"{i}", end=" ")