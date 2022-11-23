#Time Complexity:: O(n)-all nodes are visited once
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of array
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()#To handle duplicate first we sort the array ( adjacent elements will be similar )
        self.backtrack(nums,0,[]) #create a backtrack function and initialize the index as 0 and current array as empty
        return self.result #return the result array
        
    def backtrack(self,nums,index,arr):
        self.result.append(arr[:]) #shallow copy the current array into the result array initially empty
        for i in range(index, len(nums)): #for each index of the nums array 
            if i != index and nums[i] ==nums[i-1]: #skip the duplicates, except for the first time by comparing index and i, while comparing the current and previous element as the nums array is sorted.
                continue #if this is the case continue
            #action
            arr.append(nums[i]) #include the element
            self.backtrack(nums,i+1,arr) #keep traversing to the next index
            #backtrack
            arr.pop() #remove the element from the current array once traversed
                