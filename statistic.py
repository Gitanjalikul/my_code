'''
Here, I have calculated mean, median, mode, variance of each column present 
in a csv file(maize_pheno.csv)
'''

import pandas as pd 
data = pd.read_csv("maize_pheno.csv") #creating dataframe
print(data.head())
print(data.describe()) #to get statistics
mean_col1 = data["HT"].mean() #calculate mean using pandas
print(mean_col1)

#mean calculation of first column from scratch
add_HT = sum(data["HT"])
total_items_HT = (data["HT"].count())
mean_col1 = add_HT/total_items_HT
print(mean_col1)

#to calculate mean of all columns
for col in data.columns[1:]:
    add_col = sum(data[col]) 
    total = data[col].count()
    if total != 0:
        mean_col = add_col/total
        print(f"Mean of column {col} is:", mean_col)
    else:
        print("cannot divide by 0")

#calculate mode of 1st column
mode_col1 = data["HT"].mode()[0]
print("mode is", mode_col1)
freq_col1 = data["HT"].value_counts().iloc[0]

print(f"Mode of column 'HT' is: {mode_col1} with a frequency of {freq_col1}")

#calculate mode of all columns
for col in data.columns[1:]:
    mode_col = data[col].mode()[0]
    freq_col = data[col].value_counts().iloc[0]
    print(f"mode of column {col} is {mode_col} with a frequence of {freq_col}")

#calculate median of data for all columns
for col in data.columns[1:]:
    d = data[col].sort_values()
    n = d.count()
    if n%2==0:
        median_col = (d.iloc[n//2]+d.iloc[(n//2)+1])/2 
    elif n%2 != 0:
        median_col = d.iloc[(n+1)//2]
    else:
        print("something went wrong")
    print(f"median of column {col} is {median_col}")

print(data["HT"].median())

#variance calculation from scratch
mean_HT= data["HT"].mean()
diff= data["HT"]- mean_HT
sq_diff= diff**2
var= sq_diff.mean()
print(var)

#variance calculation using numpy
import numpy as np 
var = np.var(data["HT"])
print(var)

#variance calculation for all columns
for col in data.columns[1:]:
    mean_col = data[col].mean()
    diff= data[col]-mean_col
    sq_diff = diff**2
    var = sq_diff.mean()
    print(f"variance of column {col} is {var}")

print(np.std(data["HT"]))

for col in data.columns[1:]:
    mean_col = data[col].mean()
    diff= data[col]-mean_col
    sq_diff = diff**2
    var = sq_diff.mean()
    std_dev = np.sqrt(var)
    print(f"standard deviation of column {col} is {std_dev}")

# Perform one-way ANOVA
import pandas as pd
import scipy.stats as stats

f_statistic, p_value = stats.f_oneway(data['HT'], data['FT'], data['YLD'])
print("F-statistic:", f_statistic)
print("P-value:", p_value)

