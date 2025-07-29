class Solution:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()

# Test the function
sol = Solution()

# Example test cases
print(sol.detectCapitalUse("USA"))       
print(sol.detectCapitalUse("Google"))    
print(sol.detectCapitalUse("leetcode"))  
print(sol.detectCapitalUse("FlaG")) 
