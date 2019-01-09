"""
Module implementing singly linked list.
"""


class Node:
    """
    Description: Class for a node.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    Description: Class for the linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def set_tail(self):
        """
        Description: Method to set the tail.
        """
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp

    def length(self):
        """
        Description: Method to calculate length of linked list.
                     Starting index = 0
        """
        temp = self.head
        count = -1
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def insert_at_beginning(self, data):
        """
        Description: Method to insert a node at beginning.
        """
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insert_at_end(self, data):
        """
        Description: Method to insert a node at end.
        """
        temp = Node(data)
        self.tail.next = temp
        self.tail = temp

    def insert_at_any_index(self, data, index):
        """
        Description: function appends a node at given index.
        """
        length_of_list = self.length()
        if index == 0:
            self.insert_at_beginning(data)
        elif index == length_of_list:
            self.insert_at_end(data)
        elif 1 <= index <= length_of_list:
            temp = self.head
            count = 0
            while count is not index-1:
                temp = temp.next
                count = count + 1
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    def pop_head(self):
        """
        Description: Method to pop a head.
        """
        self.head = self.head.next

    def pop_at_end(self):
        """
        Description: Method to pop the last node.
        """
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = temp
        self.tail.next = None

    def pop_at_any_index(self, index):
        """
        Description: function pops a node at given index.
        """
        length_of_list = self.length()
        if index == 0:
            self.pop_head()
        elif index == length_of_list - 1:
            self.pop_at_end()
        elif 1 <= index <= length_of_list - 1:
            temp = self.head
            count = 0
            while count is not index - 1:
                count = count + 1
                temp = temp.next
            temp.next = temp.next.next

    def print(self):
        """
        Description: Method to print the linked list.
        """
        temp = self.head
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next
        print("NONE   TAIL: " + str(self.tail.data))

    def print_reverse(self):
        """
        Description: Method to print the linked list in reverse.
        """
        temp = self.head
        list_of_nodes = []
        while temp is not None:
            list_of_nodes.append(temp.data)
            temp = temp.next
        print(*list_of_nodes[::-1], sep='->', end='->')
        print("NONE   TAIL: " + str(self.tail.data))

    def print_middle_single_traversal(self):
        """
        Description: Method to print middle of the linked list in a single
        traversal.
        """
        slow = self.head
        fast = self.head

        while fast.next is not None and fast is not None:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)


def main():
    ll = LinkedList()
    for i in range(5, 0, -1):
        ll.insert_at_beginning(i)
    ll.set_tail()
    print("linked list:", end="  ")
    ll.print()

    ll.insert_at_beginning(0)
    print("insert '0' begining of linked list:", end="  ")
    ll.print()

    ll.pop_head()
    print("pop the head of the list:", end="  ")
    ll.print()

    ll.insert_at_end(6)
    print("insert 6 at the end:", end="  ")
    ll.print()

    ll.pop_at_end()
    print("pop the last element:", end="  ")
    ll.print()

    ll.insert_at_any_index(9, 2)
    print("insert the element at the position 2 starting from 0:", end="  ")
    ll.print()

    ll.pop_at_any_index(2)
    print("pop at 2nd index starting from 0:", end="  ")
    ll.print()

    print("print the middle element in single traversal:", end="  ")
    ll.print_middle_single_traversal()


if __name__ == '__main__':
    main()
