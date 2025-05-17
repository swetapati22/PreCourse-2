"""
# Time Complexity :
- Best case: O(1)
- Average and Worst case: O(log n)

# Space Complexity :
- O(1), as it's iterative

# Any problem you faced while coding this : No
"""

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):   
  #write your code here
    while l <= r:
        mid = l + (r - l) // 2  # avoid overflow (not critical in Python, but good habit)
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1  # not found
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")
