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


"""Given an array of integers nums sorted in non-decreasing order, find the position of a given element, if there are multiple positions, return any of them is acceptable. return -1 if the element does not exist.

For example give array [5, 6, 7, 8, 10],  and target 8, the algorithm should return index 3 as the result.

Given array [5, 6, 7, 8, 8, 8, 10], and target 8 , the algorithm should return any one of [3, 4, 5]


[5, 8, 8, 8, 10]

left
[5, 8, 8, 2, 10] 
[5, 8, 8] 1
[5, 8] 1

right
[5, 8, 8, 8, 10] 
[8, 8, 10] 1
[8, 10] 1

使用binary search找出最左和最右的index
"""

# hash table
class Solution_1:
    # time O(n)
    # memory is O(n)
    def find_index(self, array, target):
        hash_table = []

        for i, item in enumerate(array):
            if item == target:
                hash_table.append(i)

        if not hash_table:
            return -1
        else:
            return hash_table[-1]

    # time O(n)
    # memory is O(1)
    def find_first_index(self, array, target):
        for i, item in enumerate(array):
            if item == target:
                return i

        return -1

    # time O(logn)
    # memory is O(1)
    def find_index_bs(self, array, target):
        l = 0
        r = len(array) - 1

        while l < r:
            m = (l + r) // 2
            if target == array[m]:
                return m

            if array[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

    def find_index_bs_improve(self, array, target):
        l = 0
        r = len(array) - 1

        while l < r:
            m = (l + r) // 2
            if target == array[m]:
                return m

            if array[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1


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

    solution_1 = Solution_1()
    # array = [5, 6, 7, 8, 10] # ans = 3
    # target = 8
    # array = [] # ans = -1
    # target = 8
    array = [6, 8, 8, 9, 10]  # ans = 0
    target = 7
    # print(solution.find_index(array, target))
    print(solution_1.find_index_bs_improve(array, target))