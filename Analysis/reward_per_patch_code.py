#%%
import numpy as np
import scipy 
import pandas as pd

p1 = pd.read_csv('1.csv',skiprows=78)
print(p1[p1.Length<7])
# %%
