import pandas as pd
import os 

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

new_row_1 = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_row_1

# new_row_2 = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
# df = df.append(new_row_2, ignore_index=True)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)
print("DataFrame saved to {}".format(file_path))    