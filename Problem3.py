'''## Problem 3
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:

[

[ 1, 2, 3 ],

[ 4, 5, 6 ],

[ 7, 8, 9 ]

]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:

[

[1, 2, 3, 4],

[5, 6, 7, 8],

[9,10,11,12]

]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    '''

class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        res = []
        
        left, right, top, bottom = 0, n - 1, 0, m - 1
        
        while left <= right and top <= bottom:
            # Traverse from left to right.
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            
            # Traverse downwards.
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left.
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            
            if left <= right:
                # Traverse upwards.
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
        
        return res

sol = Solution()
matrix = [

[ 1, 2, 3 ],

[ 4, 5, 6 ],

[ 7, 8, 9 ]

]
print(sol.spiralOrder(matrix))
