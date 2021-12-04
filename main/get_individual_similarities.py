import json

from text_comparison import parseDataIntoDict, filterDataDict, computeJaccardSimilarity


def computeCastSimilarity(dataDict, show1, show2):
    return round(computeJaccardSimilarity(dataDict[show1]['cast'], dataDict[show2]['cast']), 2)


def createShowComparisonsBasedOnCast(inPath):
    """
    The 0 < computeCastSimilarity < 1 condition is deceptively important. When I ran this function without it, the
    output was 885MB, with the majority having a JS = 0.
    The condition pruned it down to 1.8MB, a ~500 times decrease. Running time for both approximately the same
    """
    dataDict = filterDataDict(parseDataIntoDict(inPath))
    showList = list(dataDict.keys())

    return {f'{shows}': {f'{elements}': computeCastSimilarity(dataDict, shows, elements) for elements in showList
                         if elements != shows if 0 < computeCastSimilarity(dataDict, shows, elements) < 1}
            for shows in showList}


def writeOutDictAsJSON(showSimilarityDict, fileName):
    with open(f'./{fileName}.json', 'w') as fp:
        json.dump(showSimilarityDict, fp)


if __name__ == '__main__':

    path = './netflix_titles.csv'
    showComparisonDict = createShowComparisonsBasedOnCast(path)
    writeOutDictAsJSON(showComparisonDict, 'show_similarities')
    print('Show similarity data written out to file')
