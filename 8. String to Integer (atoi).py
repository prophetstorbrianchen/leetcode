INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, s: str) -> int:
        # method 1 -> edge case 太多了
        """
        sign_list = ["+", "-"]
        number_list = ["0","1","2","3","4","5","6","7","8","9"]

        filter_list = []

        # 空白要先處理
        for i, c in enumerate(s):
            if c in sign_list or c in number_list or c == " ":
                filter_list.append(c)
            else:
                break

        index_record = []
        for i, c in enumerate(filter_list):
            if c != " ":
                index_record.append(i)

        new_filter = filter_list[index_record[0]:index_record[]]


        # filter_list 為空
        if not filter_list:
            return 0

        record_list_list = ["+"]
        record_number_list = []
        # edge case
        if len(filter_list) >= 2:
            if filter_list[0] in sign_list and filter_list[1] in sign_list:
                return 0
            else:
                for c in filter_list:
                    if len(record_list_list) == 3:
                        break

                    if c in sign_list:
                        record_list_list.append(c)
                    else:
                        record_number_list.append(c)

        # process string to digital
        record_number_list.reverse()

        base_digital = 1
        res = 0
        for c in record_number_list:
            res = res + int(c) * base_digital
            base_digital = base_digital * 10

        print(res)
        if record_list_list[-1] == "+":
            pass
        else:
            res = res * -1

        print(res)
        return res
        """

        # method 2
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans


if __name__ == '__main__':
    solution = Solution()
    solution.myAtoi(s="   -42")