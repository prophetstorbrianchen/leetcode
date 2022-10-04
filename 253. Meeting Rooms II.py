class Solution:
    # hint
    # 看筆記或影片
    def minMeetingRooms(self, intervals: list) -> int:
        start_list = []
        end_list = []
        for start, end in intervals:
            start_list.append(start)
            end_list.append(end)

        sorted_start_list = sorted(start_list)
        sorted_end_list = sorted(end_list)

        start_index = 0
        end_index = 0
        count = 0
        res = 0
        while start_index < len(sorted_start_list):
            # 有個edge case，(0,5) (5,10) -> 這只能算一間房
            if sorted_start_list[start_index] < sorted_end_list[end_index]:
                count = count + 1
                start_index = start_index + 1
            else:
                count = count - 1
                end_index = end_index + 1

            # 需要理解一下，為啥要取max -> 因為這邊的算法並非是直觀meeting room數量，他這邊算的是變化量，以最少的方式排出來的變化量
            res = max(res, count)
        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    # solution.minMeetingRooms(intervals = [(0, 30), (5, 10), (15, 20)])
    solution.minMeetingRooms(intervals=[(0, 30), (5, 10), (10, 15)])
