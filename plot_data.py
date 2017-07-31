import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_data_all(df,total_plots):
    title=(input("What do you want to name your graph? \n"))
    cols=2
    nrows=total_plots/cols
    rows=math.ceil(nrows)
    df4=df.ix[0:,0:total_plots]
    df4.plot(kind='line', subplots=True, figsize=(20, 20), grid=True, title=title,layout=(rows, 2), sharex=False, sharey=False,legend=True)
    plt.ylabel("percent")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

def plot_data(df,total_plots,months):
    title=(input("What do you want to name your graph? \n"))
    cols=2
    nrows=total_plots/cols
    rows=math.ceil(nrows)
    df4=df.ix[0:months,0:total_plots]
    d=df4.plot(kind='line', subplots=True, figsize=(20, 20), grid=True, title=title,layout=(rows, 2),  sharex=False, sharey=False,legend=True)
    plt.axhline(0,color="blue")
    plt.ylabel("percent")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

def data_stats(df):
    print("Mean growth rates: \n",  df.mean() ,"\n", "Standard deviation: \n", df.std())



    

def monthly_growth(df):
    df3=df.T.sort_values(df.index[-1], ascending=False).T.iloc[-1:].T

    positive=df.T.sort_values(df.index[-1], ascending=False).T.iloc[-1:].T
    positive[positive<0]=np.nan

    p=positive.as_matrix()
    p=np.isnan(p)

    length=len(p)
    
    
    colors=['r' if p[i]==True else 'b' for i in range(length)]
    #print(colors)

    print("Monthly Change \n")

    df3.plot(kind='bar',width=.5,figsize=(10,6),color=colors)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    plt.axhline(0, color='black')
    plt.ylabel("percent")
    plt.show()

    return df3
