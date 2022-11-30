from collections import defaultdict


class TimeMap:
    # hint
    # 題目要搞懂
    # https://www.youtube.com/watch?v=fu2cD_6E8Hw
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        # values為list
        values = self.store[key]

        # binary search
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            # 要找最接近答案的那個，所以這個res在整個while沒跑完前會一直更新
            # 因為並非找固定某個值，而是timestamp_prev <= timestamp就可以
            if values[m][1] <= timestamp:
                res = values[m][0]

            # 向右找
            if values[m][1] < timestamp:
                l = m + 1
            else:
                # 向左找
                r = m - 1

        print(res)
        return res

    def set_2(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get_2(self, key: str, timestamp: int) -> str:
        # 因為她是照timestamp進來的，所以前面的timestamp一定小，後面的timestamp一定大
        # 指定某一個key了
        value = self.store[key]

        res = ""
        l = 0
        r = len(value) - 1

        while l < r:
            m = (l + r) // 2

            # 找到小於或等於的即可，之前的題目大概都是要等於居多
            if value[m][1] <= timestamp:
                res = value[m][0]

            if value[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return res


if __name__ == '__main__':
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    timeMap.get("foo", 1)
    timeMap.get("foo", 3)
    timeMap.set("foo", "bar2", 4)
    timeMap.get("foo", 4)
    timeMap.get("foo", 5)