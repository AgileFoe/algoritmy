class LinkedList:
    def __init__(self):
        self.head = None

    def count_elements(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count