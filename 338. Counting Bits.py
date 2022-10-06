class Solution:
    def countBits(self, n: int) -> [int]:
        res = []
        for i in range(n + 1):
            # 先轉二進制
            tmp = bin(i)
            total = 0
            for char in tmp[2:]:
                # 二進制的值相加
                total = total + int(char)
            res.append(total)

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.countBits(n = 2)