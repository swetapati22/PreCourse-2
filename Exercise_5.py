"""
# Time Complexity :
- Best & Average Case: O(n log n)
- Worst Case: O(n^2) — when partitioning is unbalanced

# Space Complexity :
- O(log n) in best case, O(n) in worst case due to stack

# Any problem you faced while coding this : No
"""

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  # Create an auxiliary stack
    stack = []

    # Push initial values of l and h
    stack.append((l, h))

    # Keep popping while stack is not empty
    while stack:
        # Pop h and l
        l, h = stack.pop()

        # Set pivot element at its correct position
        p = partition(arr, l, h)

        # If elements on left of pivot, push left side to stack
        if p - 1 > l:
            stack.append((l, p - 1))

        # If elements on right of pivot, push right side to stack
        if p + 1 < h:
            stack.append((p + 1, h))

# Driver code to test
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    for i in arr:
      print(i, end=" ")
    print()

