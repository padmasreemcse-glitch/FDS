Hotel.csv 
CustomerID Age_Group Rating(1-5) 
Hotel 
1 
20-25 
4 
FoodPreference 
Bill 
NoOfPax 
EstimatedSalary 
Age_Group 
Ibis 
2 
30-35 
5 
veg 
1300 
2 
40000 
20-25 
LemonTree 
3 
25-30 
6 
Non-Veg 
2000 
3 
59000 
30-35 
RedFox 
4 
20-25 -1 
Veg 
1322 
2 
30000 
25-30 
LemonTree 
5 
35+ 
3 
Veg 
1234 
2 
120000 
20-25 
Ibis 
6 
35+ 
3 
Vegetarian 
989 
2 
45000 
35+ 
Ibys 
7 
35+ 
4 
Non-Veg 
1909 
2 
122220 
35+ 
RedFox 
8 
20-25 
7 
Vegetarian 
1000 -1 
21122 
35+ 
LemonTree 
9 
25-30 
2 
Veg 
2999 -10 
345673 
20-25 
Ibis 
9 
25-30 
2 
Non-Veg 
3456 
3 -99999 
25-30 
Ibis 
10 
30-35 
Non-Veg 
3456 
3 -99999 
25-30 
5 
About Dataset: 
RedFox 
non-Veg 
6755 
4 
87777 
30-35 
No.of Columns =9 (called as series – CustomerID, Age_Group, Rating(1-5),Hotel, FoodPreference, 
Bill, NoOfPax, EstimatedSalary) 
CutomerID: Numerical Continuous data  
Age: Categorical Data 
Rating (1-5): Numerical Discrete Data 
Hotel: Categorical Data 
Food: Categorical Data 
Bill: Numerical Continuous data 
NoOfPax: Numerical Discrete 
EstimatedSalary: Numerical Continuous data 
Python Code: 
# Upload Hotel.csv and convert it into dataFrame 
import numpy as np 
import pandas as pd 
df=pd.read_csv("Hotel_Dataset.csv") 
df 
#From the dataframe identify the duplicate row(i.e row 9) 
#The duplicated() method returns a Series with True and False values that describe which rows in the 
DataFrame are duplicated and not. 
df.duplicated() 
#The info() method prints information about the DataFrame. The information contains the number of 
columns, column labels, column data types, memory usage, range index, and the number of cells in 
each column (non-null values). 
df.info() 
#The drop_duplicates() method removes duplicate rows.  
df.drop_duplicates(inplace=True) 
df 
#While removing duplicate record row index also removed 
# The len() function to return the length of an object. With a dataframe, the function returns the 
number of rows. 
len(df) 
10 
#Reset the index 
index=np.array(list(range(0,len(df)))) 
df.set_index(index,inplace=True) 
index 
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
df 
#Axis refers to the dimensions of a DataFrame (index and columns) or Series (index only) Use 
axis=0 to apply functions row-wise along the index. Use axis=1 to apply functions column-wise 
across columns. 
df.drop(['Age_Group.1'],axis=1,inplace=True) 
df 
# The function . loc is typically used for label indexing and can access multiple columns. 
df.CustomerID.loc[df.CustomerID<0]=np.nan 
df.Bill.loc[df.Bill<0]=np.nan 
df.EstimatedSalary.loc[df.EstimatedSalary<0]=np.nan 
df 
C:\Users\Ayyadurai\AppData\Local\Temp\ipykernel_5300\2580639570.py:1: S
ettingWithCopyWarning:  
A value is trying to be set on a copy of a slice from a DataFrame 
See the caveats in the documentation: https://pandas.pydata.org/pandas
docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy 
df.CustomerID.loc[df.CustomerID<0]=np.nan 
df.Bill.loc[df.Bill<0]=np.nan 
C:\Users\Ayyadurai\AppData\Local\Temp\ipykernel_5300\2580639570.py:2: S
ettingWithCopyWarning:  
A value is trying to be set on a copy of a slice from a DataFrame 
df.EstimatedSalary.loc[df.EstimatedSalary<0]=np.nan 
df['NoOfPax'].loc[(df['NoOfPax']<1) | (df['NoOfPax']>20)]=np.nan 
df 
C:\Users\Ayyadurai\AppData\Local\Temp\ipykernel_5300\2129877948.py:1: S
ettingWithCopyWarning:  
A value is trying to be set on a copy of a slice from a DataFrame 
See the caveats in the documentation: https://pandas.pydata.org/pandas
docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy 
df['NoOfPax'].loc[(df['NoOfPax']<1) | (df['NoOfPax']>20)]=np.nan 
df.Age_Group.unique() 
array(['20-25', '30-35', '25-30', '35+'], dtype=object) 
df.Hotel.unique() 
array(['Ibis', 'LemonTree', 'RedFox', 'Ibys'], dtype=object) 
#Using the inplace=True keyword in a pandas method changes the default behaviour such that the 
operation on the dataframe doesn't return anything, it instead 'modifies the underlying data 
df.Hotel.replace(['Ibys'],'Ibis',inplace=True) 
df.FoodPreference.unique 
<bound method Series.unique of 0           
1      
2          
3          
4    
5      
6    
7          
8      
9      
 Non-Veg 
 Veg 
 Veg 
Vegetarian 
 Non-Veg 
Vegetarian 
 Veg 
 Non-Veg 
 non-Veg 
Name: FoodPreference, dtype: object> 
veg 
df.FoodPreference.replace(['Vegetarian','veg'],'Veg',inplace=True) 
df.FoodPreference.replace(['non-Veg'],'Non-Veg',inplace=True) 
#Fillna is a Pandas function to fill the NA/NaN values with the specified method. 
# If column or feature is numerical continuous data then replace the missing(NaN) value by taking 
mean value. 
# If column or feature is numerical discrete data then replace  the missing(NaN) value by taking 
median value. 
# If column or feature is non-numerical i.e Categorical  data then  replace the missing(NaN) value by 
taking mode value. 
df.EstimatedSalary.fillna(round(df.EstimatedSalary.mean()),inplace=True) 
df.NoOfPax.fillna(round(df.NoOfPax.median()),inplace=True) 
df['Rating(1-5)'].fillna(round(df['Rating(1-5)'].median()), inplace=True)