#Time Complexity:: O(2^n)-all nodes are visited multiple times in the tree
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of array
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = [] # create a result array to store the different ip addresses
        self.dfs(s, 0, "", res)#create a recursive dfs function to process each path
        return res #return the result array
    
    def dfs(self, s, idx, path, res):
        if idx > 4: #if the index is greater than 4 return as the max segments an ip address can have is 4
            return 
        
        if idx == 4 and not s: #if index is 4 and it's not the entire given string ie. '1111'
            res.append(path[:-1]) #add it to the resuult array and retunr
            return 
        
        for i in range(1, len(s)+1): #run  a for loop to check each possible segment with the given original string
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256): #check the octets values
                self.dfs(s[i:], idx+1, path+s[:i]+".", res) #recall the dfs function  recursively while passing the new index as +1 and changing the path