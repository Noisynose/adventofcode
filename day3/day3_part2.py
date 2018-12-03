import re


def claimsFromFile(fileName):
    claims = []
    for claim in open(fileName, 'r'):
        claimIDRegex = re.search('#[0-9]* @', claim)
        claimLeftEdgeRegex = re.search('@ [0-9]*,', claim)
        claimTopEdgeRegex = re.search(',[0-9]*:', claim)
        claimRectangleWidthRegex = re.search(': [0-9]*x', claim)
        claimRetangleTallRegex = re.search('x[0-9]*', claim)

        claimID = claimIDRegex.group(0)[1:-1].strip()
        claimLeftEdge = claimLeftEdgeRegex.group(0)[1:-1].strip()
        claimTopEdge = claimTopEdgeRegex.group(0)[1:-1].strip()
        claimRectangleWidth = claimRectangleWidthRegex.group(0)[1:-1].strip()
        claimRetangleTall = claimRetangleTallRegex.group(0)[1:].strip()

        claims.append({'id': claimID, 'left': claimLeftEdge, 'top': claimTopEdge,
                       'width': claimRectangleWidth, 'tall': claimRetangleTall})

    return claims


def loadClaims(claims, matrixWidth):
    fabric = [[([], 0) for x in range(matrixWidth)]
              for x in range(matrixWidth)]

    for claim in claims:
        column = int(claim['left'])
        line = int(claim['top'])
        claimID = int(claim['id'])

        for i in range(line, line + int(claim['tall'])):
            for j in range(column, column + int(claim['width'])):
                claimIDs = fabric[i][j][0]
                claimIDs.append(claimID)
                fabricAmount = fabric[i][j][1] + 1
                fabric[i][j] = (claimIDs, fabricAmount)

    return fabric


def printFabric(fabric):
    for line in fabric:
        print(line)


def printFabricToFile(fabric, fileName):
    fabricFile = open(fileName, "w+")
    for line in fabric:
        fabricFile.write(str(line)+'\n')
    fabricFile.close()


def findNumberOfOverlap(fabric):
    numberOfOverlap = 0
    for line in fabric:
        for (_, amount) in line:
            if amount > 1:
                numberOfOverlap += 1

    return numberOfOverlap


def findClaimWithoutOverlap(fabric, claims):
    allClaims = [int(claim['id']) for claim in claims]

    for line in fabric:
        for (claimsID, amount) in line:
            if amount > 1:
                for claimID in claimsID:
                    if claimID in allClaims:
                        allClaims.remove(claimID)

    return allClaims[0]


claims = claimsFromFile('input.txt')
fabric = loadClaims(claims, 1015)  # 1015

print(findClaimWithoutOverlap(fabric, claims))
