import numpy as np
import pandas as pd
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(root, 'data'))

sls = pd.read_csv("data/sales.csv")

def info_sales():
    print(sls.head())
    print("~"*80)
    print(sls.info())
    print("~"*80)
    print(sls.describe())
    print("~"*80)


# Call Function
info_sales()