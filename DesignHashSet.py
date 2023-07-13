"""
Design HashSet
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. 
If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 
"""
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

### Solution Commented
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.size = 1000  # Size of the array
        self.buckets = [None] * self.size  # Initialize the array with None

    def add(self, key):
        index = self._hash(key)  # Hash the key to get the index in the array
        if not self.buckets[index]:  # If the bucket is empty
            self.buckets[index] = ListNode(key)  # Create a new node and assign it to the bucket
        else:
            curr = self.buckets[index]  # Get the first node in the bucket
            while True:
                if curr.key == key:  # If the key already exists in the bucket, do nothing
                    return
                if not curr.next:  # If we reached the end of the linked list
                    break
                curr = curr.next  # Move to the next node
            curr.next = ListNode(key)  # Add a new node to the end of the linked list

    def remove(self, key):
        index = self._hash(key)  # Hash the key to get the index in the array
        curr = prev = self.buckets[index]  # Get the first node in the bucket
        if not curr:  # If the bucket is empty, the key doesn't exist
            return
        if curr.key == key:  # If the key is found at the first node
            self.buckets[index] = curr.next  # Remove the first node from the bucket
        else:
            curr = curr.next  # Move to the next node
            while curr:
                if curr.key == key:  # If the key is found in the linked list
                    prev.next = curr.next  # Remove the current node from the linked list
                    return
                curr, prev = curr.next, prev.next  # Move to the next node in the linked list

    def contains(self, key):
        index = self._hash(key)  # Hash the key to get the index in the array
        curr = self.buckets[index]  # Get the first node in the bucket
        while curr:
            if curr.key == key:  # If the key is found in the linked list
                return True
            curr = curr.next  # Move to the next node
        return False  # The key was not found in the bucket

    def _hash(self, key):
        return key % self.size  # Hash function: modulo operator to get the index in the array
