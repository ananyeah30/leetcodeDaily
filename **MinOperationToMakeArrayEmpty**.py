question : https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/?envType=daily-question&envId=2024-01-04

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        for i in nums:
            mp[i]+=1
        ans=0
        for i in mp.values():
            if i==1:
                return -1
            ans+=(i+2)//3
            
        return ans     
