class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.pointer = self.first

    def __str__(self):
        if self.first is not None:
            current = self.first
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'LinkedList [{", ".join(values)}]'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        self.first = None
        self.last = None

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        current_node = self.first
        cur_idx = 0
        while cur_idx < index - 1:
            current_node = current_node.next
            cur_idx += 1
        prev_next = current_node.next
        current_node.next = Node(value, prev_next)

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        current_node = self.first
        index = 0
        while current_node and current_node.value != value:
            current_node = current_node.next
            index += 1
        if not current_node:
            return '???'
        return index

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first

    def __iter__(self):
        self.pointer = self.first
        while self.pointer != self.last:
            yield self.pointer.value
            self.__next__()
        yield self.last.value

    def __next__(self):
        next_node = self.pointer.next
        self.pointer = self.pointer.next
        return next_node.value


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list = ", L)

    L.insert('5656', 2)
    print("list = ", L)

    L.insert('54656', 3)
    print("list = ", L)

    print(L.find(2))
    print(L.find(22))

    print(L)

    # TODO: реализовать интерфейс итерации
    for el in L:
        print(el)
    # Напомню принцип работы итератора:
    iterator_L = iter(L)  # L.__iter__()
    print(next(iterator_L))  # it.__next__()
    print(next(iterator_L))
    print(next(iterator_L))
    print(next(iterator_L))
    print(next(iterator_L))

    # TODO: реализовать обращение по индексу и изменение значение по индексу
    # print(L[0])
    # L[0] = "new"
    # print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    # L = LinkedList(2, 4, 6, -12)
    # print(L)
