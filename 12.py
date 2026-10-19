#sample calculation for low range(lr) , upper range (ur),percentile
import numpy as np
array=np.random.randint(1,100,16)  # randomly generate 16 numbers between  1 to 100
array
array([27, 50, 44,  6, 58, 61, 23, 86, 67, 20, 75,  7, 79, 61, 90, 54])
array.mean()
50.5
np.percentile(array,25)
26.0
np.percentile(array,50)
56.0
np.percentile(array,75)
69.0
np.percentile(array,100)
90.0
#outliers detection
def outDetection(array):
sorted(array)
Q1,Q3=np.percentile(array,[25,75])
IQR=Q3-Q1
lr=Q1-(1.5*IQR)
ur=Q3+(1.5*IQR)
return lr,ur
lr,ur=outDetection(array)
lr,ur
(-38.5, 133.5)
import seaborn as sns
%matplotlib inline
sns.displot(array)
<seaborn.axisgrid.FacetGrid at 0x78f3291c2710>
sns.distplot(array)
  sns.distplot(array)
<Axes: ylabel='Density'>
new_array=array[(array>lr) & (array<ur)]
new_array
array([27, 50, 44,  6, 58, 61, 23, 86, 67, 20, 75,  7, 79, 61, 90, 54])
sns.displot(new_array)
<seaborn.axisgrid.FacetGrid at 0x78f2e09bb580>
lr1,ur1=outDetection(new_array)
lr1,ur1
(-38.5, 133.5)
final_array=new_array[(new_array>lr1) & (new_array<ur1)]
final_array
array([27, 50, 44,  6, 58, 61, 23, 86, 67, 20, 75,  7, 79, 61, 90, 54])
sns.distplot(final_array)
<ipython-input-18-7ba96ada5b76>:1: UserWarning: 
`distplot` is a deprecated function and will be removed in seaborn v0.14.0.
Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).
For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
  sns.distplot(final_array)
<Axes: ylabel='Density'>
