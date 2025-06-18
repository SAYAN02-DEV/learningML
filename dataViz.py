import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv('IRIS.csv')
# print(data.iloc[:5])

'''
data.groupby('species').mean().plot(color = ['red', 'blue', 'black', 'green'], fontsize = 10.0, figsize = (4,4))
plt.show()
'''


'''
sns.pairplot(data, hue = 'species', size=3)
plt.show()
'''
'''
normal plotting using matlotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.plot(x, y, marker='o', color='blue', ls = '--')  # Line plot with circular markers
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
'''

# print(data.shape[0])
# print(data.columns.tolist())
# print(data.dtypes)

print(data.species.value_counts())


