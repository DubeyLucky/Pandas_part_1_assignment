#!/usr/bin/env python
# coding: utf-8

# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[27]:


import pandas as pd


# In[28]:


x = pd.Series([4,8,15,16,23,42])


# In[29]:


pd.DataFrame(x) #or


# In[30]:


x


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

# In[31]:


l = ['Lucky','Kumar','Dubey','MCA','a','b','c','d','e','f']


# In[32]:


y = pd.Series(l)


# In[33]:


y


# In[34]:


z=pd.DataFrame(y)


# In[35]:


z


# Q3. Create a Pandas DataFrame that contains the following data:

# In[36]:


li = {"Name":['Alice','Bob','Claire'],
     "Age":[25,30,27],
     "Gender":['Female','Male','Female']}


# In[37]:


li


# In[38]:


pd.DataFrame(li)


# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# DataFrame:
#     1.Two-dimensional
#     2.Heterogenous – DataFrame elements can have different data types.
#     3.Size-mutable – Elements can be dropped or added in an existing DataFrame.
# Pandas Series:
#     1.One-dimensional
#     2.Homogenous – Series elements must be of the same data type.
#     3.Size-immutable – Once created, the size of a Series object cannot be changed.

# In[57]:


#DataFrame
#1.Two-dimensional 2.Heterogenous – DataFrame elements can have different data types. 3.Size-mutable – Elements can be dropped or added in an existing DataFrame.
import pandas as pd
x = {"Name":['Lucky','Kumar'],
      "Course":['MCA','MBA']}


# In[58]:


x


# In[59]:


pd.DataFrame(x)


# #pandas Series
# #Pandas Series: 1.One-dimensional 2.Homogenous – Series elements must be of the same data type. 3.Size-immutable – Once created, the size of a Series object cannot be changed.

# In[60]:


l = [1,2,3,4,5]


# In[61]:


pd.Series(l)


# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# In[66]:





# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# Series	One-dimensional array	Homogeneous data	Mutable	Immutable
# Data Frame	Two-dimensional array	Heterogeneous data	Mutable	Mutable
# Panel	Three-dimensional array	Heterogeneous data	Mutable	Mutable

# Q7. Create a DataFrame using multiple Series. Explain with an example.

# In[68]:


x = ['a','b','c','d','e']


# In[69]:


y = [1,2,3,4,5]


# In[70]:


z = ['ab','bc','cd','ef','fg']


# In[80]:


a=pd.Series(x)


# In[81]:


b=pd.Series(y)


# In[82]:


c=pd.Series(z)


# In[83]:


con = pd.concat([a,b],axis=1)


# In[85]:


con


# In[86]:


con_second = pd.concat([con,c],axis=1)


# In[87]:


con_second


# In[92]:


pd.DataFrame(con_second)


# In[ ]:




