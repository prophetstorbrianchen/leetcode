class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)

        # edge case
        if len(s) != len(t):
            return True

        # normal case
        for char_s, chat_t in zip(sort_s, sort_t):
            if char_s != chat_t:
                print(False)
                return False

        print(True)
        return True


if __name__ == '__main__':
    solution = Solution()
    solution.isAnagram(s = "a", t = "ab")