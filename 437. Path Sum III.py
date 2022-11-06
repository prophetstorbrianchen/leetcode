from base_function import BuildTree
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # hint
    # 使用combination sum的概念來做
    # cp和pc為體制外的東西，不需要隨著上下層而改變 -> cp和cn是要隨著我們的需要而改變
    def pathSum(self, root: [TreeNode], targetSum: int) -> int:
        def count_path(cn, ts, cp):
            if not cn:
                return 0

            cp.append(cn.val)
            # pc ->
            pc = 0

            # 每下到一層，就重新算一次，因為不一定要從root開始算，也不一定要從leaf開始算
            ps = 0

            for i in range(len(cp) - 1, -1, -1):
                # 開始做加總，如果ps加到跟ts一樣時，表示這就是我們要的
                ps = ps + cp[i]
                if ps == ts:
                    pc = pc + 1

            # 這種用法要記，從下面判斷的值，往上開始傳
            # 而傳上來的值，是需要左右子樹來累積的
            # 累積完在往上層傳
            # 此層的結果不必向下傳，而是要等左右子樹的結果向上傳
            accumlate_pc = pc + count_path(cn.left, ts, cp) + count_path(cn.right, ts, cp)
            print(accumlate_pc)

            # 左右子樹傳完值上來之後就要pop
            cp.pop()
            return accumlate_pc

        total_count = count_path(root, targetSum, [])
        print(total_count)

        return total_count


if __name__ == '__main__':
    solution = Solution()
    buildTree = BuildTree()
    root = buildTree.deserialize([1,2,"N","N",2,"N","N"])
    solution.pathSum(root= root, targetSum = 8)