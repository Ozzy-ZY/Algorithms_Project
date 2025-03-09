# Sorting Algorithms

## Bubble Sort

Bubble Sort is a simple comparison-based algorithm that works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The algorithm gets its name because smaller elements "bubble" to the top (beginning) of the list, and larger elements "sink" to the bottom (end) as the process is repeated.

Bubble Sort is inefficient for large datasets but is still used in scenarios where simplicity is key.

### Time Complexity:

- **Best Case:** O(n) (when the list is already sorted)
- **Average Case:** O(n²)
- **Worst Case:** O(n²)

### Space Complexity:

- O(1) (in-place sorting)

### How it works:

1. Compare adjacent elements in the array.
2. Swap the elements if the left one is greater than the right one.
3. Repeat this process for every pair of adjacent elements in the array.
4. Continue this process for every element until no swaps are needed, indicating that the list is sorted.

### Real-World Applications:

- **Teaching Sorting Concepts:**
  - Used in computer science education to teach sorting logic because of its simplicity.
  - Helps beginners understand swapping and comparisons.
- **Small Data Sorting in Embedded Systems:**
  - Used in hardware devices where memory is very limited.
  - Example: Sorting small lists of sensor readings in IoT devices.
- **Animation & Visualization:**
  - Since Bubble Sort shows clear step-by-step movements, it is used in visual demos of sorting algorithms.

---

## Insertion Sort

Insertion Sort works by building a sorted portion of the array one element at a time. It takes elements from the unsorted portion and places them in their correct position in the sorted portion.

Insertion Sort is efficient when data is almost sorted and works well for small datasets.

### Time Complexity:

- **Best Case:** O(n) (when the array is already sorted)
- **Average Case:** O(n²)
- **Worst Case:** O(n²)

### Space Complexity:

- O(1) (in-place sorting)

### How it works:

1. Start with the second element of the array (since the first element is trivially sorted).
2. Compare the current element with the elements in the sorted portion, starting from the end of the sorted portion.
3. Shift the elements of the sorted portion one position to the right to make space for the current element.
4. Insert the current element in the correct position.
5. Repeat the process for each remaining element until the entire array is sorted.

### Real-World Applications:

- **Sorting Playing Cards (Manually):**
  - When sorting a hand of playing cards, you naturally use Insertion Sort, placing each card in its correct position relative to the others.
- **Autosuggestions & Typing Software:**
  - Used in applications like autocomplete & predictive text, where recently typed words are sorted dynamically.
- **Online Leaderboards in Games:**
  - When adding a new score to a sorted list of top players, Insertion Sort efficiently places it in the correct position.
- **Small Databases & Filesystem Management:**
  - Used in small databases where records are frequently updated but mostly in order.
  - Example: Sorting log files by timestamps in real-time applications.

---

## Merge Sort

Merge Sort is a divide-and-conquer algorithm. It splits the array into two halves, recursively sorts both halves, and then merges the sorted halves.

Merge Sort is one of the fastest sorting algorithms, making it ideal for big data and distributed systems.

### Time Complexity:

- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n log n)

### Space Complexity:

- O(n) (requires extra space for merging)

### How it works:

1. Divide the unsorted list into two approximately equal halves.
2. Recursively sort each half.
3. Merge the two sorted halves back together to form a sorted list.

### Real-World Applications:

- **Sorting Large Data Sets (Big Data & Search Engines):**
  - Google Search & Database Management Systems use Merge Sort or variations like Timsort (which combines Merge Sort and Insertion Sort).
- **External Sorting (Sorting Data That Doesn’t Fit in Memory):**
  - Used when sorting huge files on hard disks, where the data is too large to fit in RAM.
  - Example: Merging sorted data in external storage.
- **Video & Image Processing (Merge Sort in Rendering):**
  - Used in computer graphics to sort objects for depth sorting in 3D rendering (Z-buffer algorithm).
- **E-Commerce & Transaction Processing:**
  - Used in Amazon, eBay, and stock trading platforms to sort millions of user transactions efficiently.
- **DNA Sequencing & Bioinformatics:**
  - Sorting huge DNA sequences efficiently in genome analysis.

---

## Project by:

- **Zyad Mohamed Mahmoud Alsaeed** - 202201548
- **Seham Nasr Ali Elmaghraby** - 202202722
- **Mariam Mohamed Bayoumi** - 202202682
- **Farah Mohamed Ghareeb** - 202203463
- **Amr Khaled Arab** - 202200997

