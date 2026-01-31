# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if len(nestedList) == 0:
            return 0     

        maxDepth = 1
        
        def calculateDepth(num_list, level):
            nonlocal maxDepth
            temp_ans = 0
            for i in range(len(num_list)):
                if not num_list[i].isInteger():
                    temp_level = level+1
                    calculateDepth(num_list[i].getList(), level+1)
                    maxDepth = max(maxDepth, temp_level)            

        def calculateSum(num_list, level):
            nonlocal maxDepth
            temp_ans = 0
            for i in range(len(num_list)):
                if not num_list[i].isInteger():
                    temp_ans += calculateSum(num_list[i].getList(), level+1)
                elif num_list[i].isInteger():
                    temp_ans += (maxDepth - level + 1) * num_list[i].getInteger()
            return temp_ans

        
        calculateDepth(nestedList, 1)
        
        return calculateSum(nestedList, 1)  