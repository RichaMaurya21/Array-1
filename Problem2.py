'''## Problem 2

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[

[ 1, 2, 3 ],

[ 4, 5, 6 ],

[ 7, 8, 9 ]

]
Output: [1,2,4,7,5,3,6,8,9]
'''

class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        res = []
        r, c = 0, 0
        flag = True  # Initialize the flag

        for i in range(m * n):
            res.append(mat[r][c])
            if flag:  # Moving up
                if c == n - 1:  # Hit the right boundary
                    r += 1
                    flag = False
                elif r == 0:  # Hit the top boundary
                    c += 1
                    flag = False
                else:
                    r -= 1
                    c += 1
            else:  # Moving down
                if r == m - 1:  # Hit the bottom boundary
                    c += 1
                    flag = True
                elif c == 0:  # Hit the left boundary
                    r += 1
                    flag = True
                else:
                    r += 1
                    c -= 1

        return res



sol = Solution()
mat = [

[ 1, 2, 3 ],

[ 4, 5, 6 ],

[ 7, 8, 9 ]

]
print(sol.findDiagonalOrder(mat))



        