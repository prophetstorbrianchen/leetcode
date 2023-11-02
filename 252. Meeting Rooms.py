class Solution:
    # hint
    # https://www.youtube.com/watch?v=PaJxqZVPhbg
    # (0, 8) and (8, 10) -> 並非conflict
    def canAttendMeetings(self, intervals: list) -> bool:
        # sort
        sorted_intervals = sorted(intervals, key=lambda start: start[0])

        res = [intervals[0]]
        for i in range(1, len(sorted_intervals)):
            # non-overlap
            if res[-1][1] <= sorted_intervals[i][0]:
                res.append(sorted_intervals[i])
            else:
                # overlap
                print(False)
                return False

        print(True)
        return True

    def canAttendMeetings_1(self, intervals: list) -> bool:
        sorted_intervals = sorted(intervals)
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]

        if len(intervals) == 1:
            print(True)
            return True

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] > start and sorted_intervals[i][1] >= end:
                start = sorted_intervals[i][0]
                end = sorted_intervals[i][1]
            else:
                print(False)
                return False
        print(True)
        return True


if __name__ == '__main__':
    solution = Solution()
    solution.canAttendMeetings(intervals=[(0, 30), (15, 20), (5, 10)])
    solution.canAttendMeetings_1(intervals=[(0, 30), (15, 20), (5, 10)])