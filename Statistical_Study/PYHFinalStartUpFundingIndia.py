#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 11:30:32 2018

@author: jkp
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/home/sysadm/Desktop/JKP BSPro/Used_startup_funding.csv")

#***Basic/General/Normal Information
data.head()
data.dtypes
data.info()
data.describe()

#Well this doesn't make any clear picture about this column, so simply we can ignore
#this feature for now

#One this we can notice that we have date column which canbe very useful in EDA so 
#let's do feature of programming on it

##*** Data Modification
def temp(v):
    try:
        #pd.to_datetime(v)
        return(pd.to_datetime(v.replace('.','/').replace('//','/')))
    except:
        print(v)
data["Date"].apply(lambda v: temp(v))

date=data["Date"].apply(lambda v: temp(v))
data["month_year"]=date.dt.strftime("%Y-%m")
data["Year"]=date.dt.strftime("%Y")

'''data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data['MY'] = (pd.to_datetime(data['Date'],format='%d/%m/%Y').dt.year*100)+(
              pd.to_datetime(data['Date'],format='%d/%m/%Y').dt.month) # Works Fine'''

data['AmountInUSD']
data['amount']=data['AmountInUSD'].apply(lambda x:float(str(x).replace(",","")))
data['amount']

#data["amount"]=data["AmountInUSD"].str.replace(',', '').astype(float)
#print(data[["Date","month_year","Year","amount"]].head())
data[["Date","month_year","Year","amount"]]

#get list of numeric and categorical columns 
get_numeric_cols= lambda df:list(df._get_numeric_data().columns)
num_cols=get_numeric_cols(data)
num_cols
cat_cols=np.setdiff1d(data.columns,num_cols)
cat_cols

#Check the data quality – Missing values, Outlier
pd.isnull(data).sum()

print(data['Remarks'])
print(data['Remarks'].unique())
data.isnull().any()

data['Remarks'].fillna(0, inplace=False)
ct=0
for i in data['Remarks']:
    if i==0:
        ct=ct+1
print('Total no. of NaN cells in Remarks column is ',ct)
print('Dimension of data is',data.shape)
#ct=data['Remarks'].isnull().sum()
RVac=(ct*100)/len(data)
print('Nan_cells_count_percentage in Remark column is ',RVac)


ct0=data['IndustryVertical'].isnull().sum()
RVac0=(ct0*100)/len(data)
print('Nan_cells_count_percentage in IndustryVertical column is ',RVac0)

#data=data.drop(['Remarks'], axis=1)
#data=data[data['Remarks'] != 0]

data['StartupName'].unique().shape
data['IndustryVertical'].unique().shape
data['SubVertical'].unique().shape
data['CityLocation'].unique().shape
data['InvestorsName'].unique().shape
data['InvestmentType'].unique().shape
data['AmountInUSD'].unique().shape
len(data['AmountInUSD'].unique().shape)*100/len(data)

# percentage of null values for all the columns.
pd.isnull(data).sum()/data.shape[0]*100
#So here we can see that 82.33% data has NaN values so we can ignore this
#Column for out prediction

#"Remarks" column has highest missing values, which useless for now
# We cannot analyse by tking null value out_of account

# as we have made lot of change so start from basic again
data.head()
data.dtypes
data.info()
data.describe()

data["amount"].plot.box()

#also anything above 98% and below 2% can be treated as outlier.
print(data["amount"].quantile(0.02))
print(data["amount"].quantile(0.98))

#Here anyting below 40000USD and anything above 100000000 USD is considered outliers

#*** Univariate, bivariate, multivariate
#Apply EDA techniques to identify what influences investment amount
#EDA(Effective Data Analysis)

# Univariate

yearfreq = data['Year'].value_counts().plot.bar()

month_year = data['month_year'].value_counts().plot.bar(figsize=(12,4))
data.groupby(["month_year"]).size().plot.bar(figsize=(12,5), color="steelblue")

x=data["InvestmentType"].value_counts()/data.shape[0]*100
x.head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('Investment Type', fontsize=12)
plt.ylabel('Shaped Count', fontsize=12)

x0=data["IndustryVertical"].value_counts()/data.shape[0]*100
x0.head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('Industry Vertical', fontsize=12)
plt.ylabel('Shaped Count', fontsize=12)

dt_amo=data['IndustryVertical'].groupby([data.IndustryVertical]).agg(
        'count').nlargest(30)

dt_amo.plot(kind="bar",figsize=(16,9),grid=True,title="Industry wise distribution",
            cmap='rainbow')

