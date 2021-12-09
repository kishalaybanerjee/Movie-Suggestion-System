import json
import random

from text_comparison import parseDataIntoDict, filterDataDict


def getSimilarityDict(inPath):
    with open(f'{inPath}', 'r') as fp:
        return json.loads(fp.read())


def convertNoneTypeToString(value):
    return value if value else ''


def getShowRecommendations(dataPath, jsonPath):
    dataDict = filterDataDict(parseDataIntoDict(dataPath))
    showSimilarityDict = getSimilarityDict(jsonPath)

    showList = list(dataDict.keys())
    chosenShow = random.choice(showList)
    name = dataDict[chosenShow]['title']

    print(f'Searching for shows similar to {name} based on cast...')
    print()

    try:
        similarShowsDict = dict(sorted(showSimilarityDict[chosenShow].items(), key=lambda item: item[1], reverse=True))
        keyList = list(similarShowsDict)
        if len(keyList) >= 3:
            simShow = [dataDict[keyList[0]]['title'], dataDict[keyList[1]]['title'], dataDict[keyList[2]]['title']]
        else:
            simShow = [dataDict[keyList[0]]['title'], None, None]
    except (IndexError, KeyError):
        # returns the string instead of just printing to handle the unbound local error of simShow when exception is hit
        return print(f'Could not find similar shows to {name} based on cast. Please try again')

    # handler to prevent printing None when there are less than 3 similar shows
    simShow = [convertNoneTypeToString(i) for i in simShow]

    print(f'According to cast, shows similar to {name} are: '
          f'{str(simShow[0])} \n {str(simShow[1])} \n {str(simShow[2])}')


if __name__ == '__main__':

    dataPath = './netflix_titles.csv'
    jsonPath = './show_similarities.json'
    getShowRecommendations(dataPath, jsonPath)

    # TODO: Add user input for show name instead of random.choice (need to know the names in the database?)
    # TODO: Check the value of the highest similarity before reporting, if max is less than 0.25 (example), is there any point in reporting?
    # TODO: Replace JS with better metrics
