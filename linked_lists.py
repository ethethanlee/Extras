class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

l1 = SLinkedList()
l1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
l1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

l2 = SLinkedList()
l2.headval = Node(1)
a2 = Node(2)
a3 = Node(3)
# Link first Node to second node
l2.headval.nextval = a2

# Link second Node to third node
a2.nextval = a3

l2.listprint()