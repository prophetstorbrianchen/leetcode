import collections


class Solution:
    # hint
    # 這題忘光了，需要看影片重新筆記
    # 這題是有方向性的圖
    # 不過dict map的模板大概就是長這樣
    # 访问完整个图，即图是否DAG
    # 可和210一起看
    # 使用BFS做一次
    # https://blog.csdn.net/liuliangcan/article/details/125567442
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        def dfs(crs):
            # --base case--
            # 其是進這個case表示有cycle了
            if crs in visiting:
                return False

            # 代表已走到終點，需要回上層了
            if preMap[crs] == []:
                return True

            # 有走訪到而且能繼續往下走
            visiting.add(crs)

            # map的走訪模板就是長這樣
            # 走訪完之後，list清掉
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # --下面為true的情況才做--
            visiting.remove(crs)

            # 走訪完就要設為空，防止重走
            preMap[crs] = []
            return True

        # 建立map
        preMap = {i: [] for i in range(numCourses)}

        # 做出preMap這張表
        # 這張preMap是有方向性的
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        # 每個點都走訪
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

    def canFinish_2(self, numCourses: int, prerequisites: [[int]]) -> bool:
        def dfs(node):
            # base case
            if graph_dict[node] == []:
                return True

            # 有cycle
            if node in visit:
                return False

            # 準備進下一層
            visit.add(node)
            for n in graph_dict[node]:
                # 檢查有無cycle
                if not dfs(n):
                    return False

            visit.remove(node)

            # 走訪完就要設為空，讓最外面的迴圈可以不用每次都重作 -> 有點類似島嶼數量納提的概念
            # **沒有這行會TLE，這非常重要**
            graph_dict[node] = []
            return True

        # 有向圖的table
        graph_dict = {}
        for i in range(numCourses):
            if i not in graph_dict:
                graph_dict[i] = []

        for item in prerequisites:
            graph_dict[item[0]].append(item[1])

        visit = set()
        for i in range(numCourses):
            # 使用dfs看有無cycle
            if not dfs(i):
                print(False)
                return False
        print(True)
        return True

    def canFinish_3(self, numCourses: int, prerequisites: [[int]]) -> bool:
        # BFS
        # 有向無環圖 -> ACG -> Topology sort
        # 算法描述：
        # 首先要对所有点初始化入度。（这一句非常重要，不要只计算在边上的点！一定要初始化图里所有点！）
        # 然后建图，计算每个点的入度。
        # 把入度为0的点加入队列。（其实就是有向图的起点，可能有多个，树(单源)的话只有一个）
        # 对队列进行遍历：取出队列中的点u，访问它所有相邻的孩子v，让v入度 - 1, 如果v的入度 == 0, 那可以放入队列，继续向后搜索。
        # 遍历完毕。如果有没遍历到的点，那这图存在环不是DAG。

        indegree = [0] * numCourses
        g = collections.defaultdict(list)
        # 反向給依賴(因為是看入度的數量，會跟DFS往下走的會相反)
        # [[1,0],[2,0],[3,1],[3,2]] -> DFS: {0: [], 1: [0], 2:[0], 3:[1,2]}
        # [[1,0],[2,0],[3,1],[3,2]] -> BFS: {0: [1,2], 1: [3], 2:[3], 3:[]} or {0: [1,2], 1: [3], 2:[3]} -> node3直接不寫
        for a, b in prerequisites:
            # 建圖
            g[b].append(a)
            # 入度的數量
            indegree[a] = indegree[a] + 1

        # 入度為0的放入queue中
        tmp_list = []
        for i, v in enumerate(indegree):
            if v == 0:
                tmp_list.append(i)

        q = collections.deque(tmp_list)
        ans = []

        while q:
            u = q.popleft()
            # 開始放入拓埔排序 -> 做出拓埔排序的路徑 -> 並不是唯一解
            ans.append(u)
            for v in g[u]:
                indegree[v] = indegree[v] - 1
                # 入度為0才能進queue再重新一次loop
                if indegree[v] == 0:
                    q.append(v)

        # 若是所有的點都有在ans中 -> 沒有cycle，反之就是有cycle
        return True if len(ans) == numCourses else False


if __name__ == '__main__':
    solution = Solution()
    solution.canFinish_3(numCourses = 5, prerequisites = [[0,1], [0,2], [1, 3], [1, 4], [3,4]])
