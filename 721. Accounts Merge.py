import collections


class Solution:
    # hint
    # 理解建圖
    # 理解DFS
    # 理解DFS使用stack來取代
    # https://www.youtube.com/watch?v=f17PKE8W2p8
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        graph = collections.defaultdict(set)
        email_to_name = {}

        # 建圖
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)

                email_to_name[email] = name

        print(graph)

        res = []
        visited = set()

        for email in graph:
            if email not in visited:
                # 用stack取代dfs function
                stack = [email]
                visited.add(email)

                # 把所有同一個account的mail統一成一個
                # 一層一層往下帶，只是這個是stack，而非DFS function
                local_res = []
                while stack:
                    node = stack.pop()
                    local_res.append(node)

                    for edge in graph[node]:
                        if edge not in visited:
                            stack.append(edge)
                            visited.add(edge)

                # mail需要做字典排序
                res.append([email_to_name[email]] + sorted(local_res))

        return res


if __name__ == '__main__':
    solution = Solution()
    solution.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])