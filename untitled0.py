# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:32:46 2020

@author: user
"""


a = '''
				LEARNING GUIDE TO YOUR MODEL


•fill_na function
Removing or filling the NaN and undefined values in the dataset is an important step in Exploratory Data Analysis.
You can either remove the particular row or column containing NaN values or else fill those values with the mean,median etc. depending on the usecase.

Importing the essential tools
We use tools provided by pandas to perform this function. So all we have to import is pandas library.
import pandas

Function definition
def fill_na(dataframe):

    for col in dataframe.columns:
        if dataframe[col].dtype.name != 'object':
            if (dataframe[col].isnull().sum())*2 >= num_rec:
                dataframe = dataframe.drop([col], axis=1)
            else:
                dataframe[col] = dataframe[col].fillna(dataframe[col].mean())
    return dataframe

Function call
Input your dataset as the parameter to this function, to handle the NaN values in your dataset.
fill_na(dataframe)

Check out the documentation here : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html






•scale function
Your dataset may contain a wide variety of values. Inorder to process your data further it is essential to scale down your data in the desired range based on the usecase. 
This function helps you to do so.

Importing the essential tools
from sklearn.preprocessing import RobustScaler,StandardScaler

Function definition
def scale(X_train,X_test):
    sc = StandardScaler()   
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    return X_train, X_test

Function call
The X_train and X_test are passed in as the parameters while calling the function.
scale(X_train,X_test)

For more info visit : https://benalexkeen.com/feature-scaling-with-scikit-learn/






•splitdata function
Splits your dataset into train data for training the model and test data. This functionality is provided by the scikit-learn library.

Importing the essential tools
from sklearn.model_selection import train_test_split

Function definition
def splitdata(X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
    return X_train, X_test, y_train, y_test


Function call
Pass in your independent and dependent variables into the function while calling and that's it you get a train test split of your dataset.
splitdata(X,y)


Check out more : https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html






•encode function
This function converts the categorical features in your dataset and convert it into numerical values.
One Hot encoding produces three columns and the presence of a class is represented in binary format. The three classes are separated out to three different features.
Label encoding or Ordinal encoding gives numerical aliases to the classes. Numerical labels are always between 1 and the number of classes.

Importing the essential tools
from sklearn.preprocessing import LabelEncoder

Function definition

>>>def encode(dataframe):
...    
...    for col in dataframe.columns:
           if dataframe[col].dtype.name == 'object':
               le = LabelEncoder()
               dataframe[col] = le.fit_transform(dataframe[col])
       return dataframe

Function call
Your dataset is passed in as the parameter for this function.
encode(dataframe)

Learn more : https://machinelearningmastery.com/how-to-prepare-categorical-data-for-deep-learning-in-python/






•dupli function
It detects the duplicate rows in your dataset and removes them. The different ways of handling the datasets using this function can be found out using the links provided. 
Importing the essential tools
It is actually imported from pandas and all you need to import is pandas for this function
import pandas

Function definition
def dupli(dataframe):
    dataframe.drop_duplicates(subset=None, keep='first', inplace=True)
    return dataframe

Function call
Pass in the dataframe as the parameter for this function and it will remove the duplicate rows in your dataset.
dupli(dataframe)

Check out the documentation : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html
'''
c = ['Random Forest Classifier','Decision Tree Classifier','SVC',
                           'SGD Classifier','Gradient Boosting Classifier',
                           'Adaboost Classifier']

r  = ['Linear Regressor','Ridge Regressor','Lasso Regressor',
                   'DecisionTree Regressor','Gradient Boosting Regressor']

for ele in r:
    
    file = open('knowledge_to_display/'+ele+' Report.txt', 'a')
    file.write(a)
    file.close()