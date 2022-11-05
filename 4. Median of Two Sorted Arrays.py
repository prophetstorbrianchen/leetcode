class Solution:
    # hint
    # 看筆記
    # 注意邊界值
    # https://www.youtube.com/watch?v=q6IEA26hvXc
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # swap, B是長的A是短的
        if len(B) < len(A):
            A, B = B, A

        # 對A做binary search
        l, r = 0, len(A) - 1
        while True:
            # A
            i = (l + r) // 2
            # B, 因為是index的計算方式，所以-2才是我們所求
            j = half - i - 2

            # 比大小以及防止超出邊界
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # 正確
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # 表示Aleft的值太大，R要向左移動 -> 取到M的值才會變小 for A
            # 此為A的binary search
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


if __name__ == '__main__':
    solution = Solution()
    solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])