import pandas as pd
import json
from itertools import chain
from countryinfo import CountryInfo


def readDataFile(inPath):
    with open(f'{inPath}', 'r') as fp:
        return json.loads(fp.read())


def getCountryData(inPath):
    dataDict = readDataFile(inPath)
    countryData = [dataDict[k]['country'] for k in dataDict.keys()]
    # creating a list of unique country names
    # not removing unknown since it is needed for comparison; empty string needs to be removed from this list
    countryList = [x.lower() for x in list(filter(None, set(chain(*countryData))))]
    return [reformatCountryNames(x) for x in countryList]


def createCountryInfoDict(inPath):
    countryList = removeWhitespaceInStrings(getCountryData(inPath))
    return {x: [CountryInfo(x).capital(), CountryInfo(x).info()['capital_latlng'][0],
                CountryInfo(x).info()['capital_latlng'][1]] for x in countryList}


def removeWhitespaceInStrings(wordList):  # to handle cases when the country name has a leading or trailing space,
    # observed for ' slovenia'
    return [x.strip() for x in wordList]


def reformatCountryNames(name):
    if name == 'east germany':
        return 'germany'
    if name == 'vatican city':
        return 'italy'
    if name == 'montenegro':
        return 'serbia'
    if name == 'soviet union':
        return 'russia'
    return name


if __name__ == '__main__':
    path = './data.json'
    countryInfoDict = createCountryInfoDict(path)
    print(countryInfoDict.keys())

