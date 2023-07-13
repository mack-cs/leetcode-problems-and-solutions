"""
Design HashMap
Easy
4.2K
374
Companies
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000  # Size of the array
        self.buckets = [None] * self.size  # Initialize the array with None

    def put(self, key, value):
        index = self._hash(key)  # Hash the key to get the index in the array
        if not self.buckets[index]:  # If the bucket is empty
            self.buckets[index] = ListNode(key, value)  # Create a new node and assign it to the bucket
        else:
            curr = self.buckets[index]  # Get the first node in the bucket
            while True:
                if curr.key == key:  # If the key already exists in the bucket, update the value
                    curr.value = value
                    return
                if not curr.next:  # If we reached the end of the linked list
                    break
                curr = curr.next  # Move to the next node
            curr.next = ListNode(key, value)  # Add a new node to the end of the linked list

    def get(self, key):
        index = self._hash(key)  # Hash the key to get the index in the array
        curr = self.buckets[index]  # Get the first node in the bucket
        while curr:
            if curr.key == key:  # If the key is found in the linked list
                return curr.value
            curr = curr.next  # Move to the next node
        return -1  # The key was not found in the bucket

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

    def _hash(self, key):
        return key % self.size  # Hash function: modulo operator to get the index in the array
