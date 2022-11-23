#Time Complexity:: O(2^n)-all nodes are visited multiple times in the tree recursively
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of array and using a collections
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.letter_count = collections.Counter(tiles) #create a collection of all the occurances of each letter
        return self.dfs() #return the return value from the dfs function
    
    def dfs(self):
        count = 0 #initialize the count of possible tiles to be 0
        for tile in self.letter_count: #for each tile in the collection
            if self.letter_count[tile] == 0: #if the number of occurances of specific tile is zero then continue
                continue
            #action
            self.letter_count[tile] -= 1 #decrement the count of that tile from the occurances hashmap
            count += self.dfs() + 1 #recursively call the dfs witht the current use of tiles(+1) and assign the return type to the total number tiles
            #backtrack
            self.letter_count[tile] += 1 
        return count   #returnt the total current count