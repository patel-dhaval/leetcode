"""
Clarifying questions
- unique inputs?
- len of input
- min size of m and n, 
Edge cases

m = 1, n=1
compare the element, can directly compare the element, no need to run the loop

in general, compare with first and last elements with the target, if the value lies outside these bounds then return false immediately

Approach
Idea would be to ideally convert the 2-D matrix into 1-D array, so that search becomes easy
This can be inferred from the fact that the values are in non-decreasing order, and the values at the end of prev row is smaller than the first element of the next row. 
Thus, considering this to be a contiguous array is feasible

Start with 2 pointers, L and R, and calculate the midpoint of this.
Now, to calculate the row and col of this particular midpoint is a challenge
row would be division of the mid value and the cols, this it to find how many complete rows can be included in the midpoint
col would be modulus of the mid value and the cols, this will find the exact place within the incomplete row where the element is
Once the mid value is retreves, compare and check if the target is larger or smaller
On the basis of that the pointer needs to be shifted and we keep doing this till either the value is found or L < R.

Return

Code



Dry run

TC and SC

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row = len(matrix)
        Col = len(matrix[0])
        L, R = 0, (Row * Col) - 1

        if Row == 1 and Col == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False

        while L <= R:
            middle_element_index = (L + R)//2
            row = middle_element_index//Col
            col = middle_element_index%Col
            mid = matrix[row][col]

            if mid > target:
                R = middle_element_index - 1
            elif mid < target:
                L = middle_element_index + 1
            else:
                return True
        
        return False

