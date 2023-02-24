#!/usr/bin/env python
# coding: utf-8

# In[99]:


#importing libraries and creating dataset
import numpy as np # linear algebra
import pandas as pd # data processing

import plotly
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

tv_shows = pd.read_csv('Desktop/tv_shows.csv')
tv_shows.head()


# In[100]:


tv_shows.drop_duplicates(subset='Title',
                         keep='first',inplace=True)


# In[102]:


tv_shows_long=pd.melt(tv_shows[['Title','Netflix','Hulu','Disney+',
                                'Prime Video']],id_vars=['Title'],
                      var_name='StreamingOn', value_name='Present')
tv_shows_long = tv_shows_long[tv_shows_long['Present'] == 1]
tv_shows_long.drop(columns=['Present'],inplace=True)
tv_shows_long.head()


# In[103]:



tv_shows_combined = tv_shows_long.merge(tv_shows, on='Title', how='inner')


# In[104]:


tv_shows_combined.head()


# In[105]:


tv_shows_combined.drop(columns = ['Title',
                                  'Year', 'Age', 'Type'], inplace=True)


# In[106]:


tv_shows_combined.head()


# In[107]:


tv_shows_combined.drop(columns = ['Netflix',
                                  'Hulu', 'Prime Video', 'Disney+','ID'], inplace=True)


# In[108]:


tv_shows_combined.head()


# In[109]:


tv_shows_combined.drop(columns = ['Unnamed: 0'], inplace=True)


# In[110]:


tv_shows_combined.head()


# In[113]:


tv_shows_combined.groupby('StreamingOn').plot(kind='bar')


# In[115]:


figure = []
figure.append(px.violin(tv_shows_combined, x = 'StreamingOn', y = 'IMDb', color='StreamingOn'))
figure.append(px.violin(tv_shows_combined, x = 'StreamingOn', y = 'Rotten Tomatoes', color='StreamingOn'))
fig = make_subplots(rows=2, cols=4, shared_yaxes=True)

for i in range(2):
    for j in range(4):
        fig.add_trace(figure[i]['data'][j], row=i+1, col=j+1)

fig.update_layout(autosize=False, width=800, height=800)        
fig.show()


# In[ ]:




