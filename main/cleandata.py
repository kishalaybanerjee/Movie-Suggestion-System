import pandas as pd
import numpy as np
import os
import json


def findNulls(df):
    return df.isnull().sum()


def findUniquedTypes(df):
    return np.unique(df.dtypes)


def removeNullValues(df):

    dataTypesDict = {'int64': 0, 'O': 'unknown'}

    for cols in df.columns:
        for keys in dataTypesDict.keys():
            if df[cols].dtypes == keys:
                df[cols].fillna(dataTypesDict[keys], inplace=True)

    return df


def convertCellValuesToList(df):
    for cols in df.columns:
        if df[cols].dtypes != 'int64' and cols != 'show_id':
            df[cols] = df[cols].str.split(',')

    return df


def createDataDict(df):
    df = convertCellValuesToList(removeNullValues(df))

    keyList = list(df['show_id'])
    dataDict = {}
    dictKeys = [x for x in df.columns if x != 'show_id']

    for idx, row in df.iterrows():
        rowDict = {}
        for names in dictKeys:
            rowDict[names] = row[names]
        dataDict[keyList[idx]] = rowDict

    return getShowNamesInCorrectFormat(dataDict)


def getShowNamesInCorrectFormat(dataDict):
    showList = list(dataDict)
    for shows in showList:
        name = " ".join(dataDict[shows]['title'])
        dataDict[shows]['title'] = name

    return dataDict


if __name__ == '__main__':

    path = './netflix_titles.csv'
