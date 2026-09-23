# 146. LRU Cache
# Difficulty: Medium
# Topics: Hash Table, Linked List, Design, Doubly-Linked List
# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # dummy left/right nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    # helper to insert most recently used at end of doubly-linked list
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
    
    # helper to remove least recently used at start of doubly-linked list
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove stale entry
            self.remove(self.cache[key])
        
        # now add the key-value pair to cache
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # check if over capacity
        if len(self.cache) > self.capacity:
            least_recently_used = self.left.next
            self.remove(least_recently_used)
            del self.cache[least_recently_used.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)