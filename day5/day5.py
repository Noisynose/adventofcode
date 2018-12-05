def loadPolymer(fileName):
    polymers = []
    for polymer in open(fileName, 'r'):
        polymers = polymer
    return polymers


def react(polymer):
    replacements = ['aA', 'Aa', 'bB', 'Bb', 'cC', 'Cc', 'dD', 'Dd', 'eE', 'Ee', 'fF', 'Ff', 'gG', 'Gg', 'hH', 'Hh', 'jJ', 'Jj', 'iI', 'Ii', 'kK', 'Kk', 'lL', 'Ll', 'mM',
                    'Mm', 'nN', 'Nn', 'oO', 'Oo', 'pP', 'Pp', 'qQ', 'Qq', 'rR', 'Rr', 'sS', 'Ss', 'tT', 'Tt', 'uU', 'Uu', 'vV', 'Vv', 'wW', 'Ww', 'xX', 'Xx', 'yY', 'Yy', 'zZ', 'Zz']

    reactedPolymer = polymer

    maxNumber = 1000000
    numberOfReactions = 0
    while numberOfReactions < maxNumber:

        if not any(replacement in reactedPolymer for replacement in replacements):
            break

        for replacement in replacements:
            reactedPolymer = reactedPolymer.replace(replacement, '')

        numberOfReactions += 1

    return reactedPolymer


def day5():
    polymer = loadPolymer('input.txt')
    reactedPolymer = react(polymer)

    print(len(reactedPolymer))


day5()
