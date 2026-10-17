class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        one, two = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            tmp = two
            two = max(one + nums[i], two)
            one = tmp
        m = two
        one, two = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            tmp = two
            two = max(one + nums[i], two)
            one = tmp
        return max(m, two)