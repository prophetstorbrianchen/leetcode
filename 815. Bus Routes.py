import collections


class Solution:
    # hint
    # 使用set去記route，再由route找stop。而非直接找bus stop
    # 有2個cache -> 1.visit, 2.走完一整個route就清掉，防下次再走toute
    def numBusesToDestination(self, routes: [[int]], source: int, target: int) -> int:
        # method 1 -> 答案對的，但是TLE
        """
        # 做表 -> 有可能是這邊太慢，要用的3個for loop
        graph = collections.defaultdict(list)
        for item in routes:
            for bus_th in item:
                for i in item:
                    if i != bus_th:
                        graph[bus_th].append(i)

        # BFS
        q = collections.deque()
        visit = set()
        q.append((source, 0))
        visit.add(source)

        while q:
            bus_th, path = q.popleft()
            if target == bus_th:
                print(path)
                return path
            else:
                for item in graph[bus_th]:
                    if item not in visit:
                        q.append((item, path + 1))
                        visit.add(item)
                graph[bus_th] = []
        return -1
        """

        # method 2 -> 前面使用set去做，而不使用list
        # 使用set去減低BFS搜尋的次數
        graph = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                graph[j].add(i)

        # BFS
        q = collections.deque()
        visit = set()
        q.append((source, 0))
        visit.add(source)

        while q:
            stop, bus = q.popleft()
            if stop == target:
                return bus

            # 先去找route -> 從route中去loop bus th -> loop完之後要整個清掉，避免下一次重走(cache)
            for i in graph[stop]:
                for j in routes[i]:
                    if j not in visit:
                        q.append((j, bus + 1))
                        visit.add(j)

                # 全部歷遍就清掉 -> 下次就不會再走 -> 另類的cache
                routes[i] = []  # seen route

        return -1


if __name__ == '__main__':
    solution = Solution()
    solution.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)