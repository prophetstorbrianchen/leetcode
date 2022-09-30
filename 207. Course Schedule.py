class Solution:
    # hint
    # 這題忘光了，需要看影片重新筆記
    # 這題是有方向性的圖
    # 不過dict map的模板大概就是長這樣
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


if __name__ == '__main__':
    solution = Solution()
    solution.canFinish(numCourses = 5, prerequisites = [[0,1], [0,2], [1, 3], [1, 4], [3,4]])