import re
#

def coordinatesFromFile(fileName):
    coordinates = []
    coordinateID = 0
    for coordinate in open(fileName, 'r'):
        coordinateID += 1
        coordinateXRegex = re.search('[0-9]*, ', coordinate)
        coordinateYRegex = re.search(', [0-9]*', coordinate)

        x = int(coordinateXRegex.group(0)[:-2].strip())
        y = int(coordinateYRegex.group(0)[2:].strip())

        coordinates.append((coordinateID, x, y))

    return coordinates


def loadMatrix(coordinates):
    maximumX = max([x for (_, _, x) in coordinates]) + 3
    maximumY = max([y for (_, y, _) in coordinates]) + 3

    matrix = [[-1 if y == 0 or x ==
               0 or x == maximumX-1 or y == maximumY-1 else 0 for y in range(maximumY)] for x in range(maximumX)]

    for (identifier, x, y) in coordinates:
        matrix[y+1][x+1] = identifier

    return matrix


def printMatrix(matrix):
    for line in matrix:
        print(line)


def printMatrixToFile(matrix, fileName):
    fabricFile = open(fileName, "w+")
    for line in matrix:
        fabricFile.write(str(line)+'\n')
    fabricFile.close()


def distanceFromPoint(point, coordinates):
    distances = []

    for (identifier, x, y) in coordinates:
        distances.append((identifier, abs(point[0]-y-1) + abs(point[1]-x-1)))

    return distances


def fillMatrix(matrix, coordinates):
    filledMatrix = matrix
    for point in [(x, y) for x in range(len(matrix)) for y in range(len(matrix[x])) if matrix[x][y] != -1]:

        distances = distanceFromPoint(point, coordinates)
        minimumDistance = min([distance for (_, distance) in distances])

        filteredDistances = [(identifier, coordinateNumber) for (
            identifier, coordinateNumber) in distances if coordinateNumber == minimumDistance]

        filledMatrix[point[0]][point[1]] = filteredDistances[0][0] if len(
            filteredDistances) == 1 else -2

    return filledMatrix


def findLargestFiniteArea(filledMatrix, coordinates):
    finiteIdentifiers = [identifier for (identifier, _, _) in coordinates]
    areas = {}
    for point in [(x, y) for x in range(len(filledMatrix)) for y in range(len(filledMatrix[x])) if filledMatrix[x][y] in finiteIdentifiers]:
        area = [
            filledMatrix[point[0]-1][point[1]],
            filledMatrix[point[0]][point[1]-1],
            filledMatrix[point[0]+1][point[1]],
            filledMatrix[point[0]][point[1]+1],
        ]

        if filledMatrix[point[0]][point[1]] not in areas:
            areas[filledMatrix[point[0]][point[1]]] = 0

        areas[filledMatrix[point[0]][point[1]]
              ] = areas[filledMatrix[point[0]][point[1]]] + 1

        if -1 in area and filledMatrix[point[0]][point[1]] in finiteIdentifiers:
            finiteIdentifiers.remove(filledMatrix[point[0]][point[1]])

    size = 0
    identifier = 0

    print(finiteIdentifiers)
    print(areas)

    for area in areas:
        if area not in finiteIdentifiers:
            areas[area] = -1

    identifier = max(areas, key=areas.get)
    size = areas[identifier]

    return (identifier, size)


def day5():
    coordinates = coordinatesFromFile('input.txt')
    matrix = loadMatrix(coordinates)
    printMatrixToFile(matrix, 'matrix.txt')

    filledMatrix = fillMatrix(matrix, coordinates)
    printMatrixToFile(filledMatrix, 'filledMatrix.txt')

    print(findLargestFiniteArea(filledMatrix, coordinates))


day5()
