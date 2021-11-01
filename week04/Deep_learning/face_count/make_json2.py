#create the sample file
import os
import json
import pandas as pd
filenames = os.listdir('face_count/train/image_data')
sample_json1 = []
df = pd.read_csv("face_count/train/train.csv") 

for i in filenames:
    sample_json1.append(
   {
    'image_id': i,
    'label': 'Cat' if 'cat' in i else 'Dog'
    }
    )

    
with open('data.json1', 'w') as outfile:
    json.dump(sample_json1, outfile, indent=4, sort_keys=True)
