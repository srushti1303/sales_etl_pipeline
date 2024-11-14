#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("/Users/srushtikamble/Documents/Projects/Pay Per Click /Electronic_sales_Sep2023-Sep2024.csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


mode_add_ons = df['Add-ons Purchased'].mode().iloc[0]
df['Add-ons Purchased'] = df['Add-ons Purchased'].fillna(mode_add_ons)


# In[6]:


df = df.drop_duplicates().reset_index(drop=True)
df['item_id'] = df.index


# In[7]:


df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])


# In[8]:


df.info()


# In[9]:


purchase_date_dim  = df[['Purchase Date']].reset_index(drop=True)
purchase_date_dim['date_year'] = purchase_date_dim['Purchase Date'].dt.year
purchase_date_dim['date_month'] = purchase_date_dim['Purchase Date'].dt.month
purchase_date_dim['date_day'] = purchase_date_dim['Purchase Date'].dt.day
purchase_date_dim['date_weekday'] = purchase_date_dim['Purchase Date'].dt.weekday

purchase_date_dim['purchase_date_id'] = purchase_date_dim.index

purchase_date_dim = purchase_date_dim[['purchase_date_id', 'Purchase Date','date_year', 'date_month', 'date_day', 'date_weekday',]]

purchase_date_dim.head()


# In[10]:


customer_dim =df[['Customer ID', 'Age', 'Gender', 'Loyalty Member']].reset_index(drop=True)
customer_dim['customer_id'] = customer_dim.index 
customer_dim =customer_dim[['customer_id', 'Customer ID', 'Age', 'Gender', 'Loyalty Member']]
customer_dim.head()


# In[11]:


order_dim = df[['Order Status', 'Payment Method', 'Shipping Type']].reset_index(drop=True)
order_dim['order_id'] = order_dim.index
order_dim = order_dim[['order_id', 'Order Status', 'Payment Method', 'Shipping Type']] 
order_dim.head()


# In[12]:


fact_table = df.merge(purchase_date_dim, left_on='item_id', right_on='purchase_date_id') \
             .merge(customer_dim, left_on='item_id', right_on='customer_id') \
             .merge(order_dim, left_on='item_id', right_on='order_id') \
             [['item_id','purchase_date_id','customer_id','order_id','SKU','Product Type','Unit Price',
               'Rating','Total Price','Quantity','Add-ons Purchased','Add-on Total']]


# In[13]:


fact_table.columns


# In[14]:


fact_table.head()


# In[ ]:




