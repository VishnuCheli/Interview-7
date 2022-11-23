#Time Complexity:: O(n*target)-depending on the no. of numbers given and target sum
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of nums array
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums=nums #make the nums variable an attribute of the self object
        return self.dfs(0, target) #call and return the dfs function's return type
    
    def dfs(self,i, target):
        if i == len(self.nums): #the index is checked if it is the last index of the nums array
            return 1 if target == 0 else 0 #if target is 0 return 1, otherwise return 0
        return self.dfs(i + 1, target + self.nums[i]) + self.dfs(i+1, target - self.nums[i]) #traverse both combinations where you add and subtract from the current sum, then return the total of that expressions.