import pandas as pd
import numpy as np
import itertools
import random
import matplotlib.pyplot as plt

import cleandata


def parseDataIntoDict(path):
    df = pd.read_csv(path, header=0)
    return cleandata.createDataDict(df)


def computeJaccardSimilarity(group1, group2):
    intersection = set(group1).intersection(set(group2))
    union = set(group1).union(set(group2))
    return len(intersection)/len(union)


def filterDataDict(dataDict):
    keysToRemove = [x for x in dataDict.keys() if 'unknown' in dataDict[x]['cast']]
    for k in keysToRemove:
        dataDict.pop(k, None)

    return dataDict


def computeCastSimilarityOfShows(dataDict, randomShows=False):
    """
    Currently using Jaccard similarity
    JS has some big flaws, as listed in https://medium.com/@adriensieg/text-similarities-da019229c894, but for
    the comparison of 'Cast', I don't think they hold
    TODO : Replace JS with better similarity comparisons after more research, allow for specific user input of shows
    """
    dataDict = filterDataDict(dataDict)  # not strictly necessary, can also be solved by 0 < simIndex < 1
    showList = list(dataDict.keys())

    if randomShows:
        show1, show2 = random.sample(showList, 2)
        cast1, cast2 = dataDict[show1]['cast'], dataDict[show2]['cast']
        print(f'The similarity between the casts of {dataDict[show1]["title"]} and {dataDict[show2]["title"]} is ')
        return print(computeJaccardSimilarity(cast1, cast2))

    showPairs = list(itertools.combinations(showList, 2))
    commonCastDict = {}
    for pairs in showPairs:
        show1, show2 = pairs[0], pairs[1]
        cast1, cast2 = dataDict[show1]['cast'], dataDict[show2]['cast']
        similarityIndex = computeJaccardSimilarity(cast1, cast2)
        if similarityIndex != 0:
            commonCastDict[f'{show1}_{show2}'] = similarityIndex
            print(f'{show1}_{show2}')

    return commonCastDict


def plotSimilarityIndexOfShows(indexDict):
    indexValues = list(indexDict.values())
    plt.hist(indexValues)
    plt.title('Frequency vs Similarity Values (Filtered for non zero only)')
    plt.xlabel('Similarity Values')
    plt.ylabel('Frequency')
    plt.savefig('./Figures/jaccard_similarity_histogram.png')
    plt.show()


if __name__ == '__main__':

    source = './netflix_titles.csv'
    dataDict = parseDataIntoDict(source)
    castDict = computeCastSimilarityOfShows(dataDict)
    plotSimilarityIndexOfShows(castDict)

    # TODO : check for the large values of sim_index and find the specific shows/cast members?
