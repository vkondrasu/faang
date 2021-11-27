class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def delete(self, value):
        """ list is empty"""
        if self.head is None:
            return

        cur_node = self.head

        """ delte head"""
        if cur_node.data == value:
            self.head = cur_node.next
            return

        """ other than head be at previous node"""
        while cur_node.next:
            if cur_node.next.data == value:
                cur_node.next = cur_node.next.next
                return

            cur_node = cur_node.next



my_linked_list = LinkedList()
my_linked_list.append("python")
my_linked_list.append("LC - DC")
my_linked_list.append("The System Design")
my_linked_list.prepend("Priority - projects that matter")

my_linked_list.print_list()

my_linked_list.delete("The System Design")
my_linked_list.delete("Priority - projects that matter")

my_linked_list.print_list()
