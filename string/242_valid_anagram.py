class Solution:
    def isAnagram(self, s, t):
        characterCount = {}

        for char in s:
            if char not in characterCount:
                characterCount[char] = 0
            characterCount[char] += 1

        for char in s:
            if char not in characterCount:
                return False
            characterCount[char] -= 1

        for char in characterCount:
            if characterCount[char] != 0:
                return False

        return True

if __name__ == "__main__":
    solution = Solution()
    string = ""
    target = ""
    print(solution.isAnagram(string, target))
