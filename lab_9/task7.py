class LinkedList:
    def __init__(self):
        self.head = None

    def remove_first(self):
        if self.head:
            self.head = self.head.next