class Solution:
    # hint
    # 要注意edge case -> "(", ")", "((", "(()"
    def isValid(self, s: str) -> bool:
        mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        push_char = ["{", "(", "["]

        stack = []
        for char in s:
            if char in push_char:
                stack.append(char)
            else:
                # 為空還要pop
                if not stack:
                    print(False)
                    return False
                pop_char = stack.pop()
                # 沒有對應的括號
                if pop_char != mapping[char]:
                    print(False)
                    return False

        # stack內部有殘留括號
        if stack:
            print(False)
            return False

        print(True)
        return True


if __name__ == '__main__':
    solution = Solution()
    solution.isValid(s = "()[]{}")