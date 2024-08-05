class Solution:
    def groupAnagrams(self, strs):
        hashMap = {}

        for str in strs:

            # This is going to be the key in the hashMap
            countArray = [0] * 26

            # Populate the countArray (This will be the same for anagrams)
            for char in str:
                countArray[ord(char) - ord("a")] += 1

            # Add the strings to the hashMap based on countArray as the key
            if countArray not in hashMap:
                hashMap[countArray] = []
            hashMap[countArray].append(str)

        return hashMap.values()

if __name__ == "__main__":
    solution = Solution()
    strs = [""]
    print(solution.groupAnagrams(strs))
