# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:16:11 2022

@author: Ramisha Anjum Nova
"""

import pandas as pd

#%%

obj = pd.Series([4, 7, -5, 3])

#%%

obj[obj % 2 == 0]

#%%

obj + 5

#%%

obj * 2

#%%

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000,'Utah': 5000} 
obj3 = pd.Series(sdata) 
print(obj3)

#%%

list1 = [['Alice',23,3.5,10],['Bob', 24,3.4,6],['Charlie', 22,3.9,8]] 
df = pd.DataFrame(list1) 
df.columns = ['name','age','cgpa','hoursStudied'] 
print(df.head()) 

#%%

dict1 = {'id':[1,2,3],'name':['alice','bob','charlie'],'age':[20, 25, 32]} 
df1 = pd.DataFrame(dict1) 
print(df1) 

#%%

df2 = pd.read_csv("sample_data_1.csv", header = None) 
df2.columns = ['id','state','population','murder_rate'] 
print(df2) 

df2.head()
df2.tail()
df2.count()

#%%

print(df1.iloc[0][0]) 
print(df1.loc[0]['name']) 

#%%
 
df3 = df1[['name','cgpa']] 
print(df3) 
 
#%%

df4 = df1.loc[1:2]
print(df4) 

df5 = df1.iloc[1:3] 
print(df5) 
 
#%%

df4 = df1.loc[1:2,['name','age']] 
print(df4) 

df5 = df1.iloc[1:3,[0,1]] 
print(df5) 
 
#%%


list1 = [['Alice',23,3.5,10],['Bob',24,3.4,6],['Charlie',22,3.9,8]] 
df = pd.DataFrame(list1) 
df.columns = ['name','age','cgpa','hoursStudied']

list2 = [['Don',21,2.5,2],['Elton',25,2.75,4]] 
df11 = pd.DataFrame(list2) 
df11.columns = ['name','age','cgpa','hoursStudied'] 
 
df12 = df.append(df11, ignore_index=True) 
print(df12) 
 
#%%
 
df12.drop([0,1], inplace=True) 
df12.drop(['cgpa'], axis = 1, inplace=True) 

#%%
 
new_cols = ['n','a','hs'] 
df12.columns = new_cols 
print(df12) 

#%%
 
cgpa_greater_than_three_point_five1 = df1[df1['cgpa'] > 3.5] 
cgpa_greater_than_three_point_five2 = df1.loc[df1['cgpa'] > 3.5] 
cgpa_greater_than_three_point_five3 = df1.query('cgpa > 3.5') 
 
print(cgpa_greater_than_three_point_five1) 
print(cgpa_greater_than_three_point_five2) 
print(cgpa_greater_than_three_point_five3) 
 
df1.sort_values(by = 'age', ascending = False) 
 
#%%

df = pd.read_csv("weather.csv")
print(type(df))
print(df)

#%%

print(df.head())

#%%

print(df.tail())

#%%

print(df.describe())

#%%

df.columns = ['outlook','temperature','humidity','windy','play']

#%%

t = df['temperature']
print(type(t))
print(t)

#%%

sum = 0
for value in t:
    sum+=value
print(sum)

#%%

df1 = df[['temperature','humidity']]
print(df1)

#%%

df2 = df.loc[0:9,['temperature','humidity']]
print(df2)

#%%

df3 = df.iloc[0:10,[1,2]]
print(df3)

#%%

df4 = df.iloc[1::2,[0,1,3]]
print(df4)

#%%

temperature = df[['temperature']]

print("Mean: " , temperature.mean())
print("Standard Deviation: ", temperature.std())
print("Variance: ", temperature.var())
print("Lower Quartile: " , temperature.quantile(0.25))
print("Median: ", temperature.quantile(0.5))
print("Median: " , temperature.median())
print("Upper Quartile: " , temperature.quantile(0.75))
print("Skewness: " , temperature.skew())
print("Kurtosis: " , temperature.kurt())
print("Min: ", temperature.min())
print("Max: ", temperature.max())

#%%

df.hist(column=['temperature'], bins = 5)

#%%

df.hist(column='humidity', bins = 5)

#%%

humidity = df[['humidity']]
print("Mean: " , humidity.mean())
print("Standard Deviation: ", humidity.std())
print("Variance: ", humidity.var())
print("Lower Quartile: " , humidity.quantile(0.25))
print("Median: ", humidity.quantile(0.5))
print("Median: " , humidity.median())
print("Upper Quartile: " , humidity.quantile(0.75))
print("Skewness: " , humidity.skew())
print("Kurtosis: " , humidity.kurt())
print("Min: ", humidity.min())
print("Max: ", humidity.max())

#%%

list1 = [[1,0], [1,1], [2,2], [2,3], [2,3], [2,4], [3,4], [3,5], [4,6], [5,7]]
print(list1)

#%%

df_list1 = pd.DataFrame(list1, columns = ['x','y'])
print(df_list1)

#%%

df_list1.hist(column = ['x'], bins = 5)

#%%

print('Skew: ', df_list1[['x']].skew())

#%%

df_list1.hist(column = ['y'], bins = 8)

#%%

print('Skew: ', df_list1[['y']].skew())

#%%

print('Kurt - X: ', df_list1[['x']].kurt())
print('Kurt - Y: ', df_list1[['y']].kurt())

#%%

df_list1.plot.scatter(x = "x", y = "y")

#%%

df_list1.boxplot(column = ['x', 'y'])
