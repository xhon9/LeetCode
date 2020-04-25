# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.seen = {}

    def get(self, key):
        if not key in self.cache: return -1
        self.cache.pop(self.cache.index(key))
        self.cache.append(key)
        return self.seen[key]

    def put(self, key, value):
        if key in self.cache: self.cache.pop(self.cache.index(key))
        elif len(self.cache) == self.capacity:
            self.seen.pop(self.cache.pop(0))
        self.cache.append(key)
        self.seen[key] = value
