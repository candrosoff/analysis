import pandas as pd
import matplotlib.pyplot as plt
import csv
import plot_data as p_d
import data_functions as d_f

def run():
    df=pd.read_csv("manufacturingMay.csv",index_col="North American Industry Classification System (NAICS)",error_bad_lines=False)
    df.dropna(inplace=True)
    df=df.T


    #df=df.drop(["Geography"])
    #df=df.drop(["Prices"])
    #df=df.drop(["Seasonal adjustment"])


    dfchange=d_f.transform(df)
    p_d.plot_data_all(dfchange,6)
    p_d.data_stats(dfchange)

    df2=dfchange.T
    #df2=df2.drop(df[[2]])
    df2=df2.T
    df3=p_d.monthly_growth(df2*100)
    print(df3)

    df4=df2.iloc[:, [0,13]]*100

    df4.plot(figsize=(10,6))
    plt.ylabel('Percent')
    leg=plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.1)
    plt.axhline(0, color='black')
    plt.show()


    import statsmodels.api as sm

    dta=df.iloc[:, [0,12]]

    df4=dta["Durable goods industries"]
    df5=dta["Non-durable goods industries"]
    #dta = sm.tsa.datetools.dates_from_range('Apr-12', 'Apr-17')
    #index = pd.DatetimeIndex(dates)
    #dta.set_index(index, inplace=True)

    cycle, trend = sm.tsa.filters.hpfilter(df4, 14400)
    cd, td = sm.tsa.filters.hpfilter(df5,14400)

    dta["dcycle"]=cycle
    dta["dtrend"]=trend
    dta["ndcycle"]=cd
    dta["ndtrend"]=td


    ax1=dta.loc[:,["Non-durable goods industries","ndtrend"]]
    ax2=dta.loc[:,["ndcycle"]]
    ax3=dta.loc[:,["Durable goods industries","dtrend"]]
    ax4=dta.loc[:,["dcycle"]]


    fig, axes = plt.subplots(nrows=2, ncols=2,figsize=[10,9],sharex=False)
    fig.subplots_adjust(right=1.1,hspace=.5)
    plta1=ax1.plot(ax=axes[0,0],title="Non-Durable Goods")
    plta=ax2.plot(ax=axes[0,1])
    pltb1=ax3.plot(ax=axes[1,0],title="Durable Goods")
    pltb=ax4.plot(ax=axes[1,1])

    plta.axhline(0,color='blue')
    pltb.axhline(0,color='blue')
    plta.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    pltb.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    #plta1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    #pltb1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

run()
