import collections


class Solution:
    # hint
    # 這題是在做Topological Sorting(拓樸排序)
    # 判断是否是DAG，且输出拓扑排序
    # 可和207一起看
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        # method 1: DFS解法的拓埔排序
        """
        # 建立圖形
        prereq = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # 有3種狀態
        # visited -> crs 已經被加入output
        # visiting -> crs 沒被加入output, 但被加入cycle
        # unvisited -> crs 沒被加入output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            # 有cycle -> 回傳False
            if crs in cycle:
                return False

            # 已經被加入output了，不必在拜訪第二次
            if crs in visit:
                return True

            # 非常熟悉的cycle作法，進入時先加入cycle，等到結束時再把cycle一層一層去掉
            # 若是進去的點在cycle的set中，那這個圖肯定有cycle
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            # 這個是為了防止外面的點重複在進來跑遞迴
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        print(output)
        return output
        """
        # method 2 -> BFS解法的拓埔排序
        # https://blog.csdn.net/liuliangcan/article/details/125567442
        # 算法描述：
        # 首先要对所有点初始化入度。（这一句非常重要，不要只计算在边上的点！一定要初始化图里所有点！）
        # 然后建图，计算每个点的入度。
        # 把入度为0的点加入队列。（其实就是有向图的起点，可能有多个，树(单源)的话只有一个）
        # 对队列进行遍历：取出队列中的点u，访问它所有相邻的孩子v，让v入度 - 1, 如果v的入度 == 0, 那可以放入队列，继续向后搜索。
        # 遍历完毕。如果有没遍历到的点，那这图存在环不是DAG。

        indegree = [0] * numCourses
        g = collections.defaultdict(list)
        # 反向給依賴
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
        return ans if len(ans) == numCourses else []


if __name__ == '__main__':
    solution = Solution()
    solution.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
