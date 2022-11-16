class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        # method 1 - 暴力解
        """
        # extend gas and cost
        new_gas = gas + gas
        new_cost = cost + cost

        start_station_index = []
        end_station_index = []
        for i in range(len(gas)):
            start_station_index.append(i)
            end_station_index.append(i + len(gas))

        # 每個station都要run過，有成功走回自己的點就可以結束
        start = 0
        while start < len(gas):
            total_gas = 0
            count = 0
            for i in range(start_station_index[start], end_station_index[start]):
                total_gas = total_gas + new_gas[i] - new_cost[i]
                if total_gas < 0:
                    continue
                else:
                    count = count + 1
            if count == len(gas):
                print(start)
                return start

            start = start + 1

        print(-1)
        return -1
        """

        """
        # extend gas and cost
        new_gas = gas + gas
        new_cost = cost + cost

        start_station_index = []
        end_station_index = []
        diff_index = []
        for i in range(len(gas)):
            start_station_index.append(i)
            end_station_index.append(i + len(gas))

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if diff >= 0:
                diff_index.append(i)

        # 每個只要跑正數或是0的diff station，有成功走回自己的點就可以結束
        for item in diff_index:
            total_gas = 0
            count = 0
            for i in range(start_station_index[item], end_station_index[item]):
                total_gas = total_gas + new_gas[i] - new_cost[i]
                if total_gas < 0:
                    continue
                else:
                    count = count + 1
            if count == len(gas):
                print(item)
                return item

        print(-1)
        return -1
        """

        # 這種情況必定走不到
        if sum(gas) < sum(cost):
            return -1

        # 下面肯定走的到，但要知道是哪個當start
        # get diff gas for every station
        diff_gas = []
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            diff_gas.append(diff)

        total = 0
        start = 0

        # 使用total小於0的時候來判斷 -> 這個做法可能要背一下
        for i in range(len(gas)):
            total = total + diff_gas[i]

            if total < 0:
                total = 0
                start = i + 1

        print(start)
        return start

    def canCompleteCircuit_2(self, gas: [int], cost: [int]) -> int:
        # 他的station是從0開始一直到n
        # 先判斷是不是能夠走完
        if sum(gas) - sum(cost) < 0:
            return -1

        # 下面是一定可以走完的情況，但要從哪個station開始走?
        # 先算出gas和cost的diff
        diff_list = []

        for g, c in zip(gas, cost):
            diff = g - c
            diff_list.append(diff)

        # 若為負 -> 不可能為起點; 若為正 -> 有機會，但必須走到後面都不能變為負
        start = 0
        total = 0
        for i, n in enumerate(diff_list):
            total = total + n

            if total < 0:
                # 需要重算
                total = 0
                # **這邊可以看筆記**
                start = i + 1

        print(start)
        return start


if __name__ == '__main__':
    solution = Solution()
    solution.canCompleteCircuit_2(gas = [1,2,3,4,5], cost = [3,4,5,1,2])