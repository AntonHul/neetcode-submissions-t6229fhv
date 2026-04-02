class Solution:
    def search(self, nums, target) -> int:
        low = 0
        high = len(nums)-1
        mid = (high + low) // 2
        while low <= high:
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                high = mid -1
            else: 
                low = mid + 1
            mid = (high + low) // 2
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_num = len(matrix)
        i = 0
        while i < rows_num:
            if matrix[i][0] <= target and target <= matrix[i][-1]:
                if self.search(matrix[i], target):
                    return True
            i+=1

        return False