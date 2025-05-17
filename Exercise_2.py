"""
# Time Complexity :
- Best & Average Case: O(n log n)
- Worst Case: O(n^2) — occurs when pivot divides poorly (Already sorted array with last element as pivot)

# Space Complexity :
- O(log n) due to recursion stack (O(n) in worst case)

# Any problem you faced while coding this : No
"""

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1  # pointer for greater element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        # Partition the array and get pivot index
        pi = partition(arr, low, high)

        # Sort elements before and after partition recursively
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
