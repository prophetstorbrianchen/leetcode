class Solution:
    def maxArea(self, height: [int]) -> int:
        max_area = 0
        length = len(height) - 1
        l, r = 0, len(height) - 1

        while l < r:
            width = min(height[l], height[r])
            area = length * width
            max_area = max(max_area, area)

            if height[l] <= height[r]:
                l = l + 1
                length = length - 1
            else:
                r = r - 1
                length = length - 1

        print(max_area)
        return max_area

    def maxArea_2(self, height: [int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            if height[l] <= height[r]:
                l = l + 1
            else:
                r = r - 1

        # print(max_area)
        return max_area


if __name__ == '__main__':
    solution = Solution()
    solution.maxArea_2(height = [1,1])