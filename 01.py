class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, key: int, data):
        if self.head is None:
            print("Список порожній.")
            return
        if self.head.data == key:
            self.insert_at_beginning(data)
            return
        prev = None
        current = self.head
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Елемент не знайдено.")
            return
        new_node = Node(data)
        new_node.next = current
        prev.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, head=None):
        if head is None:
            head = self.head

        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        self.head = self.merge_sorted_lists(left, right)
        
        return self.head

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sorted_lists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.data <= l2.data:
            result = l1
            result.next = self.merge_sorted_lists(l1.next, l2)
        else:
            result = l2
            result.next = self.merge_sorted_lists(l1, l2.next)

        return result

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)


# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Before reversing:")
llist.print_list()

print("\nAfter reversing:")
llist.reverse()
llist.print_list()

print("\nBefore sorting:")
llist.print_list()

llist.merge_sort()

print("\nAfter sorting:")
llist.print_list()
