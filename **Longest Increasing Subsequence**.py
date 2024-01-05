question : https://leetcode.com/problems/longest-increasing-subsequence/submissions/1137838568/?envType=daily-question&envId=2024-01-05

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize an array to store the length of LIS ending at each index
        dp = [1] * len(nums)
        
        # Iterate through the array
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The length of the longest increasing subsequence is the maximum value in dp array
        return max(dp)
