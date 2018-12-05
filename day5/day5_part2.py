def loadPolymer(fileName):
    polymers = []
    for polymer in open(fileName, 'r'):
        polymers = polymer
    return polymers


def react(polymer, replacements):
    reactedPolymer = polymer

    maxNumber = 100000000
    numberOfReactions = 0
    while numberOfReactions < maxNumber:

        if not any(replacement in reactedPolymer for replacement in replacements):
            break

        for replacement in replacements:
            reactedPolymer = reactedPolymer.replace(replacement, '')

        numberOfReactions += 1

    return reactedPolymer


def day5_part2():
    polymer = loadPolymer('input.txt')

    replacements = ['aA', 'Aa', 'bB', 'Bb', 'cC', 'Cc', 'dD', 'Dd', 'eE', 'Ee', 'fF', 'Ff', 'gG', 'Gg', 'hH', 'Hh', 'jJ', 'Jj', 'iI', 'Ii', 'kK', 'Kk', 'lL', 'Ll', 'mM',
                    'Mm', 'nN', 'Nn', 'oO', 'Oo', 'pP', 'Pp', 'qQ', 'Qq', 'rR', 'Rr', 'sS', 'Ss', 'tT', 'Tt', 'uU', 'Uu', 'vV', 'Vv', 'wW', 'Ww', 'xX', 'Xx', 'yY', 'Yy', 'zZ', 'Zz']

    simulations = []

    for index in range(0, int(len(replacements)/2)):
        defectPolymer = polymer
        replacement1 = replacements[index*2][0]
        replacement2 = replacements[index*2+1][0]
        # Removing defects

        defectPolymer = defectPolymer.replace(replacement1, '')
        defectPolymer = defectPolymer.replace(replacement2, '')
        defectPolymer = react(defectPolymer, replacements)

        simulations.append({replacement1[0]: len(defectPolymer)})

    print(simulations)


day5_part2()
