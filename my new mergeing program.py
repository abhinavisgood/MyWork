import pandas as pd
data_set = pd.read_csv(r'C:\Users\Mr. Abhinav\Desktop\my new file.csv')
print(data_set)
a=data_set
import numpy as np

y=a['Data_value']
b=list(a['Period'])

b=[int(x) for x in b]
b=np.array(b,dtype=np.int64,order='F')
print(b)
b=np.reshape(b,(65748,1),order='F')

print(b.shape)
from sklearn.linear_model import LinearRegression
mind=LinearRegression()
mind.fit(b,y)
print(mind.predict([[2050.01]]))