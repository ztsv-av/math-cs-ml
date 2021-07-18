class Node:
   def __init__(self, initial_data):
      self.data = initial_data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def append(self, new_node):
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      else:
         self.tail.next = new_node
         self.tail = new_node

   def prepend(self, new_node):
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      else:
         new_node.next = self.head
         self.head = new_node

   def insert_after(self, current_node, new_node):
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      elif current_node is self.tail:
         self.tail.next = new_node
         self.tail = new_node
      else:
         new_node.next = current_node.next
         current_node.next = new_node
   
   def remove_after(self, current_node):
     # Special case, remove head
     if (current_node == None) and (self.head != None):
        succeeding_node = self.head.next
        self.head = succeeding_node  
        if succeeding_node == None:    # Removed last item
           self.tail = None
     elif current_node.next != None:
        succeeding_node = current_node.next.next
        current_node.next = succeeding_node
        if succeeding_node == None:    # Removed tail
           self.tail = current_node


class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)
    
    def pop(self):
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the popped item
        return popped_item

class Queue:
    def __init__(self):
        self.list = LinkedList()
        
    def enqueue(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert as list tail (end of queue)
        self.list.append(new_node)
    
    def dequeue(self):
        # Copy data from list's head node (queue's front node)
        dequeued_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the dequeued item
        return dequeued_item
