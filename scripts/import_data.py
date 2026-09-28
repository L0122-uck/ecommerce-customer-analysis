import pandas as pd
from sqlalchemy import create_engine


# CSV路径
file_path = r"D:\github_project\ecommerce\data\raw\olist_customers_dataset.csv"


# 读取CSV
df = pd.read_csv(file_path)

print(df.head())
print(df.shape)


# MySQL连接
engine = create_engine(
    "mysql+pymysql://root:122000@localhost:3306/ecommerce_analysis"
)


# 导入MySQL
df.to_sql(
    "customers",
    con=engine,
    if_exists="append",
    index=False
)

print("导入成功")