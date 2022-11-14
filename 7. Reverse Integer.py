class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if int(str_x) < 0:
            tmp = str(-1 * int(x))
            result = (-1 * int(tmp[::-1]))
        else:
            # print(int(str_x[::-1]))
            result = (int(str_x[::-1]))

        # edge case
        if result > (2 ** 31) or result < (-2 ** 31 - 1):
            print(0)
            return 0

        print(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.reverse(x = 120)