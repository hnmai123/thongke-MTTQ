import pdfplumber
import pandas as pd
import json

path = 'test2.pdf'

with pdfplumber.open(path) as pdf:
    data = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)

data = data[2:]
df = pd.DataFrame(data)

df.columns = ['ID', 'DATE', 'DESCRIPTION', 'AMOUNT', 'NAME']

for col in df.columns:
    df[col] = df[col].str.replace('\n', ' ')

df['AMOUNT'] = df['AMOUNT'].str.replace('.', '').astype(float)

with open('test2.txt', 'w') as f:
    f.write(df.to_string())

df.to_csv('output2.csv', index=False)
df.to_json('output2.json', orient='records')

with open('output2.json') as f:
    file_data = json.load(f)

with open('output2.json', 'w') as f:
    json.dump(file_data, f, indent=4)