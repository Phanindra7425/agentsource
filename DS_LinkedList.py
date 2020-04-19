#Linked List -- Sequence of data elements which are connected via links.
#Each data element contains a connection to another data element in form of a pointer
#Python doesnot have linked list in the Standarad library,but can be implemented with concepts of nodes
#Nodes are similar to pointers

#Creatiion of nodes
#
# class daynames:
#     def __init__(self,dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#
#
# e1 = daynames('Mon')
# e2 = daynames('Tue')
# e3 = daynames('Wed')
# e1.nextval = e2
# e2.nextval = e3
# print(e1.dataval,e1.nextval.dataval)


class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    #Travesring a linkedlist
    def printinglinkedlist(self):
        value = self.head;
        while value is not None:
            print(value.data)
            value = value.next

    #Insertion in linked list
    def insertionatbegininglinkedlist(self,value):
        Newnode = Node(value)
        Newnode.next = self.head
        self.head = Newnode

    def insertionatlastlinkedlist(self,value):
        Newmode = Node(value)
        if self.head is None:
            self.head = Newmode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = Newmode

list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.head.next=e2
e2.next = e3
list1.insertionatbegininglinkedlist("sun")
list1.insertionatlastlinkedlist("thurs")
print(list1.printinglinkedlist())
print(list1.head.data,list1.head.next.data,list1.head.next.next.data)














