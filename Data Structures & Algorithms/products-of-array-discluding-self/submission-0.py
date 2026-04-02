class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods_pre = [1]
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            prods_pre.append(prod)

        prods_suff = [1]
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod *= nums[i]
            prods_suff.append(prod)

        res = []
        for i in range(len(nums)):
            res.append(prods_pre[i]*prods_suff[-(i+1)])

        return res