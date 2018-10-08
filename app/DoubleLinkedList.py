class Item():
    def __init__(self, next_item, prev_item, elem):
        self.next_item = next_item
        self.prev_item = prev_item
        self.elem = elem


class DoubleLinkedList():
    def __init__(self):
        self.count = 0
        self.first_item = None
        self.last_item = None

    def push(self, elem):
        """add item to the end of list"""
        if self.count == 0:
            self.first_item = Item(None, None, elem)
            self.last_item = self.first_item
        else:
            new_item = Item(None, self.last_item, elem)
            self.last_item.next_item = new_item
            self.last_item = new_item
        self.count += 1

    def pop(self):
        """delete item from the end of list"""
        if self.count > 1:
            last_elem = self.last_item.elem
            self.last_item = self.last_item.prev_item
            self.last_item.next_item = None
        elif self.count == 1:
            last_elem = self.last_item.elem
            self.last_item = None
            self.firs_item = None
        else:
            return "list is empty"
        self.count -= 1
        return last_elem

    def unshift(self, elem):
        """add item to the top of list"""
        if self.count == 0:
            self.first_item = Item(None, None, elem)
            self.last_item = self.first_item
        else:
            new_item = Item(self.first_item, None, elem)
            self.first_item.prev_item = new_item
            self.first_item = new_item
        self.count += 1

    def shift(self):
        """delete item from the top of list"""
        if self.count > 1:
            first_elem = self.first_item.elem
            self.first_item = self.first_item.next_item
            self.first_item.prev_item = None
        elif self.count == 1:
            first_elem = self.first_item.elem
            self.last_item = None
            self.firs_item = None
        else:
            return "list is empty"
        self.count -= 1
        return first_elem

    def len(self):
        """count of items in list"""
        return self.count

    def first(self):
        """return first element in the list"""
        if self.count > 0:
            return self.first_item.elem
        else:
            return "list is empty"

    def last(self):
        """return last element in the list"""
        if self.count > 0:
            return self.last_item.elem
        else:
            return "list is empty"

    def delete(self, elem):
        """delete all elements equal to this"""
        item = self.first_item
        delete_elem_count = 0
        while item is not None:
            if item.elem == elem:
                if item.next_item is not None and item.prev_item is not None:
                    item.prev_item.next_item = item.next_item
                    item.next_item.prev_item = item.prev_item
                elif item.next_item is not None and item.prev_item is None:
                    item.next_item.prev_item = None
                    self.first_item = item.next_item
                elif item.next_item is None and item.prev_item is not None:
                    item.prev_item.next_item = None
                    self.last_item = item.prev_item
                else:
                    self.last_item = None
                    self.first_item = None
                delete_elem_count += 1
                self.count -= 1
            item = item.next_item
        if delete_elem_count == 0:
            return "no such element"

    def show(self):
        """return list of elements"""
        if self.count == 0:
            return "list is empty"
        item = self.first_item
        elements = list()
        while item is not None:
            elements.append(item.elem)
            item = item.next_item
        return elements

    def contains(self, elem):
        """return the number of occurences of an item in the list"""
        count = 0
        current_item = self.first_item
        while current_item is not None:
            if current_item.elem == elem:
                count += 1
            current_item = current_item.next_item
        return count
