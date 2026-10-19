import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
tips=sns.load_dataset('tips')
tips.head()
total_bill tip
sex smoker day time size
0
1
2
3
4
16.99 1.01 Female
10.34 1.66
21.01 3.50
23.68 3.31
Male
Male
Male
24.59 3.61 Female
No Sun Dinner
No Sun Dinner
No Sun Dinner
No Sun Dinner
No Sun Dinner
2
3
3
2
4
Code
sns.displot(tips.total_bill,kde=True)
<seaborn.axisgrid.FacetGrid at 0x79bb4c7ea680>

sns.displot(tips.total_bill,kde=False)
Text

1/9
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<seaborn.axisgrid.FacetGrid at 0x79bb0b0af580>
sns.jointplot(x=tips.tip,y=tips.total_bill)
<seaborn.axisgrid.JointGrid at 0x79bb08fc96c0>
sns.jointplot(x=tips.tip,y=tips.total_bill,kind="reg")
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
2/9
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<seaborn.axisgrid.JointGrid at 0x79bb08fc9cf0>
sns.jointplot(x=tips.tip,y=tips.total_bill,kind="hex")
<seaborn.axisgrid.JointGrid at 0x79bb088f4730>
sns.pairplot(tips)
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
3/9
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<seaborn.axisgrid.PairGrid at 0x79bb06fc3d30>
tips.time.value_counts()
count
time
Dinner
Lunch
dtype: int64
176
68
sns.pairplot(tips,hue='time')
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
4/9
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<seaborn.axisgrid.PairGrid at 0x79bb088f4670>
sns.pairplot(tips,hue='day')
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
5/9
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<seaborn.axisgrid.PairGrid at 0x79bb08f1f6a0>
sns.heatmap(tips.corr(numeric_only=True),annot=True)
<Axes: >
sns.boxplot(tips.total_bill)
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
6/9
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<Axes: ylabel='total_bill'>
sns.boxplot(tips.tip)
<Axes: ylabel='tip'>
sns.countplot(tips.day)
<Axes: xlabel='count', ylabel='day'>
sns.countplot(tips.sex)
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
7/9
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<Axes: xlabel='count', ylabel='sex'>
tips.sex.value_counts().plot(kind='pie')
<Axes: ylabel='count'>
tips.sex.value_counts().plot(kind='bar')
<Axes: xlabel='sex'>
sns.countplot(tips[tips.time=='Dinner']['day'])
https://colab.research.google.com/drive/1ixdO2LyjKtMYUgtZcoc8jSInDGmeKn4_#scrollTo=J9uBGy0XX3rZ&printMode=true
8/9
10/1/24, 9:52 AM
9.9.2024-Visualization.ipynb - Colab
<Axes: xlabel='count', ylabel='day'>
9/9
