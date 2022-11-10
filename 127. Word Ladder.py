import collections


class Solution:
    # 新題型的BFS -> 文字型轉成圖的BFS
    # https://www.youtube.com/watch?v=h9iTnkgv05E
    # https://www.youtube.com/watch?v=h9iTnkgv05E
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        # edge case
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        # 此題的重點在做graph出來
        for word in wordList:
            for j in range(len(word)):
                # 做出每種patter，其中的一個字都是用*取代
                # hot -> *ot/h*t/ho*
                pattern = word[:j] + "*" + word[j + 1:]
                # 開始做表(圖) -> 之後可用BFS traverse
                nei[pattern].append(word)

        # BFS模板
        visit = set()
        # 第一個進queue的，就也要進visit
        visit.add(beginWord)
        q = collections.deque()
        q.append((beginWord, 1))
        while q:
            for i in range(len(q)):
                word, number = q.popleft()
                # 找到了，直接回傳
                if word == endWord:
                    print(number)
                    return number
                # 假設是找hit -> 往下找hot
                # 要記得這種字典的for迴圈處理BFS的方式 -> 往下層找的方式
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append((neiWord, number + 1))

        return 0


if __name__ == '__main__':
    solution = Solution()
    solution.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])