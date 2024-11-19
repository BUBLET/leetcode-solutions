class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        new = ListNode(-1)  # Начальный фиктивный узел
        current = new       # Указатель на текущую позицию в новом списке

        # Шаг 2: Пока оба списка не пусты
        while list1 and list2:
            if list1.val <= list2.val:  # Если текущий узел list1 меньше или равен узлу list2
                current.next = list1    # Добавляем узел из list1 в новый список
                list1 = list1.next      # Переходим к следующему узлу list1
            else:                       # Иначе берем узел из list2
                current.next = list2
                list2 = list2.next
            current = current.next      # Переходим к следующему узлу в новом списке

        # Шаг 3: Добавляем оставшиеся узлы из list1 или list2
        current.next = list1 if list1 else list2

        # Шаг 4: Возвращаем голову нового списка (без фиктивного узла)
        return new.next 