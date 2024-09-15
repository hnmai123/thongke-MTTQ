import pdfplumber
import pandas as pd
import json
import numpy as np

path = 'test3.pdf'

with pdfplumber.open(path) as pdf:
    data = []
    for page in pdf.pages[:1]:
        tables = page.extract_tables()
        for table in tables[:1]:
            data.extend(table)
            

data = data[1:]
df = pd.DataFrame(data)

df.columns = ['DATE', 'DEBT','AMOUNT', 'BALANCE', 'DESCRIPTION']
dict = {}
description = []

# df['AMOUNT'] = df['AMOUNT'].str.replace('.', '').astype(float)
# df['DEBT'] = df['DEBT'].str.replace('.', '').astype(float)
# df['BALANCE'] = df['BALANCE'].str.replace('.', '').astype(float)

for col in df.columns:
    for value in df[col]:
        if col == 'DATE':
            value = value.split('\n')
            value = [value[i:i+2] for i in range(0, len(value), 2)]
            dict[col] = value

        elif col == 'DESCRIPTION':
            value = value.split('\n')
            description.extend(value)
        else:
            value = value.split('\n')
            dict[col] = value


for key, _ in dict.items():
    print(len(dict[key]))

print(description)


test_frame = np.array([dict['DATE'], dict['DEBT'], dict['AMOUNT'], dict['BALANCE']])

with open('test3.txt', 'w') as f:
    f.write(df.to_string())

df.to_csv('output3.csv', index=False)
df.to_json('output3.json', orient='records')

with open('output3.json') as f:
    file_data = json.load(f)

with open('output3.json', 'w') as f:
    json.dump(file_data, f, indent=4)