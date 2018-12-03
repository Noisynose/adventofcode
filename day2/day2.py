def codesFromFile(fileName):
    codes = []
    for code in open(fileName, 'r'):
        codes.append(code.rstrip())

    return codes


def numbersOfLetters(word):
    letters = {}
    for letter in word:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] = letters[letter] + 1

    return letters


def hasExactlyNIdenticalLetters(word, value):
    result = False
    letters = numbersOfLetters(word)

    for (_, numberOfOccurrences) in letters.items():
        if numberOfOccurrences is value:
            result = True
            break

    return result


def hasExactlyTwoIdenticalLetter(word):
    return hasExactlyNIdenticalLetters(word, 2)


def hasExactlyThreeIdenticalLetter(word):
    return hasExactlyNIdenticalLetters(word, 3)


def checksumFromInput(codes):
    identicalTwoLetters = 0
    identicalThreeLetters = 0

    for code in codes:
        if hasExactlyTwoIdenticalLetter(code):
            identicalTwoLetters += 1
        if hasExactlyThreeIdenticalLetter(code):
            identicalThreeLetters += 1

    return identicalTwoLetters * identicalThreeLetters


codesTest = codesFromFile('inputTest.txt')
codes = codesFromFile('input.txt')

checksum = checksumFromInput(codes)
print(checksum)
