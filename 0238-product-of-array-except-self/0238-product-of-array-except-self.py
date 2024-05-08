class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        # left
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1

        # right
        for i in range(len(nums)-1, 0-1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out