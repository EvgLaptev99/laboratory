class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел

class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None  # Очередь пуста
        val = self.start.data  # Сохраняем значение для возврата
        self.start = self.start.nref  # Перемещаем указатель на следующий узел
        if self.start is not None:
            self.start.pref = None  # Обновляем ссылку на предыдущий узел
        else:
            self.end = None  # Если очередь пуста, обновляем конец
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)  # Создаем новый узел
        if self.end is None:  # Если очередь пуста
            self.start = new_node  # Начало указывает на новый узел
            self.end = new_node  # Конец указывает на новый узел
        else:
            self.end.nref = new_node  # Указываем на новый узел
            new_node.pref = self.end  # Указываем на предыдущий узел
            self.end = new_node  # Обновляем конец очереди

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        if n == 0:  # Вставка в начало
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:  # Если очередь была пуста
                self.end = new_node
            return

        current = self.start
        for _ in range(n - 1):
            if current is None:
                return  # Если n больше длины очереди
            current = current.nref

        if current is None:  # Вставка в конец
            self.end.nref = new_node