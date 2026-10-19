import numpy as np
import pandas as pd
df=pd.read_csv('Iris.csv')
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
#   Column        Non-Null Count  Dtype  ---  ------        --------------  -----  
0   sepal.length  150 non-null    float64
1   sepal.width   150 non-null    float64
2   petal.length  150 non-null    float64
3   petal.width   150 non-null    float64
4   variety       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
df.variety.value_counts()
In [3]:
Out[3]: Setosa        50
Versicolor    50
Virginica     50
Name: variety, dtype: int64
df.head()
In [4]:
Out[4]:
sepal.length sepal.width petal.length petal.width variety
0
1
2
3
4
In [5]:
5.1
4.9
4.7
4.6
5.0
3.5
3.0
3.2
3.1
3.6
features=df.iloc[:,:-1].values
label=df.iloc[:,4].values
1.4
1.4
0.2 Setosa
0.2 Setosa
1.3
1.5
1.4
0.2 Setosa
0.2 Setosa
0.2 Setosa
In [6]:
In [8]:
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
xtrain,xtest,ytrain,ytest=train_test_split(features,label,test_size=.2,rando
model_KNN=KNeighborsClassifier(n_neighbors=5)
model_KNN.fit(xtrain,ytrain)
Out[8]: KNeighborsClassifier()
In a Jupyter environment, please rerun this cell to show the HTML representation or
trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page
with nbviewer.org.
1/2
localhost:8888/notebooks/KNN.ipynb
In [9]:
In [10]:
In [11]:
In [ ]:
0.9583333333333334
1.0
Out[10]: array([[50,  0,  0],
      [ 0, 47,  3],
      [ 0,  2, 48]], dtype=int64)
             precision    recall  f1-score   support
     Setosa       1.00      1.00      1.00        50
 Versicolor       0.96      0.94      0.95        50
  Virginica       0.94      0.96      0.95        50
   accuracy                           0.97       150
  macro avg       0.97      0.97      0.97       150
weighted avg       0.97      0.97      0.97       150
print(model_KNN.score(xtrain,ytrain))
print(model_KNN.score(xtest,ytest))
from sklearn.metrics import confusion_matrix
confusion_matrix(label,model_KNN.predict(features))
from sklearn.metrics import classification_report
print(classification_report(label,model_KNN.predict(features)))
 

