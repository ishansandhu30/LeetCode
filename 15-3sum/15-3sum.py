class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums = sorted(nums)
        
       
       
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            right = len(nums) - 1
            target = nums[i]
            left =i+1
            while left<right:
                if (target + nums[left] + nums[right]) == 0:
                    arr.append([target,nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif (target + nums[left] + nums[right]) > 0:
                    right-=1
                elif (target + nums[left] + nums[right]) < 0:
                    left+=1

        return arr