class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums  == []:
            return 0 
        list_nums = set(nums)
        k = 1 
        j = 1
        if len(list_nums) == 1:
            return 1 
        for i in list_nums:
            if i - 1 not in list_nums:
                k = 1
                while i + k in list_nums:
                    k += 1
                j = max(j, k)
                if j > len(list_nums) // 2:
                    return j 
        return j 