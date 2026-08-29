import pandas as pd
import os

data_dir = os.path.dirname(os.path.abspath(__file__))


csv_files = []
for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        csv_files.append(file)


dataframes = {}
for csv_file in csv_files:
    file_path = os.path.join(data_dir, csv_file)
    df = pd.read_csv(file_path)
    dataframes[csv_file] = df
    print("Loaded " + csv_file + ": " + str(df.shape))


for name in dataframes:
    df = dataframes[name]
    print("\n" + name + ":")
    print(df.head())
 