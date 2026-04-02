class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hs = set()
        len_hs = 0
        for i in nums:
            nums_hs.add(i)
            len_hs += 1
            if len(nums_hs) != len_hs:
                return True
        return False

