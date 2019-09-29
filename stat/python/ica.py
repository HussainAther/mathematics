#Supporting functions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import math

"""
Independent component analysis.
"""

#load unsupervised dataset
def loadunsuperviseddata():
    OriginalXpd = pd.read_csv("data.csv", encoding='SHIFT-JIS', index_col=0)
    OriginalX = OriginalXpd.as_matrix()
    OriginalX = OriginalX.astype(float)
    return (OriginalX, OriginalXpd)

#load unsupervised dataset with test dataset
def loadunsuperviseddatawithtestdata():
    Xpd = pd.read_csv("data.csv", encoding='SHIFT-JIS', index_col=0)
    OriginalX = Xpd.as_matrix()
    OriginalX = OriginalX.astype(float)
    X_predictionpd = pd.read_csv("data_prediction.csv", encoding='SHIFT-JIS', index_col=0)
    OriginalX_prediction = X_predictionpd.as_matrix()
    OriginalX_prediction = OriginalX_prediction.astype(float)
    return (OriginalX, OriginalX_prediction, Xpd, X_predictionpd)
    
#load supervised dataset for classification
def loadsuperviseddataforclassification():
    datapd = pd.read_csv("data.csv", encoding='SHIFT-JIS', index_col=0)
    data = np.array(datapd)
    Originaly = np.ravel( np.c_[data[:,0]] )
    OriginalX = data[:,1:data.shape[1]].astype(float)
    data_prediction1pd = pd.read_csv("data_prediction1.csv", encoding='SHIFT-JIS', index_col=0)
    data_prediction1 = np.array(data_prediction1pd)
    Originaly_prediction1 = np.ravel( np.c_[data_prediction1[:,0]] )
    OriginalX_prediction1 = data_prediction1[:,1:data.shape[1]].astype(float)
    data_prediction2pd = pd.read_csv("data_prediction2.csv", encoding='SHIFT-JIS', index_col=0)
    OriginalX_prediction2 = np.array(data_prediction2pd)
    OriginalX_prediction2 = OriginalX_prediction2.astype(float)
    return (Originaly, OriginalX, Originaly_prediction1, OriginalX_prediction1, \
            OriginalX_prediction2, data_prediction2pd)

#load supervised dataset for regression
def loadsuperviseddataforregression():
    datapd = pd.read_csv("data.csv", encoding='SHIFT-JIS', index_col=0)
    data = np.array(datapd)
    data = data.astype(float)
    Originaly = np.c_[data[:,0]]
    OriginalX = data[:,1:data.shape[1]]
    data_prediction1pd = pd.read_csv("data_prediction1.csv", encoding='SHIFT-JIS', index_col=0)
    data_prediction1 = np.array(data_prediction1pd)
    data_prediction1 = data_prediction1.astype(float)
    Originaly_prediction1 = np.c_[data_prediction1[:,0]]
    OriginalX_prediction1 = data_prediction1[:,1:data.shape[1]]
    data_prediction2pd = pd.read_csv("data_prediction2.csv", encoding='SHIFT-JIS', index_col=0)
    OriginalX_prediction2 = np.array(data_prediction2pd)
    OriginalX_prediction2 = OriginalX_prediction2.astype(float)
    return (Originaly, OriginalX, Originaly_prediction1, OriginalX_prediction1, \
            OriginalX_prediction2, data_prediction2pd)
            
#Find variables with zero variance
def variableszerovariance( X ):
    Var0Variable = np.where( X.var(axis=0) == 0 )
    if len(Var0Variable[0]) == 0:
        print( "No variables with zero variance" )
    else:
        print( "{0} variable(s) with zero variance".format(len(Var0Variable[0])))
        print( "Variable number: {0}".format(Var0Variable[0]+1) )
        print( "The variable(s) is(are) deleted." )
    return Var0Variable

#Save matrix
def savematrixcsv( X, index, filename):
    Xpd = pd.DataFrame(X)
    Xpd.index = index
    exec("Xpd.to_csv( \"{}.csv\", header = False )".format( filename ) )

def savematrixcsv2( X, index, column, filename):
    Xpd = pd.DataFrame(X[:, np.newaxis])
    Xpd.index = index
    Xpd.columns = column
    exec("Xpd.to_csv( \"{}.csv\" )".format( filename ) )

#Save matrix with column name
def savematrixcsvwithcolumnname( X, index, columnname, filename):
    Xpd = pd.DataFrame(X)
    Xpd.index = index
    Xpd.columns = columnname
    exec("Xpd.to_csv( \"{}.csv\" )".format( filename ) )
    
