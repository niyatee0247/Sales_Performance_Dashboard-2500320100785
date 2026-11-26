"""Reproducible analysis for Sales Performance Dashboard. Synthetic learning dataset."""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sales_transactions.csv"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(DATA)
raw_rows = len(df)
df = df.drop_duplicates(subset=['order_id']).copy()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['discount_pct'] = pd.to_numeric(df['discount_pct'], errors='coerce').fillna(0)
df = df.dropna(subset=['order_id','order_date','product_name','quantity','unit_price'])
df = df[(df.quantity > 0) & (df.unit_price >= 0) & df.discount_pct.between(0,100)]
df['gross_sales'] = df.quantity * df.unit_price
df['net_sales'] = df.gross_sales * (1 - df.discount_pct/100)
df['month'] = df.order_date.dt.to_period('M').astype(str)
print('Total net sales:', round(df.net_sales.sum(),2))
print('Orders:', df.order_id.nunique())
print('Units sold:', int(df.quantity.sum()))
print(df.groupby('product_name').net_sales.sum().nlargest(10))
print(df.groupby('month').net_sales.sum())
df.to_csv(OUT / "cleaned_data.csv", index=False)
qa = pd.DataFrame({"check":["raw_rows","clean_rows","removed_rows","duplicate_key_count"],"value":[raw_rows,len(df),raw_rows-len(df),raw_rows-len(df.drop_duplicates())]})
qa.to_csv(OUT / "data_quality_report.csv", index=False)
print("\\nSaved:", OUT / "cleaned_data.csv")
