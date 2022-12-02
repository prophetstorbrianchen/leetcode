import random


class RandomizedSet:
    # hint
    # 看題目，insert不能重複
    # remove不能remove不存在的東西
    # 要使用random
    # 要熟悉list的 append/insert/pop/remove/del
    # 要熟悉set的 add/remove

    def __init__(self):
        self.stack = set()

    def insert(self, val: int) -> bool:
        if val not in self.stack:
            self.stack.add(val)
            # print(True)
            return True
        else:
            # print(False)
            return False

    def remove(self, val: int) -> bool:
        if val in self.stack:
            self.stack.remove(val)
            # print(True)
            return True
        else:
            # print(False)
            return False

    def getRandom(self) -> int:
        x = random.randint(0, len(self.stack) - 1)
        # print(list(self.stack)[x])
        return list(self.stack)[x]


if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    randomizedSet.insert(1)
    randomizedSet.remove(2)
    randomizedSet.insert(2)
    randomizedSet.getRandom()
    randomizedSet.remove(1)
    randomizedSet.insert(2)
    randomizedSet.getRandom()