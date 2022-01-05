import random

from checkcountrydata import readDataFile


def generate_recommendations(dataDict):
    showList = list(dataDict.keys())
    show = random.choice(showList)
    showDataDict = dataDict[show]


if __name__ == '__main__':
    path = './data.json'
    # dataDict = readDataFile(path)
    # print(dataDict.keys())

