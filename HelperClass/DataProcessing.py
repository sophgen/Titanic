import pandas as pd
from sklearn.model_selection import train_test_split

class DataProcessing:
    def __init__(self, fileName, dataType, delimiter):
        self.fileName = fileName
        self.dataType = dataType
        self.delimiter = delimiter
        
    def ReadFile(self):
        self.AllData = pd.read_csv(filepath_or_buffer = self.fileName, dtype = self.dataType, sep = self.delimiter)
    
    def GetSummaryOfNull(self):
        return self.AllData.isnull().sum()
    
    def FillNullNumColWithMean(self, numCols):
        for i in numCols:
            if self.AllData[i].isnull().sum() > 0:
                meanVal = self.AllData[i].mean()
                self.AllData[i].fillna(meanVal, inplace=True)
                
    def FillNullCatColWithNA(self, catCols):
        for i in catCols:
            if self.AllData[i].isnull().sum() > 0:
                self.AllData[i].fillna('NA', inplace=True)
    
    def GetColumnsByType(self, colType):
        return self.X.select_dtypes(include = colType).columns.values.tolist()
    
    def PopulateFeatureColumns(self, featureColumns):
        self.X = self.AllData[featureColumns]
    
    def RandomSplitTrainTestData(self, testRatio, seed, stratifyColumn=False):
        if stratifyColumn == False:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=testRatio, random_state=seed)
        else:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=testRatio, random_state=seed, stratify = self.y)
            
    def ShowDistinctValues(self, cols):
        result = {}
        for i in cols:
            result[i] = self.AllData[i].value_counts().to_dict()
        return result