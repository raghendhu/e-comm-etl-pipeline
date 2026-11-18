#import requests
#response = requests.get('https://fakestoreapi.com/products')
#print(response.json())

import pandas as pd 
import requests

response = requests.get("https://fakestoreapi.com/products") 
raw_json = response.json() 

df = pd.json_normalize(raw_json, sep="_") 

df.to_csv("users_flattened.csv", index=False)
print("Converted JSON to CSV with columns:", list(df.columns))


