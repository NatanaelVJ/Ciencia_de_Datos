import pandas as pd
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
df_abalone = pd.read_csv(url, header = None )


print(df_abalone)
