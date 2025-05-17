"""
# Time Complexity :
- Best, Average, Worst: O(n log n)

# Space Complexity :
- O(n) due to auxiliary arrays used during merging

# Any problem you faced while coding this : No
"""

# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        L = arr[:mid]        # Dividing the array elements
        R = arr[mid:]

        mergeSort(L)         # Sorting the first half
        mergeSort(R)         # Sorting the second half

        # Merging the two halves
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking for remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
# Code to print the list 
def printList(arr): 
    #write your code here
    for i in range(len(arr)):         
        print(arr[i], end=" ") 
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
