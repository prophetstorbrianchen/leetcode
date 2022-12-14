import heapq
import math
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if not self.head:
            self.head = ListNode(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(data)

    def print(self):
        if not self.head:
            print(self.head)
        node = self.head
        while node:
            end = " -> "
            print(node.val, end=end)
            node = node.next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TireNode:
    def __init__(self):
        self.children = {}
        self.endOfNode = False


class Trie:
    # hint
    # 必須先了解TireNode，還要了解cur = cur.children[c]的意思
    # 了解insert/search/startsWith的意思
    # https://www.youtube.com/watch?v=oobqoCJlHA0
    # https://www.bilibili.com/video/BV1NL411n7s9/?spm_id_from=333.788.recommend_more_video.1

    def __init__(self):
        # 初始root為空
        self.root = TireNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                # 建立分支
                cur.children[c] = TireNode()
            # 娜到下面去接成prefix,值白翻譯往下層走(可以試試mark掉這行，會看到"a","p","l","e"為一個平行結構)
            cur = cur.children[c]
        cur.endOfNode = True

        print(cur)

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            # 若有找到，在往下繼續找
            cur = cur.children[c]

        # 必須還要判斷是不是end，若是才是真的有找到，不然就是中間一樣而已
        if cur.endOfNode is True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            # 若有找到，在往下繼續找
            cur = cur.children[c]

        return True


class TireNode1:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TireNode1()
            cur = cur.children[c]
        cur.isWord = True


class WordDictionary:
    # hint
    # https://www.youtube.com/watch?v=BTf05gs_8iU
    # leetcode 208的變話題
    # 多想想dfs和遞迴
    def __init__(self):
        # 初始root為空
        self.root = TireNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.endOfNode = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                # 碰到"."的處理
                if c == ".":
                    # 因為"."可以替代任何字母，所以直接往下一層去做search
                    # 由上到下，由左至右做深度搜尋
                    for char, child in cur.children.items():
                        print(char, child)
                        # i + 1 表示往下一層
                        # 下一層，即表示要帶這層的child下去做搜尋
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfNode

        # 從第0層開始
        return dfs(0, self.root)


class MedianFinder:
    # hint
    # 因為要降到O(logn)的解法，就必須使用heap
    # 先去把資料結構的heap弄熟 -> Max heap/Min heap -> 如果要在Max heap取最大值那就是O(1),如果要在Min heap取最小值那就是O(1)
    # 在去搞懂python的heapq -> python的heap default為Min heap，那如果要做Max heap，則push近來的值要乘-1
    # 解題的方式請看影片和我的筆記 -> 這題重點在heap的觀念
    # https://www.youtube.com/watch?v=itmhHWaHupI
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


class Codec:
    # hint
    # 此題就是把Tree轉list,list轉tree給實做出來(之前有想做，沒做出來)
    # 此題為資料結構的實做題，很重要
    # 此題我會用list去做，而非string
    # serialize -> preorder並且加上leaf為none的情況
    # deserialize -> 使用i當作指針，一直往後指.
    # deserialize -> 要記得treenode可以在dfs內產生，並return none or node去串接node.left or node.left
    # 寫dfs要記得dfs的定義是甚麼，以及base case訂好
    # 看影片和筆記
    # https://www.youtube.com/watch?v=u4JAi2JJhI8
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                # N表示tree的None
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        """
        # 使用list來做
        # print(res)
        # return res
        """
        # 使用string來做
        # 轉成逗號加sting,要記得這個用法
        string_result = ",".join(res)
        print(string_result)
        return string_result

    def deserialize(self, data):
        # i is pointer for input list
        # the self.i can be used for sub function directly
        self.i = 0

        # 使用list的方法來轉
        """
        def dfs():
            # base case
            if data[self.i] == "N":
                self.i = self.i + 1
                return None

            node = TreeNode(int(data[self.i]))
            self.i = self.i + 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()
        """
        # 答案要用string，但一樣要先轉成list，完全多此一舉
        vals = data.split(",")
        def dfs():
            # base case
            if vals[self.i] == "N":
                self.i = self.i + 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i = self.i + 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

class Solution:
    def twoSum(self, nums: [], target: int) -> []:
        seen = {}
        for i, b in enumerate(nums):
            # core logic:  a + b = target -> a = target - b
            a = target - b
            # use hashtables to implement lookups as they are extremely fast
            if a in seen:
                print([seen[a], i])
                return [seen[a], i]
            seen[b] = i

    # hint
    # 1.剛開始使用dict失敗
    # 2.使用list來保持紀錄最長的數
    # 3.找到重複的char時，必須跳過重複的那個，但必須拿後面的字串再來接
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_list = []
        maxCount = 0
        for pos, char in enumerate(s):
            if char not in temp_list:
                temp_list.append(char)
                maxCount = max(len(temp_list), maxCount)
            else:
                # find the duplicate char on temp list
                j = temp_list.index(char)
                temp_list = temp_list[j + 1:]
                temp_list.append(char)

        return maxCount

    # hint
    # implment Palindrome 的function
    # 由中心點向左右檢查
    # 使用baaabad跑一次就會明白
    # https://www.wongwonggoods.com/python/python_leetcode/leetcode-python-5/
    def longestPalindrome(self, s: str) -> str:

        def is_palindrome(s, start, end):
            while (0 <= start and end < len(s) and s[start] == s[end]):
                start = start - 1
                end = end + 1

            # print(s[start+1:end])
            return s[start + 1:end]

        # always update the ans is the longest Palindrome
        ans = ""
        for i in range(len(s)):
            print("--i is {0}--".format(i))
            # process "aba" situation
            tmp_ans = is_palindrome(s, i, i)
            print("first: {0}".format(tmp_ans))
            if len(tmp_ans) > len(ans):

                ans = tmp_ans

            # process "aa" situation
            tmp_ans = is_palindrome(s, i, i + 1)
            print("second: {0}".format(tmp_ans))
            if len(tmp_ans) > len(ans):
                ans = tmp_ans

        return ans

    # hint
    # 左右的container只能取最小的那個
    # 從2邊向中間逼近，找出每個值
    # 保留最大的即可
    # https://ithelp.ithome.com.tw/articles/10218631
    def maxArea(self, height: list) -> int:
        max_water = 0
        left_start_index = 0
        right_start_index = len(height) - 1

        while left_start_index < right_start_index:

            if height[left_start_index] <= height[right_start_index]:
                length = height[left_start_index]
            else:
                length = height[right_start_index]
            width = right_start_index - left_start_index
            temp_water = length * width
            max_water = max(max_water, temp_water)

            if height[left_start_index] < height[right_start_index]:
                left_start_index = left_start_index + 1
            else:
                right_start_index = right_start_index - 1


        # 爆力解
        """
        temp_list = []
        for i, left_contianer in enumerate(height):
            for j, right_contianer in enumerate(height):
                if i < j:
                    if left_contianer <= right_contianer:
                        length = left_contianer
                    else:
                        length = right_contianer
                    width = j - i
                    area = length * width
                    temp_list.append(area)

        print(max(temp_list))
        """

        print(max_water)
        return max_water

    # hint
    # two sum的延伸，須熟知two sum
    # sort很重要，可以避免重複
    # nums[i + 1:] -> 第一個不重複算
    # 最後要防止[[0,0,0], [0,0,0]]
    # https://www.wongwonggoods.com/python/python_leetcode/leetcode-python-15/
    def threeSum(self, nums: list) -> list:
        nums.sort()
        # print(nums)
        # print(nums[1:])

        ans_list = []
        for i, value in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            two_sum = 0 - value
            hash_table = {}

            # two sum algo
            for j, x in enumerate(nums[i + 1:]):
                y = two_sum - x
                if y in hash_table:
                    # print("find two sum")
                    temp_list = [y, x]

                    if temp_list:
                        # print("find three sum")
                        temp_list.insert(0, value)

                    # prevent [0,0,0,0] -> [[0,0,0], [0,0,0]]
                    if temp_list in ans_list:
                        pass
                    else:
                        ans_list.append(temp_list)
                hash_table[x] = j
        return ans_list

    """
    # 爆力解
    ans_list = []
    for i, value in enumerate(nums):
        two_sum = 0 - value

        hash_table = {}
        for j, a in enumerate(nums):
            if i == j:
                continue
            else:
                b = two_sum - a
                if b in hash_table:
                    # print("find two sum")
                    temp_list = [b, a]
                    #print(temp_list)

                    if temp_list:
                        temp_list.append(value)

                    if temp_list == [0, 0, 0] and [0, 0, 0] not in ans_list:
                        ans_list.append(temp_list)

                    # 處理重複的部分(此部分為爆力解)
                    if not ans_list:
                        ans_list.append(temp_list)
                    else:
                        flag = True
                        for item_list in ans_list:
                            count = 0
                            for num in temp_list:
                                if num in item_list:
                                    count = count + 1
                            if count == 3:
                                flag = False
                                break
                        if flag is True:
                            ans_list.append(temp_list)

                        # print("find three sum")

                hash_table[a] = j
    print(ans_list)
    return ans_list
    """
    # hint
    # https://www.bilibili.com/s/video/BV1KV411z7Jm -> dummy
    # https://www.youtube.com/watch?v=0czlvlqg5xw -> linked list的基礎教學
    # https://www.delftstack.com/zh-tw/howto/python/linked-list-in-python/
    # https://ithelp.ithome.com.tw/articles/10264368?sc=iThelpR
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        cur = head
        length = 0

        dummy = ListNode(0)
        dummy.next = head

        # 紀算總長度
        while (cur != None):
            length = length + 1
            cur = cur.next

        # 此時cur和dummy的linked list會一模一樣
        # 但是只要cur做了刪除或是連接新的node時，dummy舊會一起更改 -> 因為大家都reference到相同的位址，這邊全部都要用位址來思考
        cur = dummy
        for i in range(length - n):
            # 此時的cur是位址
            cur = cur.next

        # 做刪除並且做連接的動作
        # 做刪除連接的動作時，大家都是會被一起更新的，因為連接的位址改了
        cur.next = cur.next.next

        # 可以試看看，舊會明白linked list的位址一絲
        #dummy_100 = ListNode(100)
        #cur.next.next = dummy_100

        return dummy.next

    # hint
    # 括號的特性是成對存在
    # 一律都是從左括號起始
    # 根據以上特性使用stack
    def isValid(self, s: str) -> bool:
        left_list = ["(", "{", "["]
        char_mapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack_list = []
        ans = True

        for i, char in enumerate(s):
            if char in left_list:
                stack_list.append(char)
            elif not stack_list:
                # 防起始就是單一右括號: "]"
                return False
            else:
                relative_char = stack_list.pop()
                if char != char_mapping[relative_char]:
                    return False

        if len(stack_list) != 0:
            return False

        return ans

    # hint
    # list必定會有2個指針
    # 必定要使用dummy
    # https://maxming0.github.io/2020/01/04/Merge-Two-Sorted-Lists/
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        dummy = ListNode(0)
        pre = dummy

        # 其中一個list一定要run完
        # 看哪個比較小就接再pre後面
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                # list1的指針向右
                list1 = list1.next
            else:
                pre.next = list2
                # list2的指針向右
                list2 = list2.next

            # 指到之後，pre也跟著網下走
            pre = pre.next

        # 上棉run完之後必定有一個微空
        # 那表示有剩的那個list直接接再pre後面即可
        if list1 or list2:
            if list1:
                pre.next = list1
            else:
                pre.next = list2

        # 檢查用
        # while dummy.next:
        #     print(dummy.next.val)
        #     dummy = dummy.next

        return dummy.next

    def mergeKLists(self, lists: list) -> ListNode:
        print()

        dummy = ListNode(0)

        return dummy

    # hint
    # 使用binary tree
    # 有看沒懂
    # https://maxming0.github.io/2020/04/26/Search-in-Rotated-Sorted-Array/
    # https://desolve.medium.com/%E5%BE%9Eleetcode%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-6-binary-search-691c9a842a77
    # https://www.youtube.com/watch?v=RH3tZldhjJ0
    def search(self, nums: list, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m] < target or target < nums[l] <= nums[m] or nums[m] < target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        return -1

    # hint
    # 有排序過的list
    # no duplicates in the list
    # 此提為經典的Binary Search
    # 可達O(logN)
    def searchInsert(self, nums: list, target: int) -> int:
        # index; 此時的lo=l 而 up=r
        lo, up = 0, len(nums) - 1

        # 如果target == mid，那mid所在的位置就是我們要的答案；
        # 如果target > mid，表示答案只可能在mid右邊到尾端之間(不含mid)；
        # 如果target < mid，表示答案只可能在mid左邊到開頭之間(不含mid)。

        while lo <= up:
            mi = (lo + up) // 2
            if nums[mi] == target:
                return mi
            elif target > nums[mi]:
                lo = mi + 1
            else:
                up = mi - 1

        return lo

    # hint
    # 經典DFS的題目
    # 遞迴就是一直往下找
    # for loop就是整個攤平
    # https://leetcode.com/problems/combination-sum/discuss/1777569/FULL-EXPLANATION-WITH-STATE-SPACE-TREE-oror-Recursion-and-Backtracking-oror-Well-Explained-oror-C%2B%2B -> 講得不錯
    # https://maxming0.github.io/2020/10/02/Combination-Sum/
    def combinationSum(self, candidates: list, target: int) -> list:
        def dfs(cur, path):
            if cur == 0:
                # 找到了，紀錄答案
                # 它是用扣的方式，只要扣到0表示找到target
                res.append(path)
            for n in candidates:
                # 表示超過target了，回上層; 也表示cur和path會回到上一層的狀態
                if n > cur:
                    break
                # 保證不重複,([2,3,5], 8)
                # if [3] -> 沒有這行會變[3,2]; 但在[2]時，已經輪過[2,3]
                if path and n < path[-1]:
                    continue

                # 往下一層找
                dfs(cur - n, path + [n])

        res = []
        # 不重複的重要步驟
        candidates.sort()
        dfs(target, [])
        return res

    # hint
    # 先做reverse再做對角線互換可以達到順時針轉90度
    # 自己畫一次就知道
    # https://maxming0.github.io/2021/04/25/Rotate-Image/
    def rotate(self, matrix: list) -> None:

        for i in range(3):
            for j in range(i, 0, -1):
                print(i,j)

        """
        Do not return anything, modify matrix in-place instead.
        """

        # 先reverse
        matrix.reverse()

        # 做對角線元素互換
        # i為第i列
        # j為第j個
        # 左下角的三角形即是這2個for loop
        for i in range(len(matrix)):
            for j in range(i):
                # 同時交換，所以沒有誰先誰後的問題
                # print(matrix[i][j], matrix[j][i])
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # print(matrix[i][j], matrix[j][i])

        print(matrix)

    # hint
    # 有的字串有相同的字元指是位置不同，但均屬於同一類，所以必須要對每個字串做sort之後再做處理
    # 使用dict去record排序過後的字串
    # 若是有sort後相同的字串在裡面，表示是同一類
    def groupAnagrams(self, strs: list) -> list:
        temp_dict = {}
        ans_list = []

        for i, item in enumerate(strs):
            temp_list = []
            for j, char in enumerate(item):
                # sort
                temp_list.append(char)
                temp_list.sort()

            # record sorted string
            standard_string = ""
            for k, char in enumerate(temp_list):
                standard_string = standard_string + char
            # print(standard_string)

            # use dict to record
            if standard_string not in temp_dict:
                temp_dict[standard_string] = []

            # record unsorted string
            temp_dict[standard_string].append(item)

        for key, value in temp_dict.items():
            ans_list.append(value)

        return ans_list

    # hint
    # 先定義初始cur，因為第一個item是沒人可以比的，所以抓整個list中最小的當做初始cur
    # 逐步算出最大值
    # 和原本的去比，比出來看哪個大就放入ans_list
    # -2, 1, -3, 4, -1, 2, 1, -5, 4
    # -2, 1, -3, 4, -1, 2, 1, -5, 4  -> item
    # -5,-1, -2,-2,  3, 5, 6,  1, 5  -> cur
    # -2, 1, -2, 4,  3, 5, 6,  1, 5  -> ans list
    # 自己列一次就明白了
    # https://maxming0.github.io/2020/04/26/Maximum-Subarray/
    def maxSubArray(self, nums: list) -> int:

        cur = min(nums)
        ans_list = []

        for i, item in enumerate(nums):
            if i == 0:
                cur = max(item, cur)
            else:
                cur = max(item, item + cur)
            ans_list.append(cur)

        ans = max(ans_list)
        print(ans)
        return ans

    # hint
    # 分成4種case去做，分別是上下左右
    # 依照順時針順序，所以從up -> right -> down -> left
    # 最後一個left時，需要end need "up - 1",因為前面被加過一次，但python不會算最後一個，這樣會被掠過，所以要-1
    # https://www.youtube.com/watch?v=U-fW7MEJPLs
    def spiralOrder(self, matrix: list) -> list:

        res = []
        # index
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while (up <= down) and (left <= right):
            # process up
            for i in range(left, right + 1, 1):
                res.append(matrix[up][i])
                #print(matrix[up][i])
            up = up + 1

            # process right
            for i in range(up, down + 1, 1):
                res.append(matrix[i][right])
                #print(matrix[i][right])
            right = right - 1

            # process down
            if up <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                    #print(matrix[down][i])
                down = down - 1

            # process left
            if left <= right:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                    #print(matrix[i][left])
                left = left + 1

        return res

    # hint
    # current是每次都會只走一格
    # reach指需要紀每次的current可到到達的最遠位置(index)
    # 使用current和reach的位置(index)來判斷是否走到最後一步
    # 若是reach遠超過current那也算到達
    # 指要沒發生Flse那結果必定為True
    # 看影片會很好懂
    # https://maxming0.github.io/2020/04/26/Jump-Game/
    def canJump(self, nums: list) -> bool:

        # only record index
        reach = 0

        for cur, num in enumerate(nums):
            if reach < cur:
                return False

            # 如果可以到更遠的位置，reach就要更新
            if reach <= cur + num:
                reach = cur + num

        return True


    # hint
    # 要先對左端點進行排序，由小至大
    # 需要設定初始list,已排序完的第一個當起始點
    # 若是右端點比下一個的左端點來的大 -> 需要更新
    # 反之則需要append
    # https://maxming0.github.io/2020/11/18/Merge-Intervals/
    def merge(self, intervals: list) -> list:
        print(intervals)

        # 對左端點排序
        intervals.sort(key=lambda x: x[0])

        # 放入sort完的第一個，之後去做比較
        res = [intervals[0]]

        # 若是右端點比下一個的左端點來的大 -> 需要更新
        # 反之則需要append
        for i in range(len(intervals) - 1):
            if res[-1][1] >= intervals[i + 1][0]:
                res[-1][1] = max(intervals[i + 1][1], res[-1][1])
            else:
                res.append(intervals[i + 1])

        print(res)
        return res

    # hint
    # 看熟 56. Merge Intervals，完全一模一樣
    # https: // leetcode.com / problems / merge - intervals /
    def insert(self, intervals: list, newInterval: list) -> list:

        # 需要先加進list內，之後在鏡行排序
        intervals = intervals + [newInterval]

        intervals.sort(key=lambda x: x[0])

        # 放入sort完的第一個，之後去做比較
        res = [intervals[0]]

        # 若是右端點比下一個的左端點來的大 -> 需要更新
        # 反之則需要append
        for i in range(len(intervals) - 1):
            if res[-1][1] >= intervals[i + 1][0]:
                res[-1][1] = max(intervals[i + 1][1], res[-1][1])
            else:
                res.append(intervals[i + 1])

        print(res)
        return res

    def uniquePaths(self, m: int, n: int) -> int:
        #ans = math.factorial(m + n - 2) // (math.factorial(n - 1) * math.factorial(m - 1))
        #print(ans)

        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        ans = dp[-1]
        return ans

    # hint
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6    =>為n
    # 1 -> 2 -> 3 -> 5 -> 8 -> 13   =>為走到台階的方法有幾種
    # dp[n] = dp[n - 1] + dp[n - 2] =>key point
    # https://maxming0.github.io/2020/07/31/Climbing-Stairs/
    def climbStairs(self, n: int) -> int:
        # use Fibonacci -> timeout
        """
        def feb(n):
            if n <= 1:
                return 1
            else:
                return (feb(n - 1) + feb(n - 2))

        print(feb(n))
        return feb(n)
        """

        # use dp
        """
        dp1 = 1
        dp2 = 2
        for i in range(n - 1):
            dp1, dp2 = dp2, (dp1 + dp2)

        print(dp1)
        return dp1
        """

        # my code
        dp = [1, 2]

        for i in range(2, n, 1):
            ans = dp[i - 1] + dp[i - 2]
            dp.append(ans)

        print(dp[n - 1])
        return dp[n - 1]

    # hint
    # 如同旋轉走matric那題一樣，分上下左右處理
    # 處理原本是0的部分，然後非0改成0，紀錄非0改成0的這種位置
    # 若是然後非0改成0的這種位置就跳過，直到所有的矩陣內元素都處理過一次
    # https://maxming0.github.io/2021/08/13/Set-Matrix-Zeroes/
    # 小明得更快
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # hash table
        become_zero_position = []
        up_bond = 0
        down_bond = len(matrix) - 1
        left_bond = 0
        right_bond = len(matrix[0]) - 1

        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 and (i, j) not in become_zero_position:

                    # process up
                    if i - 1 >= up_bond and (i, j) not in become_zero_position:
                        for k in range(i, up_bond - 1, -1):
                            if matrix[i - k][j] == 0:
                                pass
                            else:
                                matrix[i - k][j] = 0
                                become_zero_position.append((i - k, j))

                    # procee down
                    if i + 1 <= down_bond and (i, j) not in become_zero_position:
                        for k in range(i, down_bond + 1, 1):
                            if matrix[k][j] == 0:
                                pass
                            else:
                                matrix[k][j] = 0
                                become_zero_position.append((k, j))

                    # process left
                    if j - 1 >= left_bond and (i, j) not in become_zero_position:
                        for k in range(j, left_bond - 1, -1):
                            if matrix[i][j - k] == 0:
                                pass
                            else:
                                matrix[i][j - k] = 0
                                become_zero_position.append((i, j - k))

                    # process right
                    if j + 1 <= right_bond and (i, j) not in become_zero_position:
                        for k in range(j, right_bond + 1, 1):
                            if matrix[i][k] == 0:
                                pass
                            else:
                                matrix[i][k] = 0
                                become_zero_position.append((i, k))

        print(matrix)

    def minWindow(self, s: str, t: str) -> str:
        pass

    # hint
    # BFS(深度搜尋)，也就是所有的方像都找過一次
    # https://www.youtube.com/watch?v=pfiQ_PS1g8E
    # https://www.youtube.com/watch?v=oUeGFKZvoo4
    # https://maxming0.github.io/2020/07/21/Word-Search/
    def exist(self, board: list, word: str) -> bool:
        def bfs(i, j, p, layer, ans_list):
            # print(layer)
            # 如果長度一樣就返回
            if p == len(word):
                return True

            # 超過邊界
            if i >= m or i < 0:
                return False

            # 超過邊界
            if j >= n or j < 0:
                return False

            # 當字符不相等
            if board[i][j] != word[p]:
                return False

            # 不能有回頭路
            if (i, j) in path:
                return False

            # 找到了這個福合順序的字元
            cur = board[i][j]
            ans_list.append(cur)

            # 在找到的當下，網下一層走，但下一層不能在走上一層的路，這邊用0來代替的原因是因為他這邊抓的都是char，所以碰到0一律掠過 -> 這是十分特別的case
            board[i][j] = 0
            # 要繼續往下找
            # 往此字元的4個方向繼續往下找
            res = (bfs(i - 1, j, p + 1, layer + 1, ans_list) or bfs(i + 1, j, p + 1, layer + 1, ans_list) or bfs(i, j - 1, p + 1, layer + 1, ans_list) or bfs(i, j + 1, p + 1, layer + 1, ans_list))
            # 當回到原本那層層時，就要恢復原狀 -> 這是十分特別的case
            board[i][j] = cur

            return res

        m = len(board)
        n = len(board[0])
        # 紀路回頭路的path
        path = []
        ans_list = []

        for i in range(m):
            for j in range(n):
                if bfs(i, j, 0, 0, ans_list):
                    print(ans_list)
                    return True

    # hint
    # 因為只取1位或是2位，但是是有限制的條件(頭部可為0，2位數不可以超過26)
    # 這就是爬樓梯的變形題
    # https://maxming0.github.io/2021/08/18/Decode-Ways/

    # 肯定是要一位數的組合在加上2位數的組合
    # dp[i] = dp[i - 1] (s[i - 1] != 0)
    #         + dp[i - 2] (i > 1, s[i - 2] != 0, s[i - 2: i] <= 26)
    # dp[0] = 1
    def numDecodings(self, s: str) -> int:
        # 沒使用遞迴
        n = len(s)
        dp0, dp1, dp2 = 0, 1, 0
        for i in range(1, n + 1):
            # dp2為每次新的紀算，所以要reset為0
            dp2 = 0
            if s[i - 1] != '0':
                dp2 = dp2 + dp1

            # 加完第一種(一位數的處理)在加上第二種(2位數的處理)
            if i > 1 and s[i - 2] != '0' and int(s[i - 2: i]) <= 26:
                dp2 = dp2 + dp0

            # 向前移動
            dp0, dp1 = dp1, dp2
        return dp2

        # 這題也可以使用遞迴

    # hint
    # https://maxming0.github.io/2020/12/16/Validate-Binary-Search-Tree/
    # 因為左子樹必須要比母樹小 -> upper會跟著母樹變，lower不動
    # 因為右子樹必須要比母樹大 -> lower會跟著母樹變，upper不動
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(r, u, l):
            if r is None:
                return True

            val = r.val
            if (val >= u) or (val <= l):
                return False

            if dfs(r.left, val, l) and dfs(r.right, u, val):
                return True

        # upper設定無限大
        # lower設定無限小
        upper_bound = float('inf')
        lower_bound = float('-inf')
        ans = dfs(root, upper_bound, lower_bound)
        print(ans)
        return ans

    # hint
    # https://maxming0.github.io/2020/07/13/Same-Tree/
    # 2刻樹跑到最後如果都一起跑完，也就是都是None的話，表示2個是一樣的 -> True
    # 2刻樹跑到最後如果沒有一起跑完，也就是1個微None,1個為非None，表示2個是不一樣的 -> False
    # 如果val都一樣，左子樹，右子樹都相同時，表示2刻樹都一樣
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        def dfs(r, d, res):
            print(d)
            if r is None:
                return res


            res.append(r.val)

            dfs(r.left, d + 1, res)
            dfs(r.right, d + 1, res)

        p_result = []
        q_result = []

        dfs(p, 0, p_result)
        print(p_result)
        dfs(q, 0, q_result)
        print(q_result)

        if p_result == q_result:
            return True
        else:
            return False
        """

        def dfs(a, b):
            if a is None and b is None:
                return True

            if not a or not b:
                return False

            if a.val == b.val and dfs(a.left, b.left) and dfs(a.right, b.right):
                return True

        return dfs(p, q)

    # hint
    # https://www.youtube.com/watch?v=gnOqWd10Sws
    # https://blog.csdn.net/coder_orz/article/details/51363095
    # https://www.youtube.com/watch?v=Tuij96VBdu8
    def levelOrder(self, root: TreeNode) -> list:
        # 深度搜尋方式
        """
        def dfs(r, d, res):
            if r is None:
                return res

            # 每一層的第一個 or 第一次，都需要先給list
            # d == 0時要有list, d == 1時要有list...一此類推
            # 畫個圖就會明白
            if len(res) == d:
                res.append([])

            # 找到了
            res[d].append(r.val)

            # 先向left走，left走完再走right
            dfs(r.left, d + 1, res)
            dfs(r.right, d + 1, res)

        result = []
        dfs(root, 0, result)
        print(result)
        return result
        """

        # 廣度搜尋
        # BFS摩板(由上到下，由左到右，平行處理)
        # queue有FIFO的特性
        # 把tree的root加到queue
        # queue如果不為空，就做loop
        # 用queue length當做loop的次數
        # 把queue的東西拿出來做處理
        # 看這個影片 https://www.youtube.com/watch?v=gnOqWd10Sws
        res = []

        if not root:
            return []

        # queue有FIFO的特性
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            cur_list = []

            for _ in range(queue_len):
                # 先進來的先處理
                node = queue.popleft()

                # queue的東西處理完一個，就放入cur_list
                cur_list.append(node.val)

                # 看left還有沒有
                if node.left:
                    queue.append(node.left)
                # 看right還有沒有
                if node.right:
                    queue.append(node.right)
            res.append(cur_list)
        print(res)
        return res

    # hint(104. Maximum Depth of Binary Tree)
    # 會做 102. Binary Tree Level Order Traversal，這題肯定會做，先把102弄透
    # 可以直接使用102的方法
    # 也可以找出max的depth存起來就好
    def maxDepth(self, root: TreeNode) -> int:
        """
        def dfs(r, d, ans):
            if r is None:
                return ans

            if len(ans) == d:
                ans.append([])

            ans[d].append(r.val)

            dfs(r.left, d + 1, ans)
            dfs(r.right, d + 1, ans)

        result = []
        dfs(root, 0, result)

        return len(result)
        """

        def dfs(r, d, ans):
            # 就是個終止條件，回傳啥不中要
            if r is None:
                return 0

            # 存最大的depth
            if d >= ans[0]:
                ans[0] = d

            # left, right全部都找過一次
            dfs(r.left, d + 1, ans)
            dfs(r.right, d + 1, ans)

        # 排除空樹
        if root is None:
            print(0)
            return 0

        # 必定有樹，樹高從１開始計算
        result = [1]
        dfs(root, 1, result)
        print(result[0])
        return result[0]

    # hint
    # binary tree 經典題，利用前序/中序 or 中序/後序來排出binary tree
    # 須知道前序/中序/後序的定義
    # https://www.youtube.com/watch?v=9rarSk7946Q -> 原理講得很好
    # https://www.youtube.com/watch?v=Qc0XLGFnchU -> code講得很好
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:

        # 遞迴需要有終止條件
        if not preorder or not inorder:
            return None

        # find root
        rootval = preorder[0]

        # give a tree
        root = TreeNode(rootval)

        # Use inorder to distinguish left and right tree
        inorder_root_index = inorder.index(rootval)

        # preorder = [3,9,20,15,7]
        # inorder = [9,3,15,20,7]
        # 我們知道3為root，所以可在inorder分成左右2邊(左子樹和右子樹)
        root.left = self.buildTree(preorder[1: inorder_root_index + 1], inorder[:inorder_root_index])
        root.right = self.buildTree(preorder[inorder_root_index + 1:], inorder[inorder_root_index+1:])

        return root

    # hint
    # https://www.youtube.com/watch?v=Hr5cWUld4vU
    # https://maxming0.github.io/2020/04/29/Binary-Tree-Maximum-Path-Sum/
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # 如果為負值就不選，所以直接用0取max
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            # 每次更新最大值
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # 回傳給上一層，因為規則是無法包含左右樹一起回傳給上層(可以看移下影片)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

    # hint
    # https://www.youtube.com/watch?v=TgnftvU8rxc
    def maxProfit(self, prices: list) -> int:

        max_profit = 0

        # 為買入的min_price
        min_price = float("inf")

        for price in prices:
            # 一邊要記最大的profit一邊要記最小的price
            min_price = min(min_price, price)
            # 此時的price是賣出
            max_profit = max(max_profit, price - min_price)

        return max_profit

    # hint
    # https://www.youtube.com/watch?v=P6RZZMu_maU
    def longestConsecutive(self, nums: list) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            # the n is first number
            if (n - 1) not in numset:
                length = 1
                # find total continue number for the n
                while (n + length) in numset:
                    length = length + 1
                longest = max(longest, length)

        return longest

    # hint
    # https://www.youtube.com/watch?v=Sx9NNgInc3A
    # must follow dp[i] = dp[i + len(w)] rule -> is word break
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                print(i + len(w), s[i: i + len(w)])
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

    # hint
    # two pointer
    # https://www.youtube.com/watch?v=gBTe7lFR3vc
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head

        # has cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # fast and slow meet
            if fast == slow:
                return True

        return False

    # hint
    # https://maxming0.github.io/2020/08/20/Reorder-List/
    # https://www.youtube.com/watch?v=S5bfdUTrKLM
    # slow and fast pointer to cut prefix and postfix
    # remember listnode reverse
    # remember list node merge
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # listnode reverse
        head2 = slow.next
        slow.next = None
        dummy = ListNode(0, None)
        while head2:
            tmp = head2.next
            head2.next = dummy.next
            dummy.next = head2
            head2 = tmp

        # listnode merge
        head1 = head
        head2 = dummy.next
        """
        while head1 and head2:
            tmp = head2
            head2 = head2.next
            tmp.next = head1.next
            head1.next = tmp
            head1 = head1.next.next
        """

        while head1 and head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2

    # hint
    # https://www.youtube.com/watch?v=lXVy6YWFcRM
    # DP
    # Need to see the vidio or note
    def maxProduct(self, nums: list) -> int:
        # the zero case -> [-1, 0, -2]
        max_result = max(nums)
        cur_max, cur_min = 1, 1

        for n in nums:
            # edge case, need to reset to 1
            if n == 0:
                cur_max, cur_min = 1, 1
                continue

            tmp = n * cur_max

            # the n is for this case [-1, 8] and [-1, -8]
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)

            max_result = max(max_result, cur_max)

        return max_result

    # hint
    # https://www.youtube.com/watch?v=nIVW4P8b1VA
    # 需要判斷向左搜尋還是向右搜尋
    # 還需要知道sort完之後,左邊一定為最小
    def findMin(self, nums: list) -> int:
        # edge case: [1]
        result = nums[0]
        # index position
        l, r = 0, len(nums) - 1

        # binary search
        while l <= r:
            # 已經SORT過了 左扁一定最小
            if nums[l] < nums[r]:
                result = min(result,nums[l])
                break

            m = (l + r) // 2
            # update the min result
            result = min(result, nums[m])

            # 判斷向左搜尋還是向右搜尋
            if nums[m] >= nums[l]:
                # 向左搜
                l = m + 1
            else:
                # 向右搜
                r = m - 1

        print(result)
        return result

    # hint
    # https://maxming0.github.io/2020/07/12/Reverse-Bits/
    def reverseBits(self, n: int) -> int:
        """
        # translate from 2 to 10
        print(int(bin(n), 2))
        # 32 bits
        res, power = 0, 31

        while n:
            # 最右邊那位也就是第一位 需要向左移31位
            print(n & 1)
            res += (n & 1) << power

            # 最右邊那位已經計算完畢，所以必須向右一位
            n >>= 1

            # 下一個要移的舊要減一
            power -= 1
        print(int(bin(res), 2))
        return res
        """

        # --second
        # 使用字串的方式來處理，更為直覺一些
        print(len(bin(n)[2:]))

        # 把ob給拿掉 -> python使用ob表示二進智 -> 0b01000000000000000000000000000000
        print(bin(n)[2:])

        # zfill前面補0,zfill(32)總共補滿32位員
        print(bin(n)[2:].zfill(32))

        # [::-1] -> list或是string的reverse很常用到
        print(bin(n)[2:].zfill(32)[::-1])

        # 轉10進智
        print(int(bin(n)[2:].zfill(32)[::-1], 2))

        return int(bin(n)[2:].zfill(32)[::-1], 2)

    # hint
    # use the case of leetcode 190
    # https://maxming0.github.io/2021/02/01/Number-of-1-Bits/
    def hammingWeight(self, n: int) -> int:
        ret = 0

        # 先轉成32位員然後把32bits填滿
        print(bin(n)[2:].zfill(32))

        # 在轉成string來做判斷
        for i in str(bin(n)[2:].zfill(32)):
            if i == "1":
                ret += 1

        print(ret)
        return ret

    # hint
    # DP
    # rob[i] = max(rob[i-2] + nums[i], rob[i])
    # 前一次的結果須要帶給後面來做運算，但是根據題目會有不同的條件來去取前一次的結果
    # https://www.youtube.com/watch?v=73r3KWiEvyk
    # https://maxming0.github.io/2020/09/14/House-Robber/
    def rob(self, nums: list) -> int:
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    # hint
    # dfs
    # 經典題
    # https://www.youtube.com/watch?v=TCX9qd5WbIg
    # 也可用BFS,但我還不熟模板
    # https://www.youtube.com/watch?v=pV2kpPD66nE
    def numIslands(self, grid: list) -> int:
        def dfs(grid, row, column):
            # 直接返回的情況,包含上下左右的邊界以及碰到0(直接回到上層)
            if row < 0 or row >= max_row or column < 0 or column >= max_colum or grid[row][column] == "0":
                return 0

            # 先把陸地變為海洋
            grid[row][column] = "0"

            # 若不為編階以及0,那就是要針對上下左右各自進行處理
            # top
            dfs(grid, row - 1, column)

            # down
            dfs(grid, row + 1, column)

            # left
            dfs(grid, row, column - 1)

            # right
            dfs(grid, row, column + 1)

        # edge case
        if not grid:
            return 0

        island_count = 0

        # define 邊界
        max_row = len(grid)
        max_colum = len(grid[0])

        # 歷遍所有元素
        for r in range(max_row):
            for c in range(max_colum):
                if grid[r][c] == "1":
                    # dfs即為小幫手
                    dfs(grid, r, c)
                    island_count = island_count + 1

        print(island_count)
        return island_count

    # hint
    # 使用prev = None會好懂很多
    # 經典題&功具題
    # https://www.youtube.com/watch?v=7cN0_iVQ6vI
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev

    # hint
    # https://www.youtube.com/watch?v=EgI5nU9etnU
    # 需要用範例舉例逐步說明
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        """
        # --[method 1]--
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # 做出preMap這張表
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # 只要有重複即為loop
        visiting = set()

        def dfs(crs):
            # base case
            if crs in visiting:
                return False

            # base case
            if preMap[crs] == []:
                return True

            # 有走訪到而且能繼續往下走
            visiting.add(crs)

            # 把map內給走完
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # 已經走完回到上層，所以要把隻前走訪的點給拿掉
            visiting.remove(crs)

            # 走訪完就要設為空，防止重走
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        """

        # --[method 2]--
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # 做出preMap這張表
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # 若有cycle則是true否則為false
        def cycle(node, tracker):
            tracker[node] = True

            for n in preMap[node]:
                if n in tracker or cycle(n, tracker):
                    return True

            # 迴上一層，走訪過的點要被pop掉
            tracker.pop(node)
            return False

        for i in range(numCourses):
            tracker = {}
            # 若有cycle
            if cycle(i, tracker):
                return False

        return True

    # hint
    # This is more complex but still can understand
    # Please review the note and vedio
    # https://www.youtube.com/watch?v=asbcE9mZz_U
    # This approach will encounter TLE but this method is very important
    def findWords(self, board: list, words: list) -> list:
        root = TireNode1()

        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])

        # prevent duplicate
        ret, visit = set(), set()

        def dfs(r, c, node, word):
            # --base case--
            # top and down border
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in node.children or (r, c) in visit:
                return

            # left and right border
            if c < 0 or c >= cols:
                return

            # if the element not in node
            if board[r][c] not in node.children:
                return

            # if the element already visited
            if (r, c) in visit:
                return

            # --prepare into the next layer--
            # record the visit element and prepare into next layer
            visit.add((r, c))

            # update node -> prepare to in next layer
            node = node.children[board[r][c]]

            # update word -> prepare to in next layer
            word = word + board[r][c]

            # base case, if the node is the end layer
            if node.isWord:
                ret.add(word)

            # --into the next layer--
            # top dfs
            dfs(r - 1, c, node, word)

            # down dfs
            dfs(r + 1, c, node, word)

            # left dfs
            dfs(r, c - 1, node, word)

            # right dfs
            dfs(r, c + 1, node, word)

            # back to the previous layer and need to remove the visited element
            visit.remove((r, c))

        # trval all element and using the depth-first search
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        print(list(ret))
        return list(ret)

    # hint
    # reuse the house rob 1
    # two case: "No First House" or "No Last House"
    # https://www.youtube.com/watch?v=rWAJCfYYOvM
    def rob_2(self, nums: list) -> int:
        def rob1_fun(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        # due to the house position is cycle
        # there are two case
        # the one is "No First House"
        case1 = rob1_fun(nums[1:])

        # the other one is "No Last House"
        case2 = rob1_fun(nums[:-1])

        # get the max between case1 and case2
        if len(nums) == 1:
            # edge case for the house is only one
            return nums[0]
        else:
            return max(case1, case2)

    # hint
    # need to use set(), not list
    def containsDuplicate(self, nums: list) -> bool:
        hash_table = set()

        # need to sort first otherwise TLE
        nums.sort()

        for n in nums:
            if n not in hash_table:
                hash_table.add(n)
            else:
                return True

        return False

    # hint
    # 不能加入(if not r.left) or (if not r.right)的判斷 -> 因為空樹也是要交換的
    # dfs的經點基礎題
    # https://www.youtube.com/watch?v=OnSn2XEQ4MY
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(r):
            # if root is empty return previous layer
            if not r:
                return

            # swap the left child and right child
            temp = r.left
            r.left = r.right
            r.right = temp

            # into next layer
            dfs(r.left)
            dfs(r.right)

        dfs(root)
        return root

    # hint
    # 必須要做出in-order的list -> 必須要知道in-order/pre-order/post-order如何產生(implement)在binary tree中
    # 經典功具題
    # neetcode的方法是用stack
    # https://www.youtube.com/watch?v=5LUXSvjmGCw
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []

        def dfs(r, result):
            if not r:
                return

            # in-order 
            dfs(r.left, result)
            result.append(r.val)
            dfs(r.right, result)

            """
            # pre-order
            result.append(r.val)
            dfs(r.left, result)
            dfs(r.right, result)

            # post-order
            dfs(r.left, result)
            dfs(r.right, result)
            result.append(r.val)
            """

        dfs(root, res)
        print(res[k-1])
        return res[k-1]

    # hint
    # 因為可以直接使用BST的特性來決定跑左或右，所以不需要用到dfs所有tree都掃過一次
    # 需要注意edge case,
    # https://www.youtube.com/watch?v=gs2LMfuOR9k
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # go into right child tree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # go into left child tree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # (當p or q其中一個為另一個的祖先) or (p or q 其中一個比root大其中一個比root小 -> 需要同時走到左樹和右樹時，那root鐵定舊是最小組先)
            else:
                return root

    # hint
    # 很特殊的解法
    # 需要用到累積的prefix和postfix
    # prefix的前欠要假設多個1, postfix的後面要多個1 -> 這養就可以通吃所有case,不需要額外處理edge case
    # 如果是成法要用1,加法要用0
    # 詳細可以看我的筆記
    # https://www.youtube.com/watch?v=bNvIQI2wAjk
    def productExceptSelf(self, nums: list) -> list:
        result_list = []
        prefix_list = [1] * (len(nums) + 1)
        postfix_list = [1] * (len(nums) + 1)

        # make the prefix list
        cur = 1
        for i, n in enumerate(nums):
            cur = cur * n
            prefix_list[i + 1] = cur

        # make postfix list
        reverse_nums = nums[::-1]
        cur = 1
        for i, n in enumerate(reverse_nums):
            cur = cur * n
            postfix_list[i + 1] = cur
        postfix_list.reverse()

        # get the result
        prefix_index = 0
        postfix_index = 1
        for _ in range(len(nums)):
            result_list.append(prefix_list[prefix_index] * postfix_list[postfix_index])
            prefix_index = prefix_index + 1
            postfix_index = postfix_index + 1

        print(result_list)
        return result_list

    # hint
    # using hash table or sort to solve this problem
    # https://www.youtube.com/watch?v=9UtInBqnCgA
    def isAnagram(self, s: str, t: str) -> bool:
        # --method 1--
        # using sorted
        """
        s_sort = sorted(s)
        print(s_sort)

        t_sort = sorted(t)
        print(t_sort)

        if s_sort == t_sort:
            return True

        return False
        """
        # --method 2--
        # using hash table
        s_dict = {}
        t_dict = {}

        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] = s_dict[c] + 1

        for c in t:
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] = t_dict[c] + 1

        if s_dict == t_dict:
            return True

        return False

    # hint
    # 需要對start time來做sort，之前就有碰到類似的問題,也是用到類似的觀念
    # 要會使用lambda來做排序
    # L1 <= L2 and L2 < R1 -> L為start R為end
    # 注意如何收回圈
    # https://www.youtube.com/watch?v=PaJxqZVPhbg
    def canAttendMeetings(self, intervals: list) -> bool:
        # sort the interval start time
        sorted_intervals = sorted(intervals, key=lambda start_time: start_time[0])
        print(sorted_intervals)

        for i in range(len(sorted_intervals)):
            if i == (len(sorted_intervals) -1):
                break

            if (sorted_intervals[i][0] <= sorted_intervals[i + 1][0]) and (sorted_intervals[i + 1][0] < sorted_intervals[i][1]):
                print(False)
                return False

        print(True)
        return True

    # hint
    # need to use two pointer
    # one is start the other one is end
    # 可以看我的比紀
    def minMeetingRooms(self, intervals: list) -> int:
        # sort the start and end time
        start_list = sorted([i[0] for i in intervals])
        end_list = sorted([i[1] for i in intervals])

        s, e = 0, 0
        init_count = 0
        count_list = []

        # 當start list處理完之後，奇時最大直就會知道了不需要連end list都需要跑完
        while s < len(intervals):
            if start_list[s] < end_list[e]:
                s = s + 1
                init_count = init_count + 1
                count_list.append(init_count)
            else:
                e = e + 1
                init_count = init_count - 1
                count_list.append(init_count)

        print(max(count_list))
        return max(count_list)

    # hint
    # the valid tree -> no loop and the visit node is same with node number
    # make the adj table to run dfs -> this is the key skill(must be familiar)
    # https://www.youtube.com/watch?v=bXsUuownnoQ
    def validTree(self, n: int, edges: list) -> bool:
        # empty tree is valid tree
        if not n:
            return True

        # make a dictionary table
        adj = {i: [] for i in range(n)}

        # 做出每個node的之間相鄰關係
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        print(adj)
        visit = set()

        # check loop case and add node into visit
        def dfs(i, prev):
            # base case
            if i in visit:
                return False

            visit.add(i)
            # 針對相鄰的node繼續往下走
            for j in adj[i]:
                # 走過的node不能在走過
                if j == prev:
                    continue

                # normal case
                prev = i
                if not dfs(j, prev):
                    return False
            return True

        # no loop and the visit node is same with node number
        # all of the node is start from 0 and we assume the prev is -1 when the start node is 0
        # print(dfs(0, -1) and n == len(visit))
        return dfs(0, -1) and n == len(visit)

    # hint
    # 此題我是用sort方式去解決
    # 如果+1之後可以在nums找到，就表示沒少，反之就是少了那個樹
    # 要額外處理edge case
    # 此題有很多不同種類的方法,neetcode舊是使用xor
    # https://www.youtube.com/watch?v=WnPLSRLSANE
    def missingNumber(self, nums: list) -> int:
        # --method 1 -> sort and mapping
        """
        # find the max number to process edge case
        max_num = len(nums)
        # start from 0, so I using the -1 to add 1 to match start with 0
        init_num = -1

        # edge case
        # [0,1] -> 2
        if max_num not in nums:
            print(max_num)
            return max_num

        # using sort to process normal case
        # if init_num add 1 and not match in the list -> return init_num
        # [0,1,3] -> 2
        for item in sorted(nums):
            init_num = init_num + 1
            if init_num == item:
                continue
            else:
                print(init_num)
                return init_num
        """
        # --method 2 -> xor
        # make a full list
        init = 0
        max_num = len(nums)
        full_nums = [i for i in range(max_num + 1)]

        # 0 xor 任一數即為任一數本身
        # 那5^5 -> 0
        # 那5^3^5 -> 3
        # 所以[3,0,1] ^ [0,1,2,3] -> 3^0^1^0^1^2^3 -> 2
        for n in nums:
            init = init ^ n

        for n in full_nums:
            init = init ^ n

        print(init)
        return init

    # hint
    # 這題很難，可以多用幾個例子來理解
    # 第一個部分是建立圖形，第二個是DFS利用dict去歷遍所有點
    # 要了解visited的True和False的意義
    # 要了解dfs所return的True和False的意義
    def alienOrder(self, words: list) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # ex: ["waf", "wa"] -> 這順序有問題,直接回空
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # 如何把圖弄出來
            # 2個字開始比，若第一個就不一樣，做dict起來
            # ex: ["wrf", "er"] -> {w:set(e)}
            # ex: ["wrt", "wrf"] -> {t:set(f)}
            # 直到所有都做完
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            # base case
            if char in visited:
                return visited[char]

            visited[char] = True

            # 使用dict和dfs往下找
            for neighChar in adj[char]:
                # 若是回true，則表示碰到cycle
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)
            return False

        # 每隔char都找過一次
        for char in adj:
            # 若為True表示有cycle
            if dfs(char):
                return ""

        # 因為使用postorder dfs,從leaf往回
        res.reverse()
        print(res)
        return "".join(res)

    # hint
    # 要先了解題目在說啥
    # 必須要用word的長度來做分界 -> encode
    # 找出#字元的面是數字，並且要知道前面的數字有可能是多個位數 -> deode
    # decode的部分可以用個實際的例子來跑一次
    # 注意不能用isdigital -> 因為數字有可能為字元
    # https://www.youtube.com/watch?v=B1k_sxOSgv8
    # Encode and Decode Strings - Leetcode 271
    def encode(self, strs: list):
        encode_string = ""
        for word in strs:
            word_len = str(len(word))
            encode_string = encode_string + word_len + "#" + word

        print(encode_string)
        return encode_string

    def decode(self, strs: str):
        # i 為位置也就是pointer
        result, i = [], 0

        """
        #-- method 1--
        i = 0
        # 不能用for,因為要全部跑完
        while i < len(strs):
            # 給初始pointer的位置
            j = i

            # 抓出#字元的前面位數
            while strs[j] != "#":
                j = j + 1
            length = int(strs[i: j])
            word = strs[j + 1: j + length + 1]
            result.append(word)

            #更新pointer的位置
            i = j + length + 1
        """
        # -- method 2--
        # j是另一個pointer，用來記初始位置
        # i, j 會一起從起點開始
        j = 0
        while i < len(strs):
            if strs[i] == "#":
                length = int(strs[j: i])
                word = strs[i + 1: i + length + 1]
                result.append(word)
                i = i + length + 1
                j = i
            else:
                i = i + 1

        print(result)
        return result

    # hint
    # 要了解從DFS那邊開始的解析(需要實際上劃過)，一直到直接使用DP -> 非常地不直覺，但很厲害
    # 看看我寫的筆記以及影片
    # https://www.youtube.com/watch?v=cjWnW0hdF1Y
    def lengthOfLIS(self, nums: list) -> int:
        # 這個這樣設定很高明，因為每個num從自己開始，都是1開始計算
        # 不這樣做，必須還要額外往前拿值
        LIS = [1] * len(nums)

        # i從後面倒回來看
        # j會從i+1開始直到nums結束
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # 有條件地放進來，取max，因為max也不能append，所以只能22相比，比完在和下個比
                # [1, 2, 4, 3] -> 那[4, 3]這個就不會放進來比
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        print(max(LIS))
        return max(LIS)

    # hint
    # 需要從DFS了解，是可以用DFS做，但這是暴力解法
    # 要看筆記以及影片
    # https://www.youtube.com/watch?v=H9bfqozjoqs
    def coinChange(self, coins: list, amount: int) -> int:
        # 設定最大值不可超越的那種，或是給無限大也可以
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # i為1~7的總和情形 -> [1, 3, 4, 5], amount = 7
        for i in range(1, amount + 1):
            # 每種情況
            # 如果i = 7, 即要考慮 c = 1, 3, 4, 5 -> dp[6], dp[4], dp[3], dp[2]
            for c in coins:
                if i >= c:
                    # 因為dp剛開始都有給個最大值，所以就是比一比，取最小的那個，然後更新
                    dp[i] = min(dp[i], 1 + dp[i - c])

        # 表示沒辦法更新到最後面的值 -> 也就是說[3, 5], amount = 7
        if dp[amount] == amount + 1:
            return -1
        else:
            print(dp[amount])
            return dp[amount]

    # hint
    # Union Find的演算法
    # 這題還是不懂，需要多看幾次，這題的觀念很重要
    # 多看筆記和影片
    # https://www.youtube.com/watch?v=8f1XPm4WOUc
    def countComponents(self, n: int, edges: list) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res= n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] = rank[p2] + rank[p1]
            else:
                par[p2] = p1
                rank[p1] = rank[p1] + rank[p2]

            return 1

        res = n
        for n1, n2 in edges:
            res = res - union(n1, n2)

        return res

    # hint
    # 對每個數先轉成二進制 -> 需要去除0b的開頭，然後對string做加總
    # 然後做append
    # 這題可以用DP去解，可參考Neetcode
    # https://www.youtube.com/watch?v=RyBM56RIWrM
    def countBits(self, n: int) -> [int]:
        res = []
        for i in range(n + 1):
            sum = 0
            for j in bin(i)[2:]:
                sum = sum + int(j)
            res.append(sum)

        print(res)
        return res

    # hint
    # 使用hash table(dict)
    # 針對hash table的value做排序，然後append值
    # 也可以使用heap -> 會比較快
    # Needcode使用bucket sort -> 有空在學
    # https://www.youtube.com/watch?v=YPTqKIgVk-k
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        # --method 1--
        """
        hash_table = {}
        res = []

        # 先sort過，由小排到大
        nums.sort()

        # 建立hash table
        for n in nums:
            if str(n) not in hash_table:
                hash_table[str(n)] = 0
            hash_table[str(n)] = hash_table[str(n)] + 1

        # print(hash_table)
        # print(sorted(hash_table.items(), key=lambda item: (item[1], item[0]), reverse=True))
        # 用lamdba排序，這為單條件排序，只依照value去排
        # print(sorted(hash_table.items(), key=lambda item: (item[1]), reverse=True))
        # 用lamdba排序，這為多條件排序，先依value排在排key
        sorted_hash_table = sorted(hash_table.items(), key=lambda item: (item[1], item[0]), reverse=True)

        # 抓k所需要的值
        for i in range(k):
            res.append(int(sorted_hash_table[i][0]))

        # print(res)
        return res
        """
        # method 2(使用 max heap)
        heap = []
        res = []
        dict = collections.Counter(nums)
        for key, val in dict.items():
            # 乘-1，是為了max heap，item可以是tuple类型带卫星数据，默认使用item[0]进行排序
            val = val * (-1)
            heapq.heappush(heap, (val, key))

        for i in range(k):
            element_tuple = heapq.heappop(heap)
            value = element_tuple[0] * (-1)
            element = element_tuple[1]
            print(element, value)
            res.append(element)

        print(res)
        return res

    # hint
    # 實作computer science的加法器
    # 可以看這篇，就可以知道為什麼要用0x80000000
    # https://blog.csdn.net/fuxuemingzhu/article/details/79379939
    # https://www.polarxiong.com/archives/LeetCode-371-sum-of-two-integers.html
    # https://www.youtube.com/watch?v=gVUrDV4tZfY
    def getSum(self, a: int, b: int) -> int:
        # --method 1--
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
        """

        # --method 2--
        # 必須要滿32bit
        mask = 0xffffffff

        # 使sum成為32bit，但不影響值
        sum = (a ^ b) & mask

        # 表示有進位
        part = a & b

        while part:
            a = sum
            b = (part << 1) & mask
            sum = (a ^ b)
            part = a & b

        # 32 bits integer max
        if sum & 0x80000000:
            sum = sum - 0x100000000

        print(sum)
        return sum

    # hint
    # 觀念就是
    # 小明和neet的觀念一樣，但code寫出來不一樣 -> 一個用while去做 一個用dfs去做，都要學一夏
    # https://www.youtube.com/watch?v=s-VkcjHqkGI
    # https://maxming0.github.io/2021/03/25/Pacific-Atlantic-Water-Flow/
    def pacificAtlantic(self, matrix: [[int]]) -> [[int]]:
        def dfs(matrix, q):
            m = len(matrix)
            n = len(matrix[0])
            ret = set([])
            # 需要處理每個點的上下左右
            directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}

            # q為當前能流到pacific or atlantic的所有點，看你現在是處理哪邊
            while len(q) > 0:
                # 當前的點拿出來處理
                curx, cury = q.pop()
                ret.add((curx, cury))
                height = matrix[curx][cury]

                # process 上邊 -> (-1, 0)
                tmpx, tmpy = -1 + curx, 0 + cury
                # 新的點比當前的點高 -> 新的點也可以流入海洋
                if 0 <= tmpx < m and 0 <= tmpy < n and matrix[tmpx][tmpy] >= height:
                    # 若不再裡面，表示要納入 -> 因為有可能有重複，因為都是上下左右一起走
                    if (tmpx, tmpy) not in ret:
                        # 加到q中，之後從q繼續往下走
                        q.append((tmpx, tmpy))
                        # 把新的點加到結過中
                        ret.add((tmpx, tmpy))

                # process 下邊 -> (1, 0)
                tmpx, tmpy = 1 + curx, 0 + cury
                if 0 <= tmpx < m and 0 <= tmpy < n and matrix[tmpx][tmpy] >= height:
                    # 若不再裡面，表示要納入
                    if (tmpx, tmpy) not in ret:
                        # 加到
                        q.append((tmpx, tmpy))
                        ret.add((tmpx, tmpy))

                # process 左邊 -> (0, -1)
                tmpx, tmpy = 0 + curx, -1 + cury
                if 0 <= tmpx < m and 0 <= tmpy < n and matrix[tmpx][tmpy] >= height:
                    # 若不再裡面，表示要納入
                    if (tmpx, tmpy) not in ret:
                        # 加到
                        q.append((tmpx, tmpy))
                        ret.add((tmpx, tmpy))

                # process 右邊 -> (0, 1)
                tmpx, tmpy = 0 + curx, 1 + cury
                if 0 <= tmpx < m and 0 <= tmpy < n and matrix[tmpx][tmpy] >= height:
                    # 若不再裡面，表示要納入
                    if (tmpx, tmpy) not in ret:
                        # 加到
                        q.append((tmpx, tmpy))
                        ret.add((tmpx, tmpy))

                """
                for dirx, diry in directions:
                    # 新到的點，也就是4個方向新產生的點
                    tmpx, tmpy = dirx + curx, diry + cury
                    # 判斷新的點是否比當前的點來的高，能進if表示符合
                    if 0 <= tmpx < m and 0 <= tmpy < n and matrix[tmpx][tmpy] >= height:
                        # 若不再裡面，表示要納入
                        if (tmpx, tmpy) not in ret:
                            # 加到
                            q.append((tmpx, tmpy))
                            ret.add((tmpx, tmpy))
                """
            return ret

        # 從靠pacific的點開始算，先拿到所有靠pacific的點
        # m為row
        m = len(matrix)
        if m == 0:
            return []
        # n為col
        n = len(matrix[0])

        # q為相鄰pacific的起始點
        q = []
        for i in range(m):
            q.append((i, 0))
        for i in range(n):
            q.append((0, i))

        # 出來的結果為，能流到pacific的所有點
        pac = dfs(matrix, q)

        # 從靠atlantic的點開始算，先拿到所有靠atlantic的點
        q = []
        for i in range(m):
            q.append((i, n - 1))
        for i in range(n):
            q.append((m - 1, i))

        # 出來的結果為，能流到atlantic所有點
        atl = dfs(matrix, q)

        # pac和atl的結果做交集，那有交集的肯定就是同時能夠流入pacific和atlantic
        res = pac.intersection(atl)
        print(res)
        return [list(x) for x in res]

    # hint
    # 使用slide windows以及雙指針概念
    # 必須搞清楚左指針何時向右移，右指針何時向右移
    # 我的方法是老實的做count table
    # neetcode在count table時有多動點手腳
    # 這觀念講得不錯 -> https://www.youtube.com/watch?v=SLAKjysDODM
    # https://www.youtube.com/watch?v=gqXU1UyA8pk
    def characterReplacement(self, s: str, k: int) -> int:
        # --method 1--
        # 因為這個方法在update count表的時候，一直需要for loop重算，這樣不是一個好方法 -> TLE
        """
        res = 0
        l = 0
        r = 0

        while r <= len(s):
            count = {}
            for char in s[l:r + 1]:
                if char not in count:
                    count[char] = 0
                count[char] = count[char] + 1

            max_count = count[max(count, key=lambda x: count[x])]

            if len(s[l:r + 1]) - max_count <= k:
                res = max(res, len(s[l:r + 1]))
                r = r + 1
            else:
                l = l + 1

        return res
        """

        # --method 2--
        # 使用slid window的方式去更新count表，也就是說一次只抓一個字元更新
        count = {}
        res = 0
        l = 0
        r = 0

        # r走到底 -> 最大的值也就決定了
        while r <= len(s):
            if not count:
                max_count = 0
            else:
                max_count = count[max(count, key=lambda x: count[x])]

            if len(s[l:r]) - max_count <= k:
                res = max(res, len(s[l:r]))
                prev_r = r
                r = r + 1
                # r向右移時，更新count table
                if s[prev_r: r] not in count:
                    count[s[prev_r: r]] = 0
                count[s[prev_r: r]] = count[s[prev_r: r]] + 1
            else:
                # l向右移時，更新count table
                prev_l = l
                l = l + 1
                count[s[prev_l: l]] = count[s[prev_l: l]] -1

        print(res)
        return res

    # hint
    # 跟meeting room一樣，要先對start time排序
    # 要特別處理overlap的問題，需要決定拿掉誰
    # 我自己寫了2種方法但想法都是接近neetcode
    # https://www.youtube.com/watch?v=nONCGxWoUfM
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        # method 1 -> 使用stack的方式，順便紀錄overlap的點
        result = []
        res_list = []
        # sorted_intervals = sorted(intervals, key=lambda x: x[0])
        sorted_intervals = sorted(intervals, key=lambda item: (item[0], item[1]))

        for interval in sorted_intervals:
            if not res_list:
                res_list.append(interval)
            else:
                # overlop的情況
                if interval[0] < res_list[-1][1]:
                    # 這是一個special case,overlap時需要判斷，那個要拿掉
                    # end在前的要保留，end在後的要拿掉 -> end比較小的要保留，end比較大的要拿掉
                    if interval[1] <= res_list[-1][1]:
                        result.append(res_list.pop())
                        res_list.append(interval)
                    else:
                        result.append(interval)
                else:
                    # 沒有overlap就繼續疊
                    res_list.append(interval)

        print(result)
        print(len(result))
        return len(result)

        # method 2 -> 不使用stack，只記overlap的次數，以及更新start/end值
        """
        res = 0
        res_list = []
        sorted_intervals = sorted(intervals, key=lambda item: (item[0], item[1]))

        for interval in sorted_intervals:
            if not res_list:
                res_list.append(interval)
            else:
                # 發生overlapping，end在前的要保留，end在後的要拿掉
                if interval[0] < res_list[-1][1]:
                    res = res + 1
                    if interval[1] <= res_list[-1][1]:
                        res_list[-1][0], res_list[-1][1] = interval[0], interval[1]
                else:
                    # 沒有overlap就繼續更新start/end的值，到下一個interval
                    res_list[-1][0], res_list[-1][1] = interval[0], interval[1]

        print(res)
        return res
        """

        # method 3 -> neetcode的方法
        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
        """

    # hint
    # 是用sameTree再加以改良 -> sameTree為重要的觀念題與工具題
    # https://www.youtube.com/watch?v=E36O5SWp-LE
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(r, s):
            # 為same tree的題目，same tree是個工具題
            # 2邊一起走，同時走到底，同時都是None表示有找到
            if r is None and s is None:
                return True

            # 2邊一起走，有一個沒有，表示樹不一樣
            if not r or not s:
                return False

            # root一樣，左樹以及右樹都一樣
            if r.val == s.val and dfs(r.left, s.left) and dfs(r.right, s.right):
                return True

        # root本身為root的子樹
        if not subRoot:
            return True
        if not root:
            return False
        # 最後一行不能帶dfs(root.left, subRoot) or dfs(root.right, subRoot) -> 那你就只會做一層而已也就是所謂的root的第一個左子樹和右子樹，但我們要判斷的是，所有的子樹，包含後面的好幾層
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # hint
    # 必須要熟悉回文的題目以及模板(longestPalindrome)
    # 先寫出判斷回文的funciton
    # 必須要知道有2種case，必須分成奇數跟偶數2種case
    # 可以看我的筆記或是影片
    # https://www.youtube.com/watch?v=4RACzI5-du8
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def is_palindrome(s, l_pointer, r_pointer):
            while (0 <= l_pointer and r_pointer < len(s) and s[l_pointer] == s[r_pointer]):
                l_pointer = l_pointer - 1
                r_pointer = r_pointer + 1
                self.res = self.res + 1

            return s[l_pointer + 1:r_pointer]

        # odd
        for i in range(len(s)):
            is_palindrome(s, i, i)

        # even
        for i in range(len(s)):
            is_palindrome(s, i, i+1)

        print(self.res)
        return self.res


if __name__ == '__main__':
    soultion = Solution()
    # soultion.twoSum([2, 7, 11, 15], 9)
    # soultion.lengthOfLongestSubstring("dvdf")
    # print(soultion.longestPalindrome("baaabad"))
    # soultion.maxArea([1,8,6,2,5,4,8,3,7])
    # soultion.threeSum([0,0,0,0])


    #ll = LinkedList()
    #ll.append(10)
    #ll.append(20)
    #ll.append(30)
    #print(ll.print())


    first_node = ListNode(1)
    second_node = ListNode(2)
    third_node = ListNode(3)
    fourth_node = ListNode(4)
    fifth_node = ListNode(5)

    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node

    #soultion.removeNthFromEnd(head=first_node, n=2)

    # soultion.isValid("]")

    """
    list1_first_node, list1_second_node, list1_third_node = ListNode(1), ListNode(2),  ListNode(4)
    list1_first_node.next = list1_second_node
    list1_second_node.next = list1_third_node

    list2_first_node, list2_second_node, list2_third_node = ListNode(1), ListNode(3), ListNode(4)
    list2_first_node.next = list2_second_node
    list2_second_node.next = list2_third_node

    soultion.mergeTwoLists(list1=list1_first_node, list2=list2_first_node)
    """

    #print(soultion.search([4,5,6,7,0,1,2], 0))
    #print(soultion.searchInsert([1,3,5,6], 2))
    #soultion.combinationSum([2,3,5], 8)
    #soultion.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    #soultion.groupAnagrams(strs = ["a"])
    #soultion.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])
    #soultion.spiralOrder(matrix = [[2,5,8],[4,0,-1]])
    #print(soultion.canJump(nums = [2,5,1]))
    #soultion.merge( intervals = [[1,3],[2,6],[8,10],[15,18]])
    #soultion.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
    #soultion.uniquePaths(m = 3, n = 7)
    #soultion.climbStairs(n = 6)
    #soultion.setZeroes( matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    #soultion.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
    #soultion.numDecodings(s = "12")

    list1_first_node, list1_second_node, list1_third_node, list1_fourth_node, list1_fifth_node = TreeNode(5), TreeNode(4), TreeNode(6), TreeNode(3), TreeNode(7)
    list1_first_node.left, list1_first_node.right = list1_second_node, list1_third_node
    list1_third_node.left, list1_third_node.right = list1_fourth_node, list1_fifth_node
    treenode_1 = list1_first_node

    list1_first_node, list1_second_node, list1_third_node = TreeNode(2), TreeNode(1), TreeNode(3)
    list1_first_node.left = list1_second_node
    list1_first_node.right = list1_third_node
    treenode_2 = list1_first_node

    list1_1_node, list1_2_node, list1_3_node, list1_4_node, list1_5_node, list1_6_node, list1_7_node = TreeNode(3), TreeNode(1), TreeNode(5), TreeNode(0), TreeNode(2), TreeNode(4), TreeNode(6)
    list1_1_node.left, list1_1_node.right = list1_2_node, list1_3_node
    list1_2_node.left, list1_2_node.right = list1_4_node, list1_5_node
    list1_3_node.left, list1_3_node.right = list1_6_node, list1_7_node
    treenode_3 = list1_1_node

    list1_1_node, list1_2_node = TreeNode(1), TreeNode(2)
    list1_1_node.left = list1_2_node
    treenode_4 = list1_1_node

    list1_1_node, list1_2_node = TreeNode(1), TreeNode(2)
    list1_1_node.right = list1_2_node
    treenode_5 = list1_1_node

    # soultion.isValidBST(root = treenode_3)
    # soultion.levelOrder(root = treenode_1)
    # soultion.maxDepth(root = treenode_1)
    # soultion.isSameTree( p = treenode_4, q = treenode_5)
    # soultion.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])

    #soultion.maxProfit(prices = [7,1,5,3,6,4])
    #soultion.longestConsecutive(nums = [100,4,200,1,3,2])
    #soultion.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
    #soultion.reorderList(head=first_node)
    #soultion.maxProduct(nums = [2,3,-2,4])
    #soultion.findMin(nums = [4,5,6,7,0,1,2])
    #soultion.reverseBits(n = 0b01000000000000000000000000000000)
    #soultion.hammingWeight(n = 0b01000000000000000000000000000000)
    #soultion.rob(nums = [2,7,9,3,1])
    """
    soultion.numIslands(grid = [["1","1","0","0","0"],
                                ["1","1","0","0","0"],
                                ["0","0","1","0","0"],
                                ["0","0","0","1","1"]
                        ])
    """
    #soultion.reverseList(head=first_node)
    #soultion.canFinish(numCourses = 5, prerequisites = [[0,1], [0,2], [1, 3], [1, 4], [3,4]])

    """
    trie = Trie()
    trie.insert("apple")
    """
    """
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mae")
    # wordDictionary.search(".ad")
    print(wordDictionary.search(".a"))
    """

    #soultion.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])
    #soultion.rob_2(nums = [2,3,2])
    #soultion.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])

    list1_1_node, list1_2_node, list1_3_node = TreeNode(2), TreeNode(1), TreeNode(3)
    list1_1_node.left = list1_2_node
    list1_1_node.right = TreeNode(3)

    list2_1_node, list_2_node = TreeNode(1), TreeNode(2)
    list2_1_node.left = list_2_node
    #soultion.invertTree(root = list2_1_node)

    list1_1_node, list1_2_node, list1_3_node, list1_4_node = TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(2)
    list1_1_node.left = list1_2_node
    list1_1_node.right = list1_3_node
    list1_2_node.right = list1_4_node
    # soultion.kthSmallest(root=list1_1_node, k = 1)

    list1_1_node, list1_2_node, list1_3_node = TreeNode(6), TreeNode(2), TreeNode(8)
    list1_1_node.left, list1_1_node.right = list1_2_node, list1_3_node
    list1_2_node.left, list1_2_node.right = TreeNode(0), TreeNode(4)
    list1_3_node.left, list1_3_node.right = TreeNode(7), TreeNode(9)

    # soultion.lowestCommonAncestor(root = list1_1_node, p = list1_2_node, q = list1_3_node)
    # soultion.productExceptSelf(nums = [1,2,3,4])
    # soultion.isAnagram(s = "anagram", t = "nagaram")
    # soultion.canAttendMeetings(intervals = [(0,30)])
    # soultion.minMeetingRooms(intervals = [(0,30), (5,10), (15,20)])
    # soultion.validTree(n=5, edges=[[0,1],[0,2],[0,3],[0,4]])
    # soultion.missingNumber(nums = [3,0,1])
    # soultion.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"])
    # soultion.alienOrder(words=["we", "ee", "we"])

    # encode = soultion.encode(["10#a#########b", "2#op"])
    # decode = soultion.decode(encode)

    """
    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    print(medianFinder.findMedian())   # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)  # arr[1, 2, 3]
    print(medianFinder.findMedian())   # return 2.0
    """

    """
    list1_first_node, list1_second_node, list1_third_node, list1_fourth_node, list1_fifth_node = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
    list1_first_node.left, list1_first_node.right = list1_second_node, list1_third_node
    list1_third_node.left, list1_third_node.right = list1_fourth_node, list1_fifth_node
    codec = Codec()
    tree_list = codec.serialize(list1_first_node)
    print(codec.deserialize(tree_list))
    """

    # soultion.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])
    # soultion.coinChange(coins = [1,2,5], amount = 11)
    # soultion.countComponents(n=5, edges = [[0,1],[1,2],[3,4]])
    # soultion.countBits(n=5)
    # soultion.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
    # soultion.getSum(a = 2, b = 3)

    # soultion.pacificAtlantic(matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    # soultion.characterReplacement(s = "AABABBA", k = 1)
    # soultion.eraseOverlapIntervals(intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])

    """
    root, node2, node3, node4, node5 = TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(2)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    subroot, subnode2, subnode3 = TreeNode(4), TreeNode(1), TreeNode(2)
    subroot.left, subroot.right = subnode2, subnode3
    soultion.isSubtree(root=root, subRoot=subroot)
    """
    soultion.countSubstrings(s = "aaab")