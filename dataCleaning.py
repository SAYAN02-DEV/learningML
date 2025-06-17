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
    print("Download failed with status code:", response.status_code)
    exit()

# Read and display the dataset
housing = pd.read_csv(filename, sep='\t')
print(housing.head(5))
