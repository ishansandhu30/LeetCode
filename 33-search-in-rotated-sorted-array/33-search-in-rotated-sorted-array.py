class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        if target <= max(nums) and target >= nums[0]:
            right = nums.index(max(nums))
            left = 0
        else:
            right = len(nums) -1 
            left = nums.index(max(nums)) +1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid +1
            elif nums[mid] == target:
                return nums.index(nums[mid])
            else:
                return -1
        return -1