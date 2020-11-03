import numpy as np

#Calculating the Median
test_scores = [12, 99, 86, 87, 88, 45, 87, 94, 78, 77, 85, 86]
my_median = np.median(test_scores)
print("the median is: ", my_median)

#Calculating the Mean
my_mean = np.mean(test_scores)
print("The mean is:", my_mean)

#Calculating The Mode
from scipy import stats
my_mode = stats.mode(test_scores)
print("The mode is:", my_mode)

#Calculating Range
my_range = np.ptp(test_scores)
print("The range is:", my_range)

#Calculating iNTER-QUARTILE range
x = np.percentile(test_scores, 75)
print("The 75% percentile for the marks is: ", x)

#Calculating Variance
x = np.var(test_scores)
print("The variance of the marks is :", x)

#Standard divviation
my_std = np.std(test_scores)
print("The standard deviation is :", my_std)

#Data Analysis
import matplotlib.pyplot as plt

girls_age = [19, 24, 19, 17, 50]
girls_names = ["Skyler", "Amber", "Zoe", "Lelethu", "Sesethu"]
x_pos = [i for i, _ in enumerate(girls_names)]
#labels on the x-axis
#labeling and visuals
plt.bar(x_pos, girls_age, color='green')
plt.xlabel("Girls Names")
plt.ylabel("Girls Ages")
plt.xticks(x_pos, girls_names)
plt.show()
