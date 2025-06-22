class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        p_1 = nums[0]*nums[1]*nums[-1]
        p_2 = nums[-1]*nums[-2]*nums[-3]
        return max(p_1, p_2)