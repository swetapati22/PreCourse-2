"""
# Time Complexity :
- push: O(1)
- printMiddle: O(n)

# Space Complexity :
- O(1)

# Any problem you faced while coding this : No
"""

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
  
    def push(self, new_data): 
        # Create a new node and make it the new head
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("The list is empty.")
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("The middle element is:", slow.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
