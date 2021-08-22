#!/usr/bin/env python
# coding: utf-8

# HAMOYE INTERNSHIP

# In[1]:


import pandas as pd


# In[2]:


#reading the data from the csv file
data = pd.read_csv("https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")


# In[3]:


#preview of the first five lines of the loaded data

data.head(50)


# In[4]:


data.describe()


# In[5]:


data.skew(axis = 0, skipna = True )


# In[6]:


data.kurt(axis = 0, skipna = True )


# In[7]:


data.groupby('fuel_type_code_pudl').agg({'fuel_cost_per_unit_burned': ['mean']})


# In[8]:


data.isnull().sum()


# In[9]:


data.info()


# In[10]:


data.isnull().sum() * 100 / len(data) 


# In[11]:


data.groupby('report_year').agg({'fuel_cost_per_unit_delivered': ['mean']})


# In[12]:


data.corr(method ='pearson')


# In[17]:


data_mean = data.groupby(['fuel_type_code_pudl', 'report_year',]).agg({'fuel_cost_per_unit_burned': ['mean']})


# In[19]:


data_mean['pct_change'] = data_mean.pct_change()


# In[20]:


data_mean


# In[ ]:




