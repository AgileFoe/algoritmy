class Node:
    def __init__(self, data):
        self.data = data  # Данные
        self.next = None  # Ссылка на следующий узел


class LinkedList:
    def __init__(self):
        self.head = None  # Начальный элемент пустой

    # Добавление элемента в начало списка
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Добавление элемента в конец списка
    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Вывод всех элементов списка
    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("Список пуст.")
        while current_node:
            print(current_node.data, end="->" if current_node.next else None)
            current_node = current_node.next
        print()

    # Поиск элемента в списке
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    # Удаление первого элемента списка
    def remove_first(self):
        if self.head:
            self.head = self.head.next

    # Подсчёт количества элементов в списке
    def count_elements(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # Разворот связного списка
    def reverse(self):
        prev = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev

# Тестирование всех функций

# 1. Создаём связный список
ll = LinkedList()

# 2. Добавляем элементы в начало
ll_input = LinkedList()
for _ in range(5):
    num = int(input("Введите число: "))  # Считываем 5 чисел
    ll_input.add_last(num)  # Добавляем их в список
print("Список из введённых чисел:")
ll_input.print_list()

ll.add_first(10)  # Список: 10
ll.add_first(20)  # Список: 20 → 10
ll.add_first(30)  # Список: 30 → 20 → 10

# 3. Выводим элементы списка
print("Список после добавления элементов в начало:")
ll.print_list()  # Ожидаемый вывод: 30 20 10

# 4. Добавляем элементы в конец
ll.add_last(40)  # Список: 30 → 20 → 10 → 40
ll.add_last(50)  # Список: 30 → 20 → 10 → 40 → 50

# 5. Выводим элементы списка после добавления в конец
print("Список после добавления элементов в конец:")
ll.print_list()  # Ожидаемый вывод: 30 20 10 40 50

# 6. Ищем элемент в списке
print("Поиск элемента 20:", ll.search(20))  # Ожидаемый вывод: True
print("Поиск элемента 60:", ll.search(60))  # Ожидаемый вывод: False

# 7. Удаляем первый элемент
ll.remove_first()  # Список после удаления первого элемента: 20 → 10 → 40 → 50

# 8. Выводим элементы списка после удаления первого
print("Список после удаления первого элемента:")
ll.print_list()  # Ожидаемый вывод: 20 10 40 50

# 9. Подсчёт количества элементов
print("Количество элементов в списке:", ll.count_elements())  # Ожидаемый вывод: 4

# 10. Разворачиваем список
ll.reverse()  # Список после разворота: 50 → 40 → 10 → 20

# 11. Выводим элементы списка после разворота
print("Список после разворота:")
ll.print_list()  # Ожидаемый вывод: 50 40 10 20

# 12. Программа для ввода чисел и добавления их в список
ll_input = LinkedList()
for _ in range(5):
    num = int(input("Введите число: "))  # Считываем 5 чисел
    ll_input.add_last(num)  # Добавляем их в список
print("Список из введённых чисел:")
ll_input.print_list()


