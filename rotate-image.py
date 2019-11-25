'''

https://leetcode.com/problems/rotate-image/

'''

class Solution:
    """
    In order to rotate the outer layer of a matrix purely in-place, we need to do a 4-way swap, starting with the
    four corners, and then swap the four values that are one element inwards from the corners, then
    swap the four values two elements inward, etc., until we've swapped all the values in that outer layer.
    Then we need to move to the next layer and do the same, until we've swapped a layer that is 3x3 or 2x2, in
    which either case, the full matrix has been rotated 90 degrees, since after the outer layer of a 3x3,
    there's only the middle element left, which doesn't need rotating. 

    If we look at the size of the matrix, we can see that the number of layer rotations needed is the number of 
    times 2 divides evenly into the size. A 2x2 and a 3x3 need 1 rotation, a 4x4 and a 5x5 need 2 rotations, 
    a 6x6 and a 7x7 need 3 rotations, etc. Thus, we find out how many rotations are needed, and specify a start
    and end variable, which determine which layer we are rotating. Then we iterate through the indices of each
    element in that layer and perform the 4-way swap.

    Note that in order to correctly index into the bottom-right or bottom-left corner, we need to make sure our
    index going from the end to start is set to (end-(i-start)), since we don't want to be moving inwards when
    i is starting at a value other than 0 for the first iteration. There might be a better way to handle this.

    Swap Logic:
    First row -> Last Column: matrix[start][i] -> matrix[i][end]
    Last Column -> Last Row:  matrix[i][end] -> matrix[end][end-(i-start)]
    Last Row -> First Column: matrix[end][end-(i-start)] -> matrix[end-(i-start)][start]
    First Column-> First Row: matrix[end-(i-start)][start] -> matrix[start][i]
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return []
        n = len(matrix)
        rotations = n // 2
        s, e = 0, n-1
        for _ in range(rotations):
            for i in range(s,e):
                matrix[s][i], matrix[i][e], matrix[e][e-(i-s)], matrix[e-(i-s)][s] = \
                matrix[e-(i-s)][s], matrix[s][i], matrix[i][e], matrix[e][e-(i-s)]
            s += 1
            e -= 1
        return matrix
	

