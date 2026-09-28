import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import os

os.makedirs(
    "result/images",
    exist_ok=True
)

# MySQL连接
engine = create_engine(
    "mysql+pymysql://root:122000@localhost:3306/ecommerce_analysis"
)


# =========================
# 1. 月销售趋势
# =========================

sql_sales = """
SELECT
    DATE_FORMAT(o.order_purchase_timestamp,'%%Y-%%m') AS month,
    SUM(oi.price) AS sales
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;
"""


sales = pd.read_sql(sql_sales, engine)

plt.figure(figsize=(10,5))

plt.plot(
    sales["month"],
    sales["sales"]
)

plt.xticks(rotation=45)

plt.title(
    "Monthly Sales Trend"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Sales"
)

plt.tight_layout()

plt.savefig(
    "result/images/monthly_sales.png"
)

plt.close()


print("销售趋势图完成")

# =========================
# 2. 留存热力图
# =========================

sql_retention = """

WITH user_month AS
(
SELECT
    c.customer_unique_id,
    DATE_FORMAT(o.order_purchase_timestamp,'%%Y-%%m') AS order_month
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
),


first_month AS
(
SELECT
    customer_unique_id,
    MIN(order_month) AS first_month
FROM user_month
GROUP BY customer_unique_id
),


cohort AS
(
SELECT
    u.customer_unique_id,
    f.first_month,
    u.order_month,

    TIMESTAMPDIFF(
        MONTH,
        STR_TO_DATE(CONCAT(f.first_month,'-01'),'%%Y-%%m-%%d'),
        STR_TO_DATE(CONCAT(u.order_month,'-01'),'%%Y-%%m-%%d')
    ) AS month_diff

FROM user_month u

JOIN first_month f

ON u.customer_unique_id=f.customer_unique_id
)


SELECT
    first_month,
    month_diff,
    COUNT(DISTINCT customer_unique_id) AS users

FROM cohort

GROUP BY
    first_month,
    month_diff

ORDER BY
    first_month,
    month_diff;

"""


retention = pd.read_sql(
    sql_retention,
    engine
)


# 转成矩阵

retention_matrix = retention.pivot(
    index="first_month",
    columns="month_diff",
    values="users"
)


# 计算百分比

retention_rate = retention_matrix.divide(
    retention_matrix.iloc[:,0],
    axis=0
)


plt.figure(figsize=(12,6))


sns.heatmap(
    retention_rate,
    annot=True,
    fmt=".1%",
)


plt.title(
    "Customer Retention Cohort Analysis"
)


plt.xlabel(
    "Month After First Purchase"
)


plt.ylabel(
    "First Purchase Month"
)


plt.tight_layout()


plt.savefig(
    "result/images/retention_heatmap.png"
)


plt.close()


print("留存热力图完成")
# =========================
# 3. RFM 用户价值分析
# =========================

sql_rfm = """

SELECT
    c.customer_unique_id,

    COUNT(DISTINCT o.order_id) AS frequency,

    SUM(oi.price) AS monetary

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

JOIN order_items oi
ON o.order_id=oi.order_id

GROUP BY c.customer_unique_id;

"""


rfm = pd.read_sql(
    sql_rfm,
    engine
)


plt.figure(figsize=(8,5))


plt.scatter(
    rfm["frequency"],
    rfm["monetary"],
    alpha=0.5
)


plt.xlabel(
    "Purchase Frequency"
)


plt.ylabel(
    "Total Spending"
)


plt.title(
    "Customer Value Distribution"
)


plt.tight_layout()


plt.savefig(
    "result/images/rfm_distribution.png"
)


plt.close()


print("RFM分析图完成")
