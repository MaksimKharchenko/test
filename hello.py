import pandas as pd
df = pd.read_csv('acme_worksheet.csv')
print(df)
df = df.pivot(index = 'Employee Name', columns = 'Date', values = 'Work Hours' )
print(df)