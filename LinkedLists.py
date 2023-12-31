class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes 0(n) time
        """
        current = self.head
        count = 0 

        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        """
        Adds a new node containing data at the head of
        It tackes O(n) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or None if not found

        Takes 0(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes 0(1) time but finding the node at the
        insertion point takes 0(n)

        Takes overall 0(n) time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = self.node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Remove Node containing data that matches the key
        Returns the node or None if the key doesnt exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1     
        return current

    def __repr__(self) -> str:
        """
        Returns a string representation of the list
        Taes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return ' '.join(nodes)

        # TODO
        ## Remove at index
        ## Add at index

l = LinkedList()
l.add(1)
l.add(10)
l.add(14)
l.add(13)
l.add(12)
l.remove(10)
print(l)
print(l.search(13))