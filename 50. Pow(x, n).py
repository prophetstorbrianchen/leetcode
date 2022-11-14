class Solution:
    def myPow(self, x: float, n: int) -> float:
        # method1 - TLE
        """
        pow = 1
        if n >= 0:
            for i in range(n):
                pow = pow * x
        else:
            for i in range(abs(n)):
                pow = pow / 2

        print(pow)
        return pow
        """

        # 使用python函式
        return x ** n


if __name__ == '__main__':
    solution = Solution()
    solution.myPow( x = 2.00000, n = -2)