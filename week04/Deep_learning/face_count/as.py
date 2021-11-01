# 데이터 출처 :https://www.kaggle.com/vin1234/count-the-number-of-faces-present-in-an-image/version/1
import os
import json
import pandas as pd

df = pd.read_csv("train/train.csv") 
#print(df.describe())
#print(df)

filenames = os.listdir('train/image_data')
sample_json1 = []
for i in filenames:
    if (i in df["Name"].values):
        a = int(df[df["Name"]==i]["HeadCount"].values[0])
        #print("a:",type(a))
        sample_json1.append(
            {
                'image_id' : i,
                'label' : a
            }
        )
    else:
        continue
#print(sample_json1)  
with open('data1.json', 'w') as outfile:
    json.dump(sample_json1, outfile, indent=4, sort_keys=True)
