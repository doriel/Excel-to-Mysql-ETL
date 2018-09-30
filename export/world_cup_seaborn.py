
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


df = pd.read_csv('data/world.csv')


# In[3]:


print df.head()


# In[4]:


df["Total Goals"] = df['Home Team Goals'] + df['Away Team Goals']


# In[5]:


print df['Total Goals']


# In[6]:


sns.set_style('whitegrid')


# In[7]:


sns.set_context("poster", font_scale=0.8)


# In[9]:


f, ax = plt.subplots(figsize=(18, 7))
ax = sns.barplot(data=df, x='Year', y='Total Goals')
plt.show()

