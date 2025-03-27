class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        Возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            return None  # Стек пуст
        val = self.end.data  # Сохраняем значение для возврата
        self.end = self.end.pref  # Перемещаем указатель на предыдущий узел
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)  # Создаем новый узел
        new_node.pref = self.end  # Указываем на предыдущий узел
        self.end = new_node  # Обновляем конец стека

    def print(self):
        """
        Вывод на печать содержимого стека
        """
        current = self.end
        while current is not None:
            print(current.data)
            current = current.pref

# Пример использования стека
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()  # Вывод: 3, 2, 1
    print("Pop:", stack.pop())  # Вывод: Pop: 3
    stack.print()  # Вывод: 2, 1