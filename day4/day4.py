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


timestamps = timestampsFromFile('input.txt')
sortedTimestamps = sortByTime(timestamps)

printTimestampsToFile(timestamps, 'unsorted.txt')
printTimestampsToFile(sortedTimestamps, 'sorted.txt')

print(day4(sortedTimestamps))
