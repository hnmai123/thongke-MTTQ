import pdfplumber
import pandas as pd
import json

path = 'test3.pdf'

with pdfplumber.open(path) as pdf:
    data = []
    for page in pdf.pages[:1]:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)

data = data[1:]
df = pd.DataFrame(data)

df.columns = ['DATE', 'DEBT','AMOUNT', 'BALANCE', 'DESCRIPTION']

for col in df.columns:
    df[col] = df[col].str.replace('\n', ' ')

df['AMOUNT'] = df['AMOUNT'].str.replace('.', '').astype(float)
df['DEBT'] = df['DEBT'].str.replace('.', '').astype(float)
df['BALANCE'] = df['BALANCE'].str.replace('.', '').astype(float)

with open('test3.txt', 'w') as f:
    f.write(df.to_string())

df.to_csv('output3.csv', index=False)
df.to_json('output3.json', orient='records')

with open('output3.json') as f:
    file_data = json.load(f)

with open('output3.json', 'w') as f:
    json.dump(file_data, f, indent=4)