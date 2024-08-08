class Solution:
    def encode(self, strings):
        encodedString = ""

        # We added length to the beginning to keep track of where to break the string
        # We need # becuase we cannot tell if the length is more than single-digit
        for string in strings:
            encodedString += str(len(string)) + "#" + string
        
        return encodedString
    
    def decode(self, string):
        decodedStrings = []
        start = 0

        # Start will have the starting index of each word (including the metadata we added)
        while start < len(string):
            pointer = start

            # We first parse the length
            while string[pointer] != "#":
                pointer += 1

            # We convert the length to integer for processing
            length = int(string[start : pointer])

            # Currently the pointer is at #
            # So we need to take the string from the next index to the length of the word
            decodedStrings.append(string[pointer + 1 : pointer + 1 + length])
            
            # We move start to the next word
            start = pointer + 1 + length

        return decodedStrings
    
if __name__ == "__main__":
    solution = Solution()
    strings = ["we","say",":","yes","!@#$%^&*()"]
    encodedString = solution.encode(strings)
    print(encodedString)
    decodedStrings = solution.decode(encodedString)
    print(decodedStrings)