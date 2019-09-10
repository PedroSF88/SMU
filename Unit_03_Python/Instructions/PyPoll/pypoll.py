#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("PyPoll\Resources\election_data.csv")


# In[3]:


votes=df.shape[0]-1
V=str(votes)


# In[4]:


cand=df['Candidate'].unique()


# In[5]:


cvotes = df['Candidate'].value_counts()


# In[6]:


pctvote=cvotes/votes*(100)


# In[7]:


totals=pd.DataFrame({'Percent of Votes':pctvote, 'Vote Count':cvotes})
pd.options.display.float_format = '%{:,.2f}'.format
totals


# In[8]:


winner=totals['Percent of Votes'].idxmax()
W=winner


# In[9]:


ER='Election Results'
line='-------------------------'
TV= 'Total Votes '+ V
win='Winner: '+ W


# In[10]:


final=ER, line,TV, line,totals, line,win
f=str(final)


# In[11]:


totals.to_csv('pypoll.txt')


# In[12]:


with open ('pypoll.txt','w') as file:
    file.write(f),
    file.close
    x = y = z = np.arange(1.0,7.0,1.0)
    np.savetxt('pypoll.txt', x, delimiter=",", fmt='%.3f')


# In[ ]:


print(ER)
print(line)
print(TV)
print(line)
print(totals)
print(line)
print(win)


# In[ ]:




