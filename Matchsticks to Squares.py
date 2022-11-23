#Time Complexity:: O(n) - all match sticks are traversed 
#Space Complexity:: O(n) - an array is created to store the matchsticsk used for each side 
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        self.length = sum(matchsticks) // 4 #default length each side of the square should have-usually the lenght of the longest matchstick
        sides = [0] * 4  #an array is created to store the match sticks for each side
        if sum(matchsticks) / 4 != self.length: #if the square can be built without breaking a matchstick-checking if divideing by four gives a decimal
            return False
        matchsticks.sort(reverse=True) #sort the matchsticks in reverse ordeer
        self.matchsticks = matchsticks #declaring matchsticks as a global variable
        return self.backtrack(0,sides) #returning the return value of the backtrack function
    
    def backtrack(self,i,sides): #creating a recursive function
            if i == len(self.matchsticks): #if all matchsticks have been used to create the square then return True
                return True
            for j in range(4): #for each side of the matchstick
                if sides[j] + self.matchsticks[i] <= self.length: #if the side and the new matchstick have a combined length less than one sides max length
                    sides[j] += self.matchsticks[i] #then add the matchsticsk to that side
                    if self.backtrack(i + 1,sides): #after adding the matchstick call recursion for adding the next matchstick
                        return True
                    sides[j] -= self.matchsticks[i] #once the for loop for each side has been completed remove the matchstick and return
            return False #return false once the recursion is complete without using a matchsticks