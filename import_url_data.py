

url = "https://raw.githubusercontent.com/BACCHUS2333/Machine_Learning_Lasso_and_ridge_regression.github.io/main/College.csv"
#import data from this URL using requests
import pandas as pd
import io
import requests
s=requests.get(url).content
college_data=pd.read_csv(io.StringIO(s.decode('utf-8')))
