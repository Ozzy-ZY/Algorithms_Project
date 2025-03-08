#include <iostream>
#include <vector>
using namespace std;
class Sorting {
private:
    static void merge(vector<int>& arr, int leftStart, int leftEnd, int rightStart, int rightEnd) {
        vector<int> leftSubarray, rightSubarray;
        
        // Copy elements to temporary arrays
        for (int i = leftStart; i <= leftEnd; i++) {
            leftSubarray.push_back(arr[i]);
        }
        
        for (int i = rightStart; i <= rightEnd; i++) {
            rightSubarray.push_back(arr[i]);
        }
        
        // Merge the temporary arrays back
        int leftIndex = 0;
        int rightIndex = 0;
        int mergeIndex = leftStart;
        
        // Compare and merge elements from both subarrays
        while (leftIndex < leftSubarray.size() && rightIndex < rightSubarray.size()) {
            if (leftSubarray[leftIndex] <= rightSubarray[rightIndex]) {
                arr[mergeIndex++] = leftSubarray[leftIndex++];
            } else {
                arr[mergeIndex++] = rightSubarray[rightIndex++];
            }
        }
        
        // Copy remaining elements from right subarray if any
        while (rightIndex < rightSubarray.size()) {
            arr[mergeIndex++] = rightSubarray[rightIndex++];
        }
        
        // Copy remaining elements from left subarray if any
        while (leftIndex < leftSubarray.size()) {
            arr[mergeIndex++] = leftSubarray[leftIndex++];
        }
    }
    
    static void mergeSortRecursive(vector<int>& arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            
            // Sort first and second halves
            mergeSortRecursive(arr, left, mid);
            mergeSortRecursive(arr, mid + 1, right);
            
            // Merge the sorted halves
            merge(arr, left, mid, mid + 1, right);
        }
    }
    
    static void insertElement(vector<int>& arr, int index) {
        if (index == 0) {
            return;
        }
        
        if (arr[index] < arr[index - 1]) {
            swap(arr[index], arr[index - 1]);
            insertElement(arr, index - 1);
        }
    }
    
    static void insertionSortRecursive(vector<int>& arr, int index) {
        if (index == arr.size()) {
            return;
        }
        
        insertElement(arr, index);
        insertionSortRecursive(arr, index + 1);
    }
    
    // Recursive function for bubble sort
    static void bubbleSortRecursive(vector<int>& arr, int index) {
        if (index == arr.size() - 1) {
            return;
        }
        
        bool swapped = false;
        if (arr[index] > arr[index + 1]) {
            swap(arr[index], arr[index + 1]);
            swapped = true;
        }
        
        if (swapped) {
            bubbleSortRecursive(arr, 0);
        } else {
            bubbleSortRecursive(arr, index + 1);
        }
    }
    
public:
    static void mergeSort(vector<int>& arr) {
        mergeSortRecursive(arr, 0, arr.size() - 1);
    }
    
    static void insertionSort(vector<int>& arr) {
        insertionSortRecursive(arr, 1);
    }
    
    static void bubbleSort(vector<int>& arr) {
        bubbleSortRecursive(arr, 0);
    }
};

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    
    vector<int> arr(n);
    cout << "Enter " << n << " integers: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int choice;
    cout << "\nChoose a sorting algorithm:\n";
    cout << "1. Merge Sort\n";
    cout << "2. Insertion Sort\n";
    cout << "3. Bubble Sort\n";
    cout << "Enter your choice (1-3): ";
    cin >> choice;
    
    switch (choice) {
        case 1:
            cout << "Applying Merge Sort...\n";
            Sorting::mergeSort(arr);
            break;
        case 2:
            cout << "Applying Insertion Sort...\n";
            Sorting::insertionSort(arr);
            break;
        case 3:
            cout << "Applying Bubble Sort...\n";
            Sorting::bubbleSort(arr);
            break;
        default:
            cout << "Invalid choice! Using Merge Sort by default...\n";
            Sorting::mergeSort(arr);
    }
    
    cout << "Sorted array: ";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}