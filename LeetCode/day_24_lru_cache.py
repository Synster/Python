"""

"""


class LRUCache:
    capacity = None
    cache = {}
    cacheList = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            item = self.cache[key]
            self.cacheList.remove(key)
            self.cacheList.insert(0, key)
            return item
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            self.cacheList.insert(0, key)
        else:
            del_key = self.cacheList.pop()
            del self.cache[del_key]
            self.cache[key] = value
            self.cacheList.insert(0, key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.get(2)
cache.put(4, 1)
cache.get(1)
cache.get(2)
