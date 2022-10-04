class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        # sorted
        sorted_intervals = sorted(intervals, key=lambda start_time: start_time[0])

        res = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            # non-overlap
            if res[-1][1] < sorted_intervals[i][0]:
                res.append([sorted_intervals[i][0], sorted_intervals[i][1]])
            else:
                # overlap
                tmp = res.pop()
                start = tmp[0]
                end = max(tmp[1], sorted_intervals[i][1])
                res.append([start, end])

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.merge(intervals = [[1,3],[8,10],[15,18],[2,6]])