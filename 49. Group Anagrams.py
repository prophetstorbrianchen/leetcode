class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        hash_table = {}
        res = []

        for string in strs:
            # 注意sorted(string) -> 會變list
            sorted_char_list = sorted(string)

            # 必須要再把各自的char再組起來
            sorted_string = ""
            for char in sorted_char_list:
                sorted_string = sorted_string + char
            if sorted_string not in hash_table:
                hash_table[sorted_string] = []
            hash_table[sorted_string].append(string)

        for sorted_sting, string_list in hash_table.items():
            res.append(string_list)

        print(res)
        return res

if __name__ == '__main__':
    solution = Solution()
    solution.groupAnagrams(strs = [""])