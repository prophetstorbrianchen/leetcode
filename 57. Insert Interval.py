class Solution:
    # hint
    # 我是用stack和持續更新start跟end來解題
    # 可以看我筆記
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        intervals.append(newInterval)
        new_intervals = intervals

        # 對start time sort -> 這很重要要會使用lambda
        sorted_interval = sorted(new_intervals, key=lambda start_time: start_time[0])

        res = [sorted_interval[0]]
        for i in range(1, len(sorted_interval)):
            # Non overlay
            # 跟stack最上面的那個比
            if res[-1][1] < sorted_interval[i][0]:
                res.append([sorted_interval[i][0], sorted_interval[i][1]])
            else:
                # overlap
                # 因為已經排序過，所以start就是第一個的start，而end就是比較2個的end看哪個比較大
                tmp = res.pop()
                start = tmp[0]
                end = max(tmp[1], sorted_interval[i][1])
                res.append([start, end])

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])