class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        arr = [1] * len(nums)
        for i in range(len(nums)):
            arr[i] *= left
            left *= nums[i]
            arr[len(nums)-1-i] *= right
            right *= nums[len(nums)-1-i]
        return arr