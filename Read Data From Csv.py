import pandas as pd
filepath=''

#import the data
data=pd.read_csv(filepath)

#print few rows
print(data.iloc[:5])

#different delimeters - tab seperated file (.tsv)
data=pd.read_csv(filepath,sep='\t')

#different delimeters - tab seperated file (.tsv)
data=pd.read_csv(filepath,sep='\t')

#different delimeters - space seperated file 
data=pd.read_csv(filepath,delim_whitespace=True)

#dont use first row for column names
data=pd.read_csv(filepath,header=None)

#specify column names
data=pd.read_csv(filepath,names=['Name1','Name2'])

#custom missing values
data=pd.read_csv(filepath,na_values=['NA',99])