import numpy as np
data=''

#calcualate interquartile range
q25,q50,q75=np.percentile(data,[25,50,75])
iqr=q75-q25

#calculate min/max limit to be considered
min=q25-1.5*(iqr)
max=q25+1.5*(iqr)

print(min,q25,q50,q75,max)

#identify the data points
[x for x in data[''] if x > max]