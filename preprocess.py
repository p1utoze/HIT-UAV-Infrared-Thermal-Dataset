import pandas as pd
import numpy as np
import pathlib

df_train = pd.read_csv('train_merged.csv')
df_test = pd.read_csv('test_merged.csv')
df_val = pd.read_csv('val_merged.csv')

print(df_train['category_id'].value_counts())