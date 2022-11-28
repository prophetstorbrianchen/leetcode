import collections


class Solution:
    def pick_peaks(self, arr):
        # https://www.codewars.com/kata/5279f6fe5ab7f447890006a7
        # 利用指針 -> 指針只能從第二個開始到倒數第二個結束
        # 如果指針大於前一個和後一個 -> 表示為peak -> record

        # define the varible
        pos = []
        peaks = []
        for i in range(len(arr)):
            l = i
            r = i

            # 邊界問題
            if l - 1 < 0:
                continue

            # 指針一直往右找，直到右邊找盡或是比i小或是比i大
            while 0 <= l and r < len(arr):
                # 如果是peak就只要看前一個是不是下降，以及後面是否是上升(假設後面平的不算)
                if arr[i] > arr[l - 1] and arr[i] > arr[r]:
                    # 比i小的case -> find
                    pos.append(i)
                    peaks.append(arr[i])
                    break
                elif arr[r] > arr[i]:
                    # 比i大的case -> 表示i肯定不是peak，直接找下個i
                    break
                else:
                    # 跟i一樣大 -> 繼續往下找
                    r = r + 1

        res = {"pos": pos, "peaks": peaks}
        return res

    def prime_factors(self, n):
        # https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
        # 質因數分解 -> 必會必考 -> 背下來
        count_table = collections.defaultdict(int)

        a = n
        b = n

        # 質因數分解
        while True:  # 使用 while 迴圈
            for i in range(2, (a + 1)):  # 使用 for 迴圈
                if i == b:  # 如果 i 等於 b，表示是質數，跳出 for 迴圈
                    count_table[i] = count_table[i] + 1
                    break
                if a % i == 0:  # 如果可以被 i 整除，表示不是質數
                    count_table[i] = count_table[i] + 1
                    a = int(a / i)  # 重新將 a 設定為商
                    break  # 跳出 for 迴圈
            if a == 1 or a == b:  # 如果商等於 1 或是質數，跳出 while 迴圈
                break

        # 合成字串
        string = ""
        for key, value in count_table.items():
            if value > 1:
                string = string + "(" + str(key) + "**" + str(value) + ")"
            else:
                string = string + "(" + str(key) + ")"

        print(string)
        return string


if __name__ == '__main__':
    solution = Solution()
    # solution.pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])
    solution.prime_factors(n = 10)  # "(2**2)(3**3)(5)(7)(11**2)(17)"