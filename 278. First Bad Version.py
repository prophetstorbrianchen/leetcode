# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    # hint
    # 這答案是對的，但並非是個好寫法
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            # 第一個版本就錯的情況
            if m == 1 and isBadVersion(m):
                return m

            if not isBadVersion(m):
                # 向右找
                l = m + 1
                if isBadVersion(l):
                    return l
            else:
                r = m - 1
                if not isBadVersion(r):
                    return m

    def firstBadVersion_1(self, n: int) -> int:
        l = 1
        r = n
        result = 1  # 當n = 1，第一個就是壞掉的情況，這很重要

        while l <= r:
            m = (l + r) // 2
            if not isBadVersion(m):
                # 是對的version，就要向右找
                l = m + 1
            else:
                # 就要向左找，並保留錯的，直到下一次更新
                r = m - 1
                result = m

        return result
