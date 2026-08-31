import numpy as np
import pandas as pd
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(root, 'data'))

cstmr = pd.read_csv("data/customers.csv")
def customer():
    print(cstmr.head())
    print("~"*80)
    print(cstmr.info())
    print("~"*80)
    print(cstmr.describe())
    print("~"*80)


customer()
