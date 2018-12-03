def codesFromFile(fileName):
    codes = []
    for code in open(fileName, 'r'):
        codes.append(code.rstrip())

    return codes


def numberOfDifferentCharactersAtTheSamePosition(word, wordToCompare):
    numberOfDifferentCharactersAtTheSamePosition = 0

    for index in range(0, len(word)):
        if word[index] is not wordToCompare[index]:
            numberOfDifferentCharactersAtTheSamePosition += 1

    return numberOfDifferentCharactersAtTheSamePosition


def findWordsThatDiffersByExactlyOneCharacter(codes):

    found = False
    for index in range(0, len(codes)):
        wordToCompareFrom = codes[index]

        for code in codes[index+1:]:
            differences = numberOfDifferentCharactersAtTheSamePosition(
                wordToCompareFrom, code)

            if differences is 1:
                found = True
                wordFound = code
                break

        if found:
            break

    return [(wordToCompareFrom, wordFound)]


def commonLetters(words):
    indexToRemove = 0
    for (word, wordToCompare) in words:
        for index in range(0, len(word)):
            if word[index] is not wordToCompare[index]:
                indexToRemove = index
                break

        commonLetters = word[:indexToRemove]+word[indexToRemove+1:]

    return commonLetters


codesTest = codesFromFile('inputTest_part2.txt')
codes = codesFromFile('input.txt')

words = findWordsThatDiffersByExactlyOneCharacter(codes)
print(words)

result = commonLetters(words)
print(result)
