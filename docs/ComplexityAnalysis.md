# Complexity Analysis

This document provides the time and space complexities of Bubble Sort, Insertion Sort, and Merge Sort for both recursive and iterative approaches.

## Time Complexity

| Sorting Algorithm  | Best Case (Ω) | Average Case (Θ) | Worst Case (O) |
|--------------------|---------------|------------------|---------------|
| **Bubble Sort (Iterative)** | O(n) | O(n²) | O(n²) |
| **Bubble Sort (Recursive)** | O(n) | O(n²) | O(n²) |
| **Insertion Sort (Iterative)** | O(n) | O(n²) | O(n²) |
| **Insertion Sort (Recursive)** | O(n) | O(n²) | O(n²) |
| **Merge Sort (Iterative)** | O(n log n) | O(n log n) | O(n log n) |
| **Merge Sort (Recursive)** | O(n log n) | O(n log n) | O(n log n) |

## Space Complexity

| Sorting Algorithm  | Space Complexity |
|--------------------|-----------------|
| **Bubble Sort (Iterative)** | O(1) |
| **Bubble Sort (Recursive)** | O(n) (due to recursion depth) |
| **Insertion Sort (Iterative)** | O(1) |
| **Insertion Sort (Recursive)** | O(n) (due to recursion depth) |
| **Merge Sort (Iterative)** | O(n) (for auxiliary arrays) |
| **Merge Sort (Recursive)** | O(n) (for auxiliary arrays and recursion stack) |

## Notes:
- **Bubble Sort and Insertion Sort** are in-place algorithms, meaning they require O(1) space in their iterative versions.
- **Recursive Bubble Sort and Recursive Insertion Sort** require O(n) space due to recursion depth.
- **Merge Sort** is not an in-place sorting algorithm as it requires additional space (O(n)) for merging.
- **Merge Sort (Recursive)** has an additional O(log n) space requirement due to recursive function calls.

This complexity analysis helps in choosing the right sorting algorithm based on the requirements and constraints of the problem.

