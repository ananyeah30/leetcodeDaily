
Valid Palindrome :https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase=s.lower()
        my_list=[]
        for char in lowercase:
            if char.isalnum():
                my_list.append(''.join(char))
        print()
        return my_list==my_list[::-1]
