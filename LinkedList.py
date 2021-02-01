import sys

sys.setrecursionlimit(5000)

class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    headtrck = None
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtStart(self, data):
        if self.head == None:
            node = Node(data, next = self.head)
            self.head = node
            self.tail = node
            self.headtrck = node
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node
            self.headtrck = node

    def insertAtEnd(self, data):
        if self.head == None:
            node = Node(data,prev = self.tail)
            self.head = node
            self.tail = node
            self.headtrck = node
            return
        node = Node(data,prev = self.tail)
        self.tail.next = node
        self.tail = node



    def printLR(self, rev = False):
        if self.head == None:
            print("List Empty#")
            return
        llstr = ''
        itr = self.head
        while itr:
            if rev == False:
                arrow = "-->"
            else:
                arrow = "<--"
            if itr.next != None:
                llstr += str(itr.data) + arrow
            else: llstr += str(itr.data)
            itr = itr.next
        print(llstr)

    def printRL(self, rev = False):
        if self.tail == None:
            print("List Empty!")
            return
        llstr = ''
        itr = self.tail
        while itr:
            if rev ==False:
                arrow = "-->"
            else:
                arrow = "<--"
            if itr.prev != None:
                llstr += str(itr.data) + arrow
            else: llstr += str(itr.data)
            itr = itr.prev
        print(llstr)

    def updateVal(self,nodeval, newval):
        if self.head == None:
            print("List is empty")
            return
        itr = self.head
        while itr:
            if itr.data == nodeval:
                itr.data = newval
                print("Value updated")
                return
            itr = itr.next
        print("Entered node cannot be found")
        return

    def findVal(self,val):
        if self.head == None:
            print("List empty")
            return False
        itr = self.head
        while itr:
            if itr.data == val:
                print("Element found")
                return True
            itr = itr.next
        print("Element not found")
        return False

    def deleteItem(self,val):
        if self.head == None:
            print("Empty List")
            return False
        itr = self.head
        while itr:
            if itr.data == val:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    del itr
                    print("Deleted")
                    return True
                elif itr.prev == None:
                    self.head = itr.next
                    rightEle = itr.next
                    rightEle.prev = None
                    del itr
                    print("Deleted")
                    return True
                elif itr.next == None:
                    leftEle = itr.prev
                    leftEle.next = None
                    self.tail = itr.prev
                    del itr
                    print("Deleted")
                    return True
                else:
                    leftEle = itr.prev
                    rightEle = itr.next
                    leftEle.next= rightEle
                    rightEle.prev = leftEle
                    print("Deleted")
                    del itr
                    return True
            else: itr = itr.next
        print("Element not found")
        return False

    def printValues(self, direction = True,reverse = False):
        if direction:
            self.printLR(reverse)
        else:
            self.printRL(reverse)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(9)
    ll.insertAtEnd(11)
    ll.insertAtEnd(12)
    ll.printLR()
    #ll.printRL(rev = False) # Print from Right to Left

    ll.findVal(12)
    ll.updateVal(14,14)
    ll.printValues(reverse=True)