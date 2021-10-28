#%%
import numpy as np
import scipy 
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/7.csv',skiprows=75)
# print(df)
explore = 0
exploit = 0

# print(df.iloc[0,3])

data = pd.DataFrame(columns=["time","ratio"])

for i in range(1,len(df.iloc[:,0])):
    if df.iloc[i,0] == df.iloc[i-1,0]:
            exploit = exploit + 1
    else:
        explore = explore + 1
    ratio = exploit/explore
    data = data.append({"time":df.iloc[i,3],"ratio":ratio},ignore_index=True)

    i=i+1

print(data.iloc[0:20,:])

sns.scatterplot(x="time",y="ratio",data=data)

# %%
