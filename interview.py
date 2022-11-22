class Solution:
    def stringReplace(self, s, target, replacedValue):
        s_list = s.split(" ")
        print(s_list)
        if target in s_list:
            newString = s.replace(target, replacedValue)
        else:
            newString = s.replace(target, replacedValue)

        return newString


if __name__ == '__main__':
    solution = Solution()
    # test case
    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="Monday", replacedValue="Tuesday"))

    # edge case
    print(solution.stringReplace(s="Today is Monday, we are interviewing", target=" ", replacedValue=""))

    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="", replacedValue=""))

    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="Monday", replacedValue="Monday"))

    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="Mon", replacedValue="Tuesday"))