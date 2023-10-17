import pandas as pd
import io 

with open('/Contracts.csv', 'rb') as f:
    bom = f.read(2)

if bom == b'\xff\xfe':
    print('File is encoded as UTF-16-LE')
elif bom == b'\xfe\xff':
    print('File is encoded as UTF-16-BE')
else:
    print('File does not have a BOM, so the version of UTF-16 is unknown')

with open('/Contracts.csv', 'rb') as f:
    data = f.read()
    decoded_data = data.decode('utf-16-le', errors='ignore')

df = pd.read_csv(io.StringIO(decoded_data), sep=';')
df.head(1)
df.to_csv('/contracts_decoded.csv', encoding='utf-8', sep = ';')