data["IndustryVertical"].value_counts().head(20)
data['IndustryVertical'].isnull().sum()
industryvertical = []
for indver in data['IndustryVertical']:
    for inv in str(indver).split(","):
        if inv != "":
            industryvertical.append(inv.strip().lower())
StartUpIndvers = pd.Series(industryvertical).value_counts()#[:20]
StartUpIndvers
for i in  range(len(industryvertical)):
    if industryvertical[i] =='ECommerce':
        industryvertical[i]='eCommerce'
    if industryvertical[i] =='Ecommerce':
        industryvertical[i]='eCommerce'
    if industryvertical[i] =='ecommerce':
        industryvertical[i]='eCommerce' 
    if industryvertical[i] =='Food & Beverages ':
        industryvertical[i]='Food & Beverage '
    if industryvertical[i] =='Food Delivery Platform':
        industryvertical[i]='Online Food Delivery'   
        
#Still we donot have covered all redudency
StartUpIndvers0 = pd.Series(industryvertical).value_counts()#[:20]
StartUpIndvers0.head(20)

StartUpIndvers0.head(20).plot(kind="bar",figsize=(16,9),grid=True,
                     title="Industry wise distribution",cmap='rainbow')

x1=data["SubVertical"].value_counts()/data.shape[0]*100
x1.head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('Industry SubVertical', fontsize=12)
plt.ylabel('SubVerticalCount', fontsize=12)

x2=data["SubVertical"].value_counts()
x2.head(20).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('Industry SubVertical', fontsize=12)
plt.ylabel('Shaped Count', fontsize=12)
#online pharmacy has highest investments

data["SubVertical"].value_counts().head(20)
data['SubVertical'].isnull().sum()
industrysubvertical = []
for indsver in data['SubVertical']:
    for insv in str(indsver).split(","):
        if insv != "":
            industrysubvertical.append(insv.strip().lower())
        #else :
            #investornames.append('unknown'.lower())    
StartUpIndsvers = pd.Series(industrysubvertical).value_counts()#[:20]
StartUpIndsvers.isnull().sum()
#Still we donot have covered all redudency

StartUpIndsvers.head(20).plot(kind="bar",figsize=(16,9),grid=True,
                     title="Industry wise distribution",cmap='rainbow')
plt.xlabel('Industry SubVertical', fontsize=12)
plt.ylabel('Count', fontsize=12)

data['CityLocation'].value_counts().head(20)
data_ct=data['CityLocation'].groupby([data.CityLocation]).agg('count')

data_ct.plot(kind="bar",figsize=(16,9),grid=True,title="City wise distribution",
             cmap='rainbow')

x3=data["CityLocation"].value_counts()/data.shape[0]*100
x3.head(20).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('City Location', fontsize=12)
plt.ylabel('Shaped Count For The City', fontsize=12)


x4=data["CityLocation"].value_counts()
x4.plot.bar(figsize=(12,5), color="steelblue") #x1.head(20)
plt.xlabel('City Location', fontsize=12)
plt.ylabel('Count For The City', fontsize=12)

x5=data["InvestorsName"].value_counts()#/data.shape[0]*100
x5.head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('Investors Name', fontsize=12)
plt.ylabel('ShapedCount', fontsize=12)

dt_inv=data['InvestorsName'].groupby([data.InvestorsName]).agg('count').nlargest(10)
dt_inv.plot(kind="bar",figsize=(12,9),grid=True,title="Industry wise distribution",
            cmap='rainbow')


data["InvestorsName"].value_counts().head(30)
data['InvestorsName'].isnull().sum()
investornames = []
for investor in data['InvestorsName']:
    for inv in str(investor).split(","):
        if inv != "":
            investornames.append(inv.strip().lower())
        else :
            investornames.append('unknown'.lower())
        
StartUpInvestors = pd.Series(investornames).value_counts()[:20]
StartUpInvestors#.isnull().sum()

for i in  range(len(investornames)):
    if investornames[i] =='undisclosed investor':
        investornames[i]='undisclosed investors'
    if investornames[i] =='undisclosed':
        investornames[i]='undisclosed investors'      
#Still we donot have covered all undisclosed
StartUpInvestors0 = pd.Series(investornames).value_counts()#[:20]
StartUpInvestors0.head(20)

StartUpInvestors0.head(20).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('InvestorsName', fontsize=12)
plt.ylabel('Count', fontsize=12)

StartUpInvestors0.head(10).plot(kind="pie",figsize=(12,9),
                                title="Industry wise distribution",
                                 autopct='%1.1f%%', startangle=90,cmap='rainbow')
plt.ylabel('Count/Freq', fontsize=12)
#Bivariet analysis

data.groupby(["Year"])["amount"].sum().plot(kind="pie",figsize=(12,9),
                                title="Industry wise distribution",
                                 autopct='%1.1f%%', startangle=90,cmap='rainbow')
####shows key error but not in_regular

data.groupby(["month_year"])["amount"].mean().plot.bar(figsize=(12,5), color="steelblue")
plt.ylabel('Count Of Investment', fontsize=12)

#2 months have highest average investment.. March and May of 2017 have highest investements.
#Lowest investment was seen in the month of October 2017

X6=data.groupby('StartupName')['amount'].sum().sort_values(ascending=False)
X6.head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('StatrUp Name', fontsize=12)
plt.ylabel('TotalAmountGotInvestedIn_c_USD ', fontsize=12)
##Paytm and Flipkart are the 2 startups with highest investments put in to them



X7=data.groupby('StartupName')['amount'].size().sort_values(ascending=False)
X7.head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('StatrUp Name', fontsize=12)
plt.ylabel('NumberOfInvestmentGot', fontsize=12)

##Swiggy is the comapany which received highest number of investments i.e,
#7 investments

x=data.groupby(["IndustryVertical"])["amount"].mean().sort_values(
                ascending=False).head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('IndustryVertical', fontsize=12)
plt.ylabel('AverageAmountGotInvestedIn_c_USDperInvestor', fontsize=12)

##from the below graph we can see that average of people investing in online 
#marketplace is more 

x=data.groupby(["InvestorsName"])["amount"].sum().sort_values(
                ascending=False).head(10).plot.bar(figsize=(12,5), color="steelblue")
plt.xlabel('InvestorsName', fontsize=12)
plt.ylabel('TotalAmountHvInvestedIn_c_USD', fontsize=12)
#Soft bank is the highest investor group in terms of sum invested

#***Hypothesis Testing

from scipy.stats import chi2_contingency
def df(df,cat_colS):
    I = [0,2,6,8,10]
    cat_col1=np.delete(cat_colS, I).tolist() # removed remarks,date,amountinusd(kept amount)
                                             #columns
    
    t=[]
    t1=[]
    for i in range(len(cat_col1)):
        for j in range(i + 1, len(cat_col1)):
            
            obsv=df.groupby([cat_col1[i],cat_col1[j]]).size()
            obsv.name="Freq"
            obsv=obsv.reset_index()
            obsv=obsv.pivot_table(index=cat_col1[i],columns=cat_col1[j],values="Freq")
            stat, p, dof, exp =chi2_contingency(obsv.fillna(0).values)
            if p< 0.05:

                t1= (cat_col1[i],cat_col1[j])
              
                t.append(t1)

    return(t)
a=df(data,cat_cols)
for b in a:
    print( "%s is dependent on %s" %(b[0],b[1]))


####

#Summary:
    
###AmountinUSD has many missing values about 35% of data is missing.
## subvertical also has many missing values
#Remarks has lot of missing values-->we can ignore/drop remarks column fron analysis
#there are a lot of outliers in amountin USD column.
    
#Year 2016 had maximum number of investments
#Month July 2016 followed by January of 2016 has large number of funding.
##Seed Funding and Private Equity are the most preferable type of funding 
#ConsumerInternet is the Industry vertical on which highest number of investement unlike 
#Technology
##bangalore has highest number of investements
#Large number of the startup's funding are from undisclosed source
## ratan tata can be considered a special case, since all others are investment groups and he
#is an individual investing
##online pharmacy has highest investments
# 2 months have highest average investment.. March and May of 2017 have highest investements.
#Lowest investment was seen in the month of October 2017
##Paytm and Flipkart are the 2 startups with highest investments put in to them
##Swiggy is the comapany which received highest number if investments i.e, 7 investments
## from the graph we can see that average of people investing in online marketplace is more 
#Soft bank is the highest investor group in terms of sum invested
#Investment type and the Year column influence the amount.

lstmsg=[10,20,10,10,20,10,20]
msg=['T','H','A','N','K','S','!']
plt.figure(figsize=(12,12))
colors=['red','green','orange']
plt.pie(lstmsg, labels=msg,autopct='THANKS!',startangle=310) #colors=colors,
plt.title('Thanks',color = 'blue',fontsize = 15)
plt.xlabel('The END', fontsize=12)
plt.show() 

