class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = dict()
        self.minKeys = set()
        self.maxKeys = set()
        self.candidateMinKey = None

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        keys, minKeys, maxKeys, candidateMinKey = self.keys, self.minKeys, self.maxKeys, self.candidateMinKey

        """ Process for common key and values """
        if key in keys:
            keys[key] += 1
        else:
            keys[key] = 1

        """ Process for maximum key """
        # 1. Check and assign existent max key except input key.
        existentMaxKey = None
        for maxKey in maxKeys:
            if key != maxKey:
                existentMaxKey = maxKey
                break

        # 2. Check maxKeys' size is 0. if so, then initialize maxKeys with adding the key.
        if len(maxKeys) == 0:
            maxKeys.add(key)

        # 3. If there is a valid existentMaxKey, handle it through comparing values.
        if existentMaxKey is not None:
            if keys[key] > keys[existentMaxKey]:
                maxKeys.clear()
                maxKeys.add(key)
            elif keys[key] == keys[existentMaxKey]:
                maxKeys.add(key)
            elif keys[key] < keys[existentMaxKey]:
                maxKeys.discard(key)

        """ Process for minimum key """
        # 1. Check and assign existent min key except input key.
        existentMinKey = None
        for minKey in minKeys:
            if key != minKey:
                existentMinKey = minKey
                break

        # 2. Check minKeys' size is 0. if so, then initialize minKeys with adding the key.
        if len(minKeys) == 0:
            minKeys.add(key)

        # 3. If there is a valid existentMinKey, handle it through comparing values.
        if existentMinKey is not None:
            if keys[key] > keys[existentMinKey]:
                minKeys.discard(key)
            elif keys[key] == keys[existentMinKey]:
                minKeys.add(key)
            elif keys[key] < keys[existentMinKey]:
                # candidateMinKey is second smallest value's key.
                candidateMinKey = existentMinKey
                minKeys.clear()
                minKeys.add(key)

        # 4. If key in minKeys and maxKeys both, then assign the union of minKeys and maxKeys to pure minKeys (sync)
        if key in minKeys & maxKeys:
            minKeys |= maxKeys

        self.keys, self.minKeys, self.maxKeys, self.candidateMinKey = keys, minKeys, maxKeys, candidateMinKey

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        The process order MUST not be changed! (common -> minimum -> maximum)
        """
        keys, minKeys, maxKeys, candidateMinKey = self.keys, self.minKeys, self.maxKeys, self.candidateMinKey

        if key in keys:
            """ Process for common key and values """
            # 1. Handle key and value as requirement.
            if keys[key] > 1:
                keys[key] -= 1
            else:
                del keys[key]
                minKeys.discard(key)
                maxKeys.discard(key)
                # 2. Assign candidateMinKey to the last key for handling the case that minKeys' size is 0
                if len(keys) == 1:
                    candidateMinKey = next(iter(keys))

                # 3. Handle the case minKeys' size is 0.
                if len(minKeys) == 0:
                    if candidateMinKey in maxKeys:
                        minKeys |= maxKeys
                    else:
                        minKeys.add(candidateMinKey)
                return

            """ Process for minimum key """
            # 1. Check and assign existent min key except input key.
            existentMinKey = None
            for minKey in minKeys:
                if key != minKey:
                    existentMinKey = minKey
                    break

            # 2. Check minKeys' size is 0. if so, then initialize minKeys with adding the key.
            if len(minKeys) == 0:
                minKeys.add(key)

            # 3. If there is a valid existentMinKey, handle it through comparing values.
            if existentMinKey is not None:
                if keys[key] > keys[existentMinKey]:
                    minKeys.discard(key)
                elif keys[key] == keys[existentMinKey]:
                    minKeys.add(key)
                elif keys[key] < keys[existentMinKey]:
                    # candidateMinKey is second smallest value's key.
                    candidateMinKey = existentMinKey
                    minKeys.clear()
                    minKeys.add(key)

            """ Process for maximum key """
            # 1. Check and assign existent max key except input key.
            existentMaxKey = None
            for maxKey in maxKeys:
                if key != maxKey:
                    existentMaxKey = maxKey
                    break

            # 2. Check maxKeys' size is 0. if so, then initialize maxKeys with adding the key.
            if len(maxKeys) == 0:
                maxKeys.add(key)

            # 3. If there is a valid existentMaxKey, handle it through comparing values.
            if existentMaxKey is not None:
                if keys[key] > keys[existentMaxKey]:
                    maxKeys.clear()
                    maxKeys.add(key)
                elif keys[key] == keys[existentMaxKey]:
                    maxKeys.add(key)
                elif keys[key] < keys[existentMaxKey]:
                    maxKeys.discard(key)

            # 4. If key in minKeys and maxKeys both, then assign the union of minKeys and maxKeys to pure maxKeys (sync)
            if key in minKeys & maxKeys:
                maxKeys |= minKeys

            self.keys, self.minKeys, self.maxKeys, self.candidateMinKey = keys, minKeys, maxKeys, candidateMinKey

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
    allOne.inc("a")
    allOne.inc("a")
    allOne.inc("a")
    allOne.inc("a")
    allOne.inc("a")
    allOne.inc("b")
    allOne.inc("b")
    allOne.inc("c")
    allOne.dec("c")
    print(allOne.getMinKey())


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
