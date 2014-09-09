class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []  #store all the keys in priority order
        self.dictionary = {} #key-value pair
        
    # @return an integer
    def get(self, key):
        value = self.dictionary.get(key,-1)
        if value != -1:
            index = self.stack.index(key)
            self.stack.pop(index)
            self.stack.insert(0,key)
            return value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.dictionary.has_key(key):
            self.dictionary[key] = value
            index = self.stack.index(key)
            self.stack.pop(index)
            self.stack.insert(0,key)
        else:
            if len(self.stack) < self.capacity:
                self.dictionary[key] = value
                self.stack.insert(0,key)
            else:
                #delete the least recent key
                LRUkey = self.stack[-1]
                self.stack.pop()
                self.stack.insert(0,key)
                del self.dictionary[LRUkey]
                self.dictionary[key] = value