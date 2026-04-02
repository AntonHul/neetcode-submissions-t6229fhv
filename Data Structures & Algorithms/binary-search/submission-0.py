class Solution:

    def search(self, nums, target) -> int:
        low = 0
        high = len(nums)-1
        mid = (high + low) // 2
        while low <= high:
            print(mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid -1
            else: 
                low = mid + 1
            mid = (high + low) // 2
        return -1

        