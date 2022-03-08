class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if all(i > j for i, j in zip(nums, nums[1:])):
            return nums.sort()
        if n==1:
            return nums
        if all(elem == nums[0] for elem in nums):
            return nums
        
        pivot=-100
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot==-100:
            return nums.sort()
        for j in range(n-1,-1,-1):
            if nums[j]>nums[pivot]:
                swapper=j
                break
        a=nums[pivot]
        nums[pivot]=nums[swapper]
        nums[swapper]=a
        nums[pivot+1:n] = sorted(nums[pivot+1:n])
  