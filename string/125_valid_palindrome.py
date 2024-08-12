class Solution:
    def isPalindrome(self, s):
        processedString = ""

        # First we process the string by removing the non-alphanumeric characters
        # and converting them to lowercase
        for char in s:
            if char.isalnum():
                processedString += char.lower()
        
        # Initialize left and right pointers
        l = 0
        r = len(processedString) - 1

        # Move both pointers at the same time and keep comparing
        # They should always be equal in case of a palindrome
        while l < r:
            if processedString[l] != processedString[r]:
                return False
            l += 1
            r -= 1
        
        return True

if __name__ == "__main__":
    solution = Solution()
    string = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(string))