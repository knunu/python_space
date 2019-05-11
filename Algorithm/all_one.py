class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = dict()
        self.minKeys = set()
        self.maxKeys = set()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        keys, minKeys, maxKeys = self.keys, self.minKeys, self.maxKeys

        # Process for keys (dict)
        if key in keys:
            keys[key] += 1
        else:
            keys[key] = 1

        # Process for minimum key
        existentMinKey = next(iter(minKeys)) if len(minKeys) > 0 else key
        if len(minKeys) == 0:
            minKeys.add(key)

        if keys[key] > keys[existentMinKey]:
            minKeys.discard(key)
        elif keys[key] == keys[existentMinKey]:
            minKeys.add(key)
        elif keys[key] < keys[existentMinKey]:
            minKeys.clear()
            minKeys.add(key)

        # Process for maximum key
        existentMaxKey = next(iter(maxKeys)) if len(maxKeys) > 0 else key
        if len(maxKeys) == 0:
            maxKeys.add(key)

        if keys[key] > keys[existentMaxKey]:
            maxKeys.clear()
            maxKeys.add(key)
        elif keys[key] == keys[existentMaxKey]:
            maxKeys.add(key)
        elif keys[key] < keys[existentMaxKey]:
            maxKeys.discard(key)

        self.keys, self.minKeys, self.maxKeys = keys, minKeys, maxKeys

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        keys, minKeys, maxKeys = self.keys, self.minKeys, self.maxKeys

        # Process for keys (dict)
        if key in keys:
            if keys[key] > 1:
                keys[key] -= 1
            else:
                del keys[key]
                minKeys.discard(key)
                maxKeys.discard(key)

        # Process for minimum key
        existentMinKey = next(iter(minKeys)) if len(minKeys) > 0 else key
        if len(minKeys) == 0:
            minKeys.add(key)

        if keys[key] > keys[existentMinKey]:
            minKeys.discard(key)
        elif keys[key] == keys[existentMinKey]:
            minKeys.add(key)
        elif keys[key] < keys[existentMinKey]:
            minKeys.clear()
            minKeys.add(key)

        # Process for maximum key
        existentMaxKey = next(iter(maxKeys)) if len(maxKeys) > 0 else key
        if len(maxKeys) == 0:
            maxKeys.add(key)

        if keys[key] > keys[existentMaxKey]:
            maxKeys.clear()
            maxKeys.add(key)
        elif keys[key] == keys[existentMaxKey]:
            maxKeys.add(key)
        elif keys[key] < keys[existentMaxKey]:
            maxKeys.discard(key)

        self.keys, self.minKeys, self.maxKeys = keys, minKeys, maxKeys

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.maxKeys)) if len(self.maxKeys) != 0 else ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.minKeys)) if len(self.minKeys) != 0 else ""


if __name__ == "__main__":
    allOne = AllOne()
    allOne.inc("a")
    allOne.inc("b")
    allOne.inc("b")
    allOne.inc("c")
    allOne.inc("c")
    allOne.inc("c")
    allOne.dec("b")
    allOne.dec("b")
    print(allOne.getMinKey())
    allOne.dec("a")
    print(allOne.getMaxKey())
    print(allOne.getMinKey())


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
