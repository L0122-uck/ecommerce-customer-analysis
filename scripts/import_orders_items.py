import pandas as pd
from sqlalchemy import create_engine


file_path = r"D:\github_project\ecommerce\data\raw\olist_order_items_dataset.csv"


df = pd.read_csv(file_path)

print(df.head())
print(df.shape)


engine = create_engine(
    "mysql+pymysql://root:122000@localhost:3306/ecommerce_analysis"
)


df.to_sql(
    "order_items",
    con=engine,
    if_exists="append",
    index=False
)


print("order_items导入成功")