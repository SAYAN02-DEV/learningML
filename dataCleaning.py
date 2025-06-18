import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from scipy.stats import norm
from scipy import stats
import requests

# Download the data using requests (standard Python)
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/Ames_Housing_Data1.tsv"
filename = "Ames_Housing_Data1.tsv"

response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
else:
    print("Download failed with status code :", response.status_code)
    exit()

# Read and display the dataset
housing = pd.read_csv(filename, sep='\t')
# print(housing.head(5))

# housing.info()
# print(housing["SalePrice"].describe())
# print(housing["Sale Condition"].value_counts())

print("Skewness before normalizing: %f" % housing['SalePrice'].skew())

log_transformed = np.log(housing['SalePrice'])

#this plot show the right side has a longer tail
graph = sns.displot(housing['SalePrice'])
# graph.figure.canvas.manager.set_window_title("Original SalePrice Distribution")

# this plot normalize that making the graph bell shaped
graph2 = sns.displot(log_transformed)
# graph2.figure.canvas.manager.set_window_title("Log-Transformed SalePrice Distribution")


# print("Skewness after normalizing: %f" %(log_transformed).skew())
# plt.show()

#handling duplicates

duplicate = housing[housing.duplicated(['PID'])]
print(duplicate)