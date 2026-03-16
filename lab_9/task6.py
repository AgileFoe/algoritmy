class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False