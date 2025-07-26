import pandas as pd
import os

data={
    'Name':['rahul','monk','project'],
    'city':['bankok','munmbai','chennai'],
    'age':[23,45,67]
}
df=pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#define the file path

file_path= os.path.join(data_dir,'sample_data.csv')

#save the datafram to csv
df.to_csv(file_path,index=False)
print(f"csv filed saved to {file_path}")