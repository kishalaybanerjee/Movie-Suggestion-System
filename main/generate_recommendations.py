import json

from text_comparison import parseDataIntoDict, filterDataDict


def getSimilarityDict(inPath):
    with open(f'{inPath}', 'r') as fp:
        return json.loads(fp.read())


def getShowNamesInCorrectFormat(dataDict):
    showList = list(dataDict)
    for shows in showList:
        name = " ".join(dataDict[shows]['title'])
        dataDict[shows]['title'] = name


def getShowDetails(dataPath, jsonPath):
    dataDict = filterDataDict(parseDataIntoDict(dataPath))
    showSimilarityDict = getSimilarityDict(jsonPath)
    print()


if __name__ == '__main__':

    dataPath = './netflix_titles.csv'
    jsonPath = './show_similarities.json'
    getShowDetails(dataPath, jsonPath)
