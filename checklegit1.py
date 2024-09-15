import pdfplumber
import pandas as pd
import json

path = 'test1.pdf'

with pdfplumber.open(path) as pdf:
    data = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)

data = data[1:]
df = pd.DataFrame(data)

df.columns = ['ID', 'DATE', 'AMOUNT', 'DESCRIPTION']

for col in df.columns:
    df[col] = df[col].str.replace('\n', ' ')

df['AMOUNT'] = df['AMOUNT'].str.replace('.', '').astype(float)

with open('test1.txt', 'w') as f:
    f.write(df.to_string())

df.to_csv('output1.csv', index=False)
df.to_json('output1.json', orient='records')

with open('output1.json') as f:
    file_data = json.load(f)

with open('output1.json', 'w') as f:
    json.dump(file_data, f, indent=4)