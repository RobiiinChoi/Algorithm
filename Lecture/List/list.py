class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.node = None
        self.datas = 0

    def __len__(self):
        return self.datas

    def __str__(self):
        node = self.head
        node = node.next
        s = ''

        for i in range(self.datas):
            s += f'{node.data}, '
            node = node.next

        return f'[{s[:-2]}]'

    def __iter__(self):
        node = self.head
        node = node.next

        while node:
            yield node.data
            node = node.next

    def insert(self, input_index, input_data):
        node = self.head

        for i in range(input_index):
            node = node.next

        new_node = Node(input_data)
        new_node.next = node.next
        node.next = new_node

        self.datas += 1

    def append(self, data):
        newnode = Node(data)
        self.tail.next = newnode
        self.tail = newnode
        self.datas += 1

    def pop(self):
        end_node = self.tail.data
        node = self.head

        for i in range(self.datas):
            if node.next is self.tail:
                self.tail = node
                break
            node = node.next

        self.datas -= 1
        return end_node

    def find(self, data):
        index = -1
        node = self.head

        for i in range(self.datas+1):
            if node.data == data:
                return index
            index += 1
            node = node.next

        return -1