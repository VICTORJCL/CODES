import pandas as pd



# data=[1,2,3,4]
data={'id':[1,2,3,4],'nome':['rob','ana', 'carol','concha']}
df = pd.DataFrame(data, index=["pessoa1", 'pessoa2','pessoa 3', 'pessoa 4'])
df