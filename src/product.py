import numpy as np
import pandas as pd
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(root, 'data'))
prd = pd.read_csv("data/products.csv")

def info_product():
    print("="*80)
    print(prd.head())
    print("~"*80)
    print(prd.info())
    print("~"*80)
    print(prd.describe())
    print("~"*80)
    print("="*80)

def start_product():
    print("="*80)
    print(prd[['Product_ID','Product_Name','Brand','Cost_Price']])
    print("="*80)
    print(prd.groupby("Brand")["Cost_Price"].mean())
    print("="*80)

        
# Call Functions
info_product()
start_product()