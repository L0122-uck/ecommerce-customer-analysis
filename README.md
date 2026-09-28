# 电商用户留存与RFM分析项目
# E-commerce Customer Retention & RFM Analysis


## 项目介绍 | Project Overview

本项目基于 Brazilian E-Commerce Public Dataset 真实电商订单数据，
使用 MySQL + Python 对用户购买行为进行分析。

主要目标：

- 分析用户复购行为
- 分析用户留存情况
- 构建RFM用户价值分析模型


数据分析流程：

原始数据
→ MySQL数据库建表
→ SQL业务分析
→ Python数据可视化
→ 输出业务结论


---

## 技术栈 | Tech Stack

- SQL（MySQL）
- Python
- Pandas
- Matplotlib
- Seaborn


SQL技能：

- SELECT
- JOIN
- GROUP BY
- 聚合函数
- CTE
- 用户留存分析
- RFM分析


---

## 数据集

数据来源：

Brazilian E-Commerce Public Dataset


主要数据表：

- customers（用户信息）
- orders（订单信息）
- order_items（商品订单信息）


数据规模：

- 99k+订单
- 99k+用户


---

## 分析内容


### 1. 用户复购分析

分析用户购买次数以及重复购买行为。


SQL：
sql/01_repeat_purchase.sql


---

### 2. 用户留存分析（Cohort Analysis）

根据用户首次购买月份划分用户群体，
分析不同月份用户后续活跃情况。


结果：

![Retention Heatmap](result/images/retention_heatmap.png)


---

### 3. RFM用户价值分析

基于：

- R（Recency）：最近一次购买时间
- F（Frequency）：购买频率
- M（Monetary）：消费金额


分析不同价值用户群体。


结果：

![RFM](result/images/rfm_distribution.png)


---

### 4. 销售趋势分析


分析月度销售变化趋势。


结果：

![Sales](result/images/monthly_sales.png)



---

## 项目结构
ecommerce/

├── data/
├── sql/
├── scripts/
├── result/
├── analysis_visualization.py
└── README.md


---

## 分析结论

- 大部分用户购买次数较少，存在提升复购率的空间；
- 少量高价值用户贡献较高消费金额；
- 用户留存率随着首次购买时间增加逐渐下降；
- RFM模型可以帮助识别不同价值用户群体。


---

## 后续优化

- 增加用户流失预测模型
- 使用Power BI/Tableau制作交互式看板
- 进行用户生命周期价值（CLV）分析