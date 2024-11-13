import pandas as pd
file_path = 'desercion.xlsx'
data = pd.read_excel(file_path)
data.dropna(inplace=True)

head=data.head()
columns=data.columns

print(head)