class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        # sorted
        sorted_intervals = sorted(intervals, key=lambda start_time: start_time[0])

        # 先把最初的一個放入stack，因為需要拿來做比較
        res = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            # non-overlap
            if res[-1][1] <= sorted_intervals[i][0]:
                res.append([sorted_intervals[i][0], sorted_intervals[i][1]])
            else:
                # overlap
                tmp = res.pop()
                # 要取一個end最小的放入，這樣可以比較能夠避免下一次的overlap
                if tmp[1] < sorted_intervals[i][1]:
                    res.append(tmp)
                else:
                    res.append([sorted_intervals[i][0], sorted_intervals[i][1]])

        print(len(intervals) - len(res))
        return len(intervals) - len(res)


if __name__ == '__main__':
    solution = Solution()
    solution.eraseOverlapIntervals(intervals = [[1,2],[2,3]])