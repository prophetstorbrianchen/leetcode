import heapq


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        hash_table = {}
        heap = []
        res = []

        # 建立dict
        for n in nums:
            if n not in hash_table:
                hash_table[n] = 0
            hash_table[n] = hash_table[n] + 1

        for n, count in hash_table.items():
            # 建立max的heap
            heapq.heappush(heap, (-1 * count, n))

        # 對max heap做pop -> 做k次
        for i in range(k):
            count, n = heapq.heappop(heap)
            count = count * (-1)
            print(n, count)
            res.append(n)

        return res


if __name__ == '__main__':
    solution = Solution()
    solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2)