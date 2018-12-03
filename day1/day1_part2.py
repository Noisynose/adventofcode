def variationsFromFile(fileName):
    variations = []
    for variation in open(fileName, 'r'):
        variations.append(int(variation))

    return variations

# day1_part1


def totalFrequency(variations):
    frequency = 0
    for variation in variations:
        frequency += variation

    return frequency

# day1_part2


def applyFrequenciesTwice(variations):
    frequency = 0
    for variation in variations+variations:
        frequency += variation

    return frequency


def findFirstSecondFrequency(variations, numberOfIterations):
    frequency = 0
    frequencies = [0]
    found = False

    for _ in range(1, numberOfIterations):
        for variation in variations:

            frequency += variation

            if frequency in frequencies:
                found = True
                break

            frequencies.append(frequency)

        if found:
            break

    return frequency


variations = variationsFromFile('input.txt')
# print(variations)
endFrequency = totalFrequency(variations)
# print(endFrequency)
firstSecondFrequency = findFirstSecondFrequency(variations, 200)
print(firstSecondFrequency)
