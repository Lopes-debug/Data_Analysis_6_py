import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from itertools import combinations
import efficient_apriori
from efficient_apriori import apriori

## Market Basket Analysis (MBA)

aisles = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto6\Scripts-06\dados\aisles\aisles.csv')
departments = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto6\Scripts-06\dados\departments\departments.csv')
prod_prior = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto6\Scripts-06\dados\order_products__prior\order_products__prior.csv')
prod_train = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto6\Scripts-06\dados\order_products__train\order_products__train.csv')
orders = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto6\Scripts-06\dados\orders\orders.csv')
products = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto6\Scripts-06\dados\products\products.csv')
sample_sub = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto6\Scripts-06\dados\sample_submission\sample_submission.csv')

print(aisles.head(2))
print(departments.head(2))
print(prod_prior.head(2))
print(prod_train.head(2))
print(orders.head(2))
print(products.head(2))
print(sample_sub.head(2))