


https://leetcode.com/problems/climbing-stairs/submissions/1150032110/?envType=daily-question&envId=2024-01-18
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 1

        for i in range(1, (n // 2) + 1):
            product = 1

            for j in range(i, 2 * i):
                product *= (n - j) / (j - i + 1)

            ways += product

        return int(ways)
