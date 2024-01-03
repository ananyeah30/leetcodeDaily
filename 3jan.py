question:  Determine Color of a Chessboard Square : https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter=coordinates[0]
        num=int(coordinates[1])
        def ascii(letter)->int:
            return ord(letter)
        if 1<=num<=8 and ascii("a")<=ascii(letter)<=ascii("h"):
            if (num+ascii(letter))%2==0:
                return False
            else:
                return True
