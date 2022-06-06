class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None

   def Atbegining(self, data_in):
      NewNode = Node(data_in)
      NewNode.next = self.head
      self.head = NewNode

# Function to remove node
   def RemoveNode(self, Removekey):
      HeadVal = self.head
         
      if (HeadVal is not None):
         if (HeadVal.data == Removekey):
            self.head = HeadVal.next
            HeadVal = None
            return
      while (HeadVal is not None):
         if HeadVal.data == Removekey:
            break
         prev = HeadVal
         HeadVal = HeadVal.next

      if (HeadVal == None):
         return

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
l1 = SLinkedList()
l1.headval = Node(2)
e2 = Node(4)
e3 = Node(3)
l1.headval.nextval = e2
e2.nextval = e3
l2 = SLinkedList()
l2.headval = Node(5)
a2 = Node(6)
a3 = Node(4)
l2.headval.nextval = a2
a2.nextval = a3
l1.listprint()

# result = l2.dataval  
# print(result)
# l2 = l2.nextval 
l2.listprint()