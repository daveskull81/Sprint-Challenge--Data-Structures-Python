from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            oldest = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if oldest == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.current

        list_buffer_contents.append(current_node.value)

        if current_node.next is not None:
            working_node = current_node.next
        else:
            working_node = self.storage.head
        
        while working_node != current_node:
            list_buffer_contents.append(working_node.value)

            if working_node.next is not None:
                working_node = working_node.next
            else:
                working_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
