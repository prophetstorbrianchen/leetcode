class Solution:
    def mySqrt(self, x: int) -> int:
        # 給一個sort list為 [0, 1, 2, 3, ..., x] -> 不能給list，會炸掉
        l = 0
        r = x + 1

        res_value = float("inf")
        res = 0
        while l <= r:
            m = (l + r) // 2

            if m * m == x:
                print(m)
                return m
            if m * m < x:
                if x - m * m < res_value:
                    res_value = x - (m * m)
                    res = m

            if m * m < x:
                l = m + 1
            else:
                r = m - 1

        print(res)
        return res

        """
        l = 1
        r = x
        while l + 1 != r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                r = mid
            if mid * mid < x:
                l = mid
        return l
        """


if __name__ == '__main__':
    solution = Solution()
    solution.mySqrt(x = 2147395599)