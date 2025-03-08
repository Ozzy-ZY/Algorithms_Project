#include <iostream>
#include <vector>
using namespace std;

class SortingIterative {
private:

    static void merge(vector<int>& array, int leftIndex, int midIndex, int rightIndex)
    {
        int leftSubarraySize = midIndex - leftIndex + 1;
        int rightSubarraySize = rightIndex - midIndex;

        vector<int> leftSubarray(leftSubarraySize), rightSubarray(rightSubarraySize);

        for (int i = 0; i < leftSubarraySize; i++) 
            leftSubarray[i] = array[leftIndex + i];
        
        for (int i = 0; i < rightSubarraySize; i++) 
            rightSubarray[i] = array[midIndex + 1 + i];
        
        int leftPos = 0; 
        int rightPos = 0;
        int mergePos = leftIndex; 

        while (leftPos < leftSubarraySize && rightPos < rightSubarraySize)
        {
            if (leftSubarray[leftPos] <= rightSubarray[rightPos]) 
                array[mergePos++] = leftSubarray[leftPos++];
            else 
                array[mergePos++] = rightSubarray[rightPos++];
        }

        while (leftPos < leftSubarraySize) 
            array[mergePos++] = leftSubarray[leftPos++];
        
        while (rightPos < rightSubarraySize) 
            array[mergePos++] = rightSubarray[rightPos++];
    }

public:
    static void insertionSort(vector<int>& array)
    {
        int arraySize = array.size();
        for (int currentPos = 1; currentPos < arraySize; currentPos++)
        {
            int currentElement = array[currentPos];
            
            int prevPos = currentPos - 1;
            while(prevPos >= 0 && currentElement < array[prevPos])
            {
                array[prevPos + 1] = array[prevPos];
                --prevPos;
            }
            
            array[prevPos + 1] = currentElement;
        }
    }

    static void bubbleSort(vector<int>& array)
    {
        int arraySize = array.size();
        for (int pass = 0; pass < arraySize-1; pass++)
        {
            for (int compareIndex = 0; compareIndex < arraySize-pass-1; compareIndex++)
            {
                if (array[compareIndex] > array[compareIndex+1]) 
                    swap(array[compareIndex], array[compareIndex+1]);
            }
        }
    }

    static void mergeSort(vector<int>& array)
    {
        int arraySize = array.size();
        for (int subarraySize = 1; subarraySize < arraySize; subarraySize *= 2)
            for (int leftStart = 0; leftStart < arraySize - subarraySize; leftStart += 2 * subarraySize)
            {
                int midPoint = min(leftStart + subarraySize - 1, arraySize - 1);
                int rightEnd = min(leftStart + 2 * subarraySize - 1, arraySize - 1);

                merge(array, leftStart, midPoint, rightEnd);
            }
    }
};
class SortingRecursive {
private:
    static void merge(vector<int>& arr, int leftStart, int leftEnd, int rightStart, int rightEnd) {
        vector<int> leftSubarray, rightSubarray;
        
        for (int i = leftStart; i <= leftEnd; i++) {
            leftSubarray.push_back(arr[i]);
        }
        
        for (int i = rightStart; i <= rightEnd; i++) {
            rightSubarray.push_back(arr[i]);
        }
        
        int leftIndex = 0;
        int rightIndex = 0;
        int mergeIndex = leftStart;
        
        while (leftIndex < leftSubarray.size() && rightIndex < rightSubarray.size()) {
            if (leftSubarray[leftIndex] <= rightSubarray[rightIndex]) {
                arr[mergeIndex++] = leftSubarray[leftIndex++];
            } else {
                arr[mergeIndex++] = rightSubarray[rightIndex++];
            }
        }
        
        while (rightIndex < rightSubarray.size()) {
            arr[mergeIndex++] = rightSubarray[rightIndex++];
        }
        
        while (leftIndex < leftSubarray.size()) {
            arr[mergeIndex++] = leftSubarray[leftIndex++];
        }
    }
    
    static void mergeSortRecursive(vector<int>& arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSortRecursive(arr, left, mid);
            mergeSortRecursive(arr, mid + 1, right);
    
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
            //SortingRecursive::mergeSort(arr);
            SortingIterative::mergeSort(arr);
            break;
        case 2:
            cout << "Applying Insertion Sort...\n";
            //SortingRecursive::insertionSort(arr);
            SortingIterative::insertionSort(arr);
            break;
        case 3:
            cout << "Applying Bubble Sort...\n";
            //SortingRecursive::bubbleSort(arr);
            SortingIterative::bubbleSort(arr);
            break;
        default:
            cout << "Invalid choice! Using Merge Sort by default...\n";
            //SortingRecursive::mergeSort(arr);
            SortingIterative::mergeSort(arr);
    }
    
    cout << "Sorted array: ";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}