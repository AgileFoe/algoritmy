# 1
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


# 2
def most_frequent(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)


# 3
def two_sum(arr, target):
    seen = {}
    for num in arr:
        comp = target - num
        if comp in seen:
            return comp, num
        seen[num] = True
    return None


# 4
def sort_by_length(strings):
    return sorted(strings, key=len)


# 5
def top_3_words(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:3]


# 6
def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# 7
def intersection(a, b):
    return list(set(a) & set(b))


# 8
def best_student(students):
    return max(students, key=lambda x: x[1])


# 9 
def split_even_odd(arr):
    even = []
    odd = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd


# 10
def longest_sequence(arr):
    if not arr:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1

    return max(max_len, current_len)


# 11
class UserSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, name, age):
        self.users[name] = age

    def remove_user(self, name):
        if name in self.users:
            del self.users[name]

    def find_user(self, name):
        return self.users.get(name, "Пользователь не найден")

    def show_all(self):
        return self.users


# Пример использования
if __name__ == "__main__":

    print("Задача 1:", find_duplicates([1, 2, 2, 3, 4, 4]))
    print("Задача 2:", most_frequent([1, 2, 2, 3, 3, 3]))
    print("Задача 3:", two_sum([2, 7, 11, 15], 9))
    print("Задача 4:", sort_by_length(["apple", "hi", "banana"]))
    print("Задача 5:", top_3_words("hi hi hello world world world"))
    print("Задача 6:", remove_duplicates([1, 1, 2, 3, 3]))
    print("Задача 7:", intersection([1, 2, 3], [2, 3, 4]))
    print("Задача 8:", best_student([("Anna", 90), ("Ivan", 85)]))
    print("Задача 9:", split_even_odd([1, 2, 3, 4, 5]))
    print("Задача 10:", longest_sequence([1, 1, 2, 2, 2, 3]))

    system = UserSystem()
    system.add_user("Alex", 20)
    system.add_user("Mira", 22)
    print("Задача 11:", system.show_all())