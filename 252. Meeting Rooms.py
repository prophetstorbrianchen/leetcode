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
                continue
            else:
                # overlap
                print(False)
                return False

        print(True)
        return True


if __name__ == '__main__':
    solution = Solution()
    solution.canAttendMeetings(intervals=[(0, 30), (15, 20), (5, 10)])