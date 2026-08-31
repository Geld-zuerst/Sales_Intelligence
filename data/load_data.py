import pandas as pd

product = pd.read_csv("data/products.csv")
customers = pd.read_csv("data/customers.csv")
sales = pd.read_csv("data/sales.csv")

def customer():
    print(customers.head())
    print("~"*80)
    print(customers.info())
    print("~"*80)
    print(customers.describe())


def sale():
    print(sales.head())
    print("~"*80)
    print(sales.info())
    print("~"*80)
    print(sales.describe())


def product():
    print(product.head())
    print("~"*80)
    print(product.info())
    print("~"*80)
    print(product.describe())


# CALLING FUNCTIONS
a = customer()

# print(a)

if a.to_csv("a.csv"):
    print('exported')