#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv(r'C:\Users\floPe\OneDrive\Desktop\SMU\SMU\Unit_03_Python\Instructions\PyBank\Resources\budget_data.csv')


# In[3]:


NumMonths = len(df["Date"].unique())


# In[4]:


dftotalsum = df["Profit/Losses"].sum()
avgdif=df['Profit/Losses'].diff()
averagediff=avgdif.sum()/(NumMonths-1)
maxdif=avgdif.max()
mindif=avgdif.min()


# In[5]:


df2=df
df2["Avg_Dif"]=avgdif


# In[6]:


max_date=df2['Date'].loc[df2['Avg_Dif'].idxmax()]
min_date=df2['Date'].loc[df2['Avg_Dif'].idxmin()]


# In[7]:


max_dd=(max_date,maxdif)
min_dd=(min_date,mindif)


# In[8]:


finData_df=pd.DataFrame({
    'Financial Analysis':['Total Months:', 'Total:', 'Average Change:','Greatest Increase in Profits:', 'Greatest Decrease in Profits '],
'Amt':[NumMonths,dftotalsum, averagediff, max_dd,min_dd]
})


# In[9]:


print(finData_df)


# In[10]:


finData_df.to_csv('pybank.txt')


# In[ ]:




