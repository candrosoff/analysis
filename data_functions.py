import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv
import math
from dateutil.parser import parse
import statsmodels.api as sm

def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False

def transform(df):
    columns = [column for column in df.columns]
    dfnew = df[columns]
    dfnew=dfnew.transpose()
    #dfchange=[]
    dfchange=df.pct_change(1)

    return dfchange





def select_index(df):
    index_col = [column for column in df.columns if df[column].dtype != 'float64']
    print(index_col)
    dfindex = df[index_col]
    choose_index = int(input("What index do you want to select? "))
    choose_index=choose_index-1
    print("Selecting " + index_col[choose_index] + "\n")

    selection = int(input("Do you want to select a second index? Type 1 for yes or 0 for no. \n"))
    if selection==1:
        second_index = [column for column in df.columns if df[column].dtype != 'float64']
        print(second_index)
        dfsecond_index = df[second_index]
        if dfsecond_index.empty:
            print("No second index available")
            df.index=df[[choose_index]]
        else:
            choose_index2 = int(input("What index do you want to select? "))
            choose_index2=choose_index2-1
            print("Selecting " + second_index[choose_index2] + "\n")
            index_array=[index_col[choose_index],second_index[choose_index2]]
            df.index = pd.MultiIndex.from_tuples(df.index, names=index_array)
    else:
        df.index=df[[choose_index]]

    return df

#def colour_negative_red(val):#needs work

#    color = 'red' if val < 0 else 'black'
#    return 'color: %s' % color

def filter(df,period):
    #where period is 100 for yearly, 1600 for quarterly and 14400 for monthly

    cycle, trend = sm.tsa.filters.hpfilter(df, period)
    m_decomp = df
    m_decomp["cycle"] = cycle
    m_decomp["trend"] = trend

    return m_decomp
