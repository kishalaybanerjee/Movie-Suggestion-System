import json
from itertools import chain
from countryinfo import CountryInfo


def readDataFile(inPath):
    with open(f'{inPath}', 'r') as fp:
        return json.loads(fp.read())


def getCountryData(inPath):
    dataDict = readDataFile(inPath)
    countryData = [dataDict[k]['country'] for k in dataDict.keys()]
    # creating a list of unique country names and cleaning the data
    countryList = cleanCountryData(countryData)
    return [reformatCountryNames(x) for x in countryList]


def cleanCountryData(dataList):
    countryList = list(filter(None, set(chain(*dataList))))
    countryList = list(set(removeWhitespaceInStrings(countryList)))
    countryList = [x.lower() for x in countryList]
    return [x for x in countryList if 'unknown' not in x]


def createCountryInfoDict(inPath):
    countryList = getCountryData(inPath)
    return {x: [CountryInfo(x).capital(), CountryInfo(x).info()['capital_latlng'][0],
                CountryInfo(x).info()['capital_latlng'][1]] for x in countryList}


def removeWhitespaceInStrings(wordList):  # to handle cases when the country name has a leading or trailing space,
    return [x.strip() for x in wordList]


def writeDictToJson(infoDict):
    with open('./countryinfo.json', 'w') as fp:
        json.dump(infoDict, fp)


def reformatCountryNames(name):
    if name == 'east germany' or name == 'west germany':
        return 'germany'
    if name == 'vatican city':
        return 'italy'
    if name == 'montenegro':
        return 'serbia'
    if name == 'soviet union':
        return 'russia'
    if name == 'bahamas':
        return 'the bahamas'
    if name == 'palestine':
        return 'israel'
    return name


if __name__ == '__main__':
    path = './data.json'
    countryInfoDict = createCountryInfoDict(path)
    # print(countryInfoDict.keys())
    writeDictToJson(countryInfoDict)

    # TODO: Drawbacks of countryinfo module results in the need for the reformatCountryNames function
    # TODO: A more elegant way of data cleaning (?)

