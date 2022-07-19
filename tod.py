# import pandas as p

import matplotlib.pyplot as bb
import pylab
import pandas as pd
# import time

# readexcel = pd.read_excel('Analog input data.xlsx')
# print(readexcel.head())
# print(readexcel.head())
# bb.plot(readexcel['value'])
# pylab.show()
file = 'Analog input data.xlsx'


df= pd.read_excel(file)
print(df)
# bb.plot(df)
# d = df.to_dict()
# pylab.show()
df.plot.bar(x='date',y='value')
bb.show()

# while True:
#     val = df
#     print(val)
#     time.sleep(10)
    

# ,usecols=[0,1]