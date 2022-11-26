class Solution:
    def stringReplace(self, s, target, replacedValue):
        s_list = s.split(" ")
        print(s_list)
        if target in s_list:
            newString = s.replace(target, replacedValue)
        else:
            newString = s.replace(target, replacedValue)

        return newString

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


if __name__ == '__main__':



    solution = Solution()
    # test case
    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="Monday", replacedValue="Tuesday"))

    # edge case
    print(solution.stringReplace(s="Today is Monday, we are interviewing", target=" ", replacedValue=""))

    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="", replacedValue=""))

    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="Monday", replacedValue="Monday"))

    print(solution.stringReplace(s="Today is Monday, we are interviewing", target="Mon", replacedValue="Tuesday"))

    # 考繼承
    square = Square(10)
    print(square.area())
    print(square.perimeter())