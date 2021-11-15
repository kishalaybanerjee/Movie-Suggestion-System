import numpy as np
import pandas as pd


class DataSets:
    def __init__(self, df):
        self.df = df

    def __len__(self):
        return len(self.df)

    def checkForNulls(self):
        return self.df.isnull().values.any()

    def findNulls(self):
        return self.df.isnull().sum()

    def printCols(self):
        print(self.df.columns)

    def getColumnNames(self):
        return [x for x in self.df.columns]

    def getColumnDataTypes(self):
        # TODO : Add more useful methods
        pass

    def checkSpecificColumn(self, colName):
        print(self.df[colName].head())

    def findUniquedTypes(self):
        return np.unique(self.df.dtypes)

    def replaceNaNValues(self):
        # TODO : Fix this
        for cols in self.df.columns:
            if 'int' in str(self.df[cols].dtypes):
                self.df[cols].fillna(0)
            else:
                self.df[cols].fillna('unknown')


if __name__ == '__main__':

    path = './Netflix Data/netflix_titles.csv'
    df = pd.read_csv(path, header=0)
    print(df.head())

    dfObj = DataSets(df)
    print(type(dfObj))
