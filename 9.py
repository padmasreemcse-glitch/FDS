import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
data=pd.read_csv('/content/Iris_Dataset.csv')
data
data.info()
data.describe()
data.value_counts('variety')
sns.countplot(x='variety',data=data,)
plt.show()
dummies=pd.get_dummies(data.variety)
FinalDataset=pd.concat([pd.get_dummies(data.variety),data.iloc[:,[0,1,2,3]]],axis=1)
FinalDataset.head()
sns.scatterplot(x='SepalLengthCm',y='SepalWidthCm',hue='variety',data=data,)
sns.scatterplot(x='PetalLengthCm',y='PetalWidthCm',hue='variety',data=data,)
sns.pairplot(data,hue='variety',height=3);
plt.show()
sns.FacetGrid(data,hue='variety',height=5).map(sns.histplot,'PetalLengthCm').add_legend();
plt.show();