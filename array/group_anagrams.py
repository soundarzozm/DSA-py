def solution(arr):
    anagramMap = {}
    result = []

    for word in arr:
        sortedWord = ""
        sortedWordArray = sorted(word)

        for letter in sortedWordArray:
            sortedWord += letter

        if sortedWord in anagramMap:
            anagramMap[sortedWord].append(word)
        else:
            anagramMap[sortedWord] = [word]

    for word in anagramMap:
        result.append(anagramMap[word])

    return result

if __name__ == "__main__":
    arr = ["eat","tea","tan","ate","nat","bat"]
    print(solution(arr))
