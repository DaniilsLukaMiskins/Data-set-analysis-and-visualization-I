# The basic overview of the dataset, EDA:
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if not os.path.exists("diabetes_risk_dataset.csv"):
    print("File not found.")

diabetes_filepath = "diabetes_risk_dataset.csv"
diabetes_data = pd.read_csv(diabetes_filepath, index_col="diabetes_risk_category")
# see the first rows of the dataset
print(diabetes_data.head())
plt.figure(figsize=(16,6))
sns.barplot(x="diabetes_risk_category", y="sugar_intake_grams_per_day", data=diabetes_data)
plt.show()
# We can clearly see that the sugar intake is considerably higher for the high risk category and prediabetes which confirms 
# our hypothesis about the correlation between sugar intake and diabetes risk.

# Lets build a graph with physical activity level and diabetes risk category to see the dependency.

plt.figure(figsize=(16,6))
sns.barplot(x="physical_activity_level", y="fasting_glucose_level", data=diabetes_data, hue="diabetes_risk_category")
plt.show()
# From this graph we can see that patients with high physical activity level have the lowest
#  fasting glucose level and noone of them are in high risk diavetes risk category.
# Conclusion if you want to reduce your diabetes risk, you should increase your physical activity level.

sns.lineplot(x="age", y="bmi", data=diabetes_data, hue="diabetes_risk_category")
plt.show()
# we can see that the weight is a sign of diabetes risk, the higher the weight the higher the diabetes risk category.

sns.boxplot(x="gender", y="sleep_hours", data=diabetes_data, hue="diabetes_risk_category")
plt.show()
# This graph shows that sleep hours are significant factor
#  in diabests risk, since sleeping 7.5 hours is a serious sign of diabetes risk.



print(diabetes_data.info())
print(diabetes_data.describe())


