class Solution:
    def isVampire(self, x: int, y: int) -> [bool]:
        # use the string to mapping the result of x*y
        # step 1: save integer of x and y
        # step 2: get the result of x*y and save the integer of result
        # step 3: compare by sort

        result_element_list = []

        element_list = list(str(x) + str(y))
        sorted_result = sorted(list(str(x * y)))

        if len(element_list) != len(sorted_result):
            print(False)
            return False
        else:
            for item in element_list:
                if item in sorted_result:
                    result_element_list.append(item)
                else:
                    print(False)
                    return False

        if sorted(result_element_list) == sorted_result:
            print(True)
            return True
        else:
            print(False)
            return False

    def is_vampire(self, x, y):
        num = str(x * y)
        string_factors = str(x) + str(y)
        factors_count_list = [num.count(fi) for fi in string_factors]
        num_count_list = [string_factors.count(ci) for ci in num]
        if sum(factors_count_list) == sum(num_count_list):
            print(True)
            return True
        else:
            print(False)
            return False


if __name__ == '__main__':
    solution = Solution()
    solution.isVampire(x = 21, y = 60)
    solution.is_vampire(x=21, y=60)