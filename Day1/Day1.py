File = 'ChallengeData.txt'
testFile = 'testDataDay2.txt'
def mainPart1(filename):
    deltaCollection = []
    totalDelta = 0
    lists = extractData(filename)
    sortedLeftSide = sortList(lists[0])
    sortedRightSide = sortList(lists[1])

    for i in range(len(sortedLeftSide)):
        delta = GetDelta(sortedLeftSide[i], sortedRightSide[i])
        deltaCollection.append(delta)
        totalDelta += delta
    print (totalDelta)


def mainPart2(filename):
    similarityScore = 0
    SimilarityNumbersToSum = []
    lists = extractData(filename)
    leftlist = lists[0]
    rightlist = lists[1]
    for i in range(len(leftlist)):
        number = leftlist[i] * (rightlist.count(leftlist[i]))
        #SimilarityNumbersToSum.append(number)
        similarityScore+= number
    print(similarityScore)

def extractData(filename):
    leftlist = []
    rightlist = []
    testData = open(filename)
    for line in testData:
        numbers = line.split()
        leftlist.append(int(numbers[0]))
        rightlist.append(int(numbers[1]))
    return leftlist, rightlist

def sortList(list):
    newList = sorted(list)
    return newList

def GetDelta(num1, num2):
    larger = max(num1, num2)
    smaller = min(num1, num2)
    delta = larger - smaller
    return delta

#mainPart1(File)
mainPart2(File)


