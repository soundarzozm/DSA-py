class Solution:
	def groupAnagrams(self, strs):
		# Use hashmap to store lists of all unique anagrams
		hashMap = {}
		
		for word in strs:
			
			# Use an alphabet array of size 26 to store count of letters
			alphabets = [0]*26
			
			# Populate this array
			for letter in word:
				alphabets[ord(letter)-ord("a")] += 1
			
			# Since python cannot hash an array, we have to convert it into a tuple
			processedAlphabets = tuple(alphabets)

			# Populate the count of the tuple in the hashmap
			if processedAlphabets not in hashMap:
				hashMap[processedAlphabets] = []
			hashMap[processedAlphabets].append(word)
		
		return list(hashMap.values())

if __name__ == "__main__":
	solution = Solution()
	strs = ["eat","tea","tan","ate","nat","bat"]
	print(solution.groupAnagrams(strs))
