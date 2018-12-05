import re
from datetime import datetime


def timestampsFromFile(fileName):
    timestamps = []
    for timestamp in open(fileName, 'r'):
        timeOfEvent = timestamp[1:17]
        guardNumberRegex = re.search('#[0-9]* ', timestamp)
        guardNumber = int(guardNumberRegex.group(
            0)[1:-1].strip()) if guardNumberRegex else 0

        isWakingUpEventRegex = re.search('wakes', timestamp)
        isWakingUpEvent = True if isWakingUpEventRegex else False
        isFallingAsleepEventRegex = re.search('falls', timestamp)
        isFallingAsleepEvent = True if isFallingAsleepEventRegex else False

        timestamps.append({'date': timeOfEvent, 'guardNumber': guardNumber,
                           'isWakingUpEvent': isWakingUpEvent, 'isFallingAsleepEvent': isFallingAsleepEvent})

    return timestamps


def sortByTime(timestamps):

    sortedTimestamps = sorted(timestamps, key=lambda timestamp: datetime.strptime(
        timestamp['date'], '%Y-%m-%d %H:%M'))

    guardNumber = 0
    for index in range(0, len(sortedTimestamps)):
        timestamp = sortedTimestamps[index]
        guardNumber = timestamp['guardNumber'] if timestamp['guardNumber'] > 0 else guardNumber
        sortedTimestamps[index]['guardNumber'] = guardNumber

    return sortedTimestamps


def printTimestamps(timestamps):
    for timestamp in timestamps:
        print(timestamp)


def printTimestampsToFile(timestamps, fileName):
    timestampsFile = open(fileName, "w+")
    for timestamp in timestamps:
        timestampsFile.write(str(timestamp)+'\n')
    timestampsFile.close()


def minutesSleptByGuards(sortedTimestamps):
    minutesSleptByGuards = {}

    for timestamp in sortedTimestamps:
        guardNumber = timestamp['guardNumber']
        timeOfEvent = datetime.strptime(
            timestamp['date'], '%Y-%m-%d %H:%M')

        if timestamp['isWakingUpEvent']:
            if guardNumber not in minutesSleptByGuards:
                minutesSleptByGuards[guardNumber] = 0

            minutesSleptByGuards[guardNumber] = minutesSleptByGuards[guardNumber] + (
                timeOfEvent.minute - fallingAsleepTime.minute)

        fallingAsleepTime = timeOfEvent if timestamp['isFallingAsleepEvent'] else None

    return minutesSleptByGuards


def guardWhoHasSleptTheMost(minutesByGuards):
    return max(minutesByGuards, key=minutesByGuards.get)


def minuteSleptTheMost(minutesDetail):
    return max(minutesDetail, key=minutesDetail.get)


def day4(sortedTimestamps):
    guardNumber = guardWhoHasSleptTheMost(
        minutesSleptByGuards(sortedTimestamps))

    minutes = {}
    for timestamp in [event for event in sortedTimestamps if event['guardNumber'] == guardNumber]:
        if timestamp['isWakingUpEvent'] or timestamp['isFallingAsleepEvent']:
            timeOfEvent = datetime.strptime(
                timestamp['date'], '%Y-%m-%d %H:%M')

            if timestamp['isWakingUpEvent']:
                for minute in range(fallingAsleepTime.minute, timeOfEvent.minute):
                    if minute not in minutes:
                        minutes[minute] = 0

                    minutes[minute] = minutes[minute] + 1

            fallingAsleepTime = timeOfEvent if timestamp['isFallingAsleepEvent'] else None

    minute = minuteSleptTheMost(minutes)

    return guardNumber * minute


def day4_part2(sortedTimestamps):
    guards = {}
    for timestamp in sortedTimestamps:
        guardNumber = timestamp['guardNumber']

        if timestamp['isWakingUpEvent'] or timestamp['isFallingAsleepEvent']:

            if guardNumber not in guards:
                guards[guardNumber] = {}

            timeOfEvent = datetime.strptime(
                timestamp['date'], '%Y-%m-%d %H:%M')

            if timestamp['isWakingUpEvent']:
                for minute in range(fallingAsleepTime.minute, timeOfEvent.minute):
                    if minute not in guards[guardNumber]:
                        guards[guardNumber][minute] = 0

                    guards[guardNumber][minute] = guards[guardNumber][minute] + 1

            fallingAsleepTime = timeOfEvent if timestamp['isFallingAsleepEvent'] else None

    guardNumberFound = 1
    minuteFound = 1
    maxMinute = 1
    for guard in guards:
        for minute in guards[guard]:
            guardNumberFound = guard if guards[guard][minute] > maxMinute else guardNumberFound
            minuteFound = minute if guards[guard][minute] > maxMinute else minuteFound
            maxMinute = guards[guard][minute] if guards[guard][minute] > maxMinute else maxMinute

    timestampsFile = open('outputtabranak.txt', "w+")
    for guard in guards:
        timestampsFile.write(str(guard)+' | '+str(guards[guard]))
        timestampsFile.write('\n')
    timestampsFile.close()

    return guardNumberFound * minuteFound


timestamps = timestampsFromFile('input.txt')
sortedTimestamps = sortByTime(timestamps)

printTimestampsToFile(timestamps, 'unsorted.txt')
printTimestampsToFile(sortedTimestamps, 'sorted.txt')

print(day4_part2(sortedTimestamps))
