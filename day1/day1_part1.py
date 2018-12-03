def sum():
    sum = 0
    for line in open('input.txt', 'r'):
        sum += int(line)

    return sum


print(sum())
