#include <vector>
#include <iostream>
using namespace std;

// Bubble Sort (Iterative)
// Repeatedly swaps adjacent elements if they are in the wrong order
void bubble_sort_iterative(vector<int>& v, int n) // un-optimized
// space o(1)
// time best case = n^2 worst = n^2  // un-optimized
{
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if (v[j] > v[j+1]) 
                swap(v[j], v[j+1]);
        }
    }
}

// Bubble Sort (Recursive)
// Recursively pushes the largest element to the end in each pass
void _bubble_sort_recursive(vector<int>& v, int i)// optimized
// space o(1)
// time best case = n worst = n^2
{
    if (i == v.size() - 1)
        return;

    bool f = 0;

    if (v[i] > v[i + 1])
    {
        swap(v[i], v[i + 1]);
        f = 1;
    }

    if (f)
        _bubble_sort_recursive(v, 0);
    else
        _bubble_sort_recursive(v, i + 1);
}

void bubble_sort_recursive(vector<int>& v)
{
    _bubble_sort_recursive(v, 0);
}

// Insertion Sort (Recursive)
// Inserts each element in its correct position by shifting elements
void insert(vector<int>& v, int i)
{
    if (i == 0)
        return;

    if (v[i] < v[i - 1])
    {
        swap(v[i], v[i - 1]);
        insert(v, i - 1);
    }
}
// space = o(n) // for stack 
// time = worst = n^2 best = n
void _insertion_sort_recursive(vector<int>&v, int i)
{
    if (i == v.size())
        return;

    insert(v, i);
    _insertion_sort_recursive(v, i + 1);
}

void insertion_sort_recursive(vector<int>&v)
{
    _insertion_sort_recursive(v, 1);
}

// Insertion Sort (Iterative)
// Builds a sorted sequence one element at a time
void insertionSortIterative(vector<int>& v, int n)
// space = o(1) // in-place 
// time = worst = n^2 best = n
{
    for (int i = 1; i < n; i++)
    {
        int temp = v[i];
        int j = i - 1;
        while(temp < v[j] && j > -1)
        {
            v[j + 1] = v[j];
            --j;
        }
        v[j + 1] = temp;
    }
}

// Merge Sort (Iterative)
// Merges sorted subarrays iteratively
void merge(vector<int>& v, int left, int mid, int right)
// space o(n)
// time all is o(n log(n))
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> leftArr(n1), rightArr(n2);

    for (int i = 0; i < n1; i++) 
        leftArr[i] = v[left + i];
    
    for (int i = 0; i < n2; i++) 
        rightArr[i] = v[mid + 1 + i];
    
    int i = 0; 
    int j = 0;
    int k = left; 

    while (i < n1 && j < n2)
    {
        if (leftArr[i] <= rightArr[j]) 
            v[k++] = leftArr[i++];
        else 
            v[k++] = rightArr[j++];
    }

    while (i < n1) 
        v[k++] = leftArr[i++];
    
    while (j < n2) 
        v[k++] = rightArr[j++];
}

void merge_sort_iterative(vector<int>& v, int n)
// space o(n)
// time all is o(n log(n))
{
    for (int size = 1; size < n; size *= 2) // log (n)
    {
        for (int left = 0; left < n - size; left += 2 * size)
        {
            int mid = min(left + size - 1, n - 1);
            int right = min(left + 2 * size - 1, n - 1);
            merge(v, left, mid, right);
        }
    }
}

// Merge Sort (Recursive)
// Divides array into halves and merges them recursively
// time = n log n
// log n -> stack <- f calls 
// n -> heap
void _merge_sort_recursive(vector<int>&v, int l1, int r1, int l2, int r2)
{
    vector<int>L, R;
    int n1 = r1 - l1 + 1;
    int n2 = r2 - l2 + 1;

    for (int i = l1; i <= r1; i++)
        L.push_back(v[i]);

    for (int i = l2; i <= r2; i++)
        R.push_back(v[i]);

    int i = 0;
    int j = 0;
    int k = l1;

    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
            v[k++] = L[i++];
        else
            v[k++] = R[j++];
    }

    while (j < n2)
        v[k++] = R[j++];

    while (i < n1)
        v[k++] = L[i++];
}

void divide(vector<int>&v, int l, int r)
{
    if (l < r)
    {
        int l1 = l, r1 = (l + r) / 2;
        int l2 = r1 + 1, r2 = r;
        divide(v, l1, r1);
        divide(v, l2, r2);
        _merge_sort_recursive(v, l1, r1, l2, r2);
    }
}

void merge_sort_recursive(vector<int>& v)
{
    divide(v, 0, v.size() - 1);
}

// Example usage
int main()
{
    int n;
    cin >> n;
    vector<int> v(n);

    for (int i = 0; i < n; i++)
        cin >> v[i];
    
    // Choose which sorting algorithm to use
    // bubble_sort_iterative(v, n);       // Iterative bubble sort
    // bubble_sort_recursive(v);         // Recursive bubble sort
    // insertion_sort_recursive(v);      // Recursive insertion sort
    // merge_sort_iterative(v, n);        // Iterative merge sort
    merge_sort_recursive(v);           // Recursive merge sort

    // Output sorted array
    for (int i = 0; i < n; i++)
        cout << v[i] << " ";

    return 0;
}
