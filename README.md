# 🧴 Interactive Dashboard for Skincare Product Segmentation using K-Means Clustering
<br>

**Tool :** Jupyter Notebook <br>
**Programming Language :** Python <br>
**Libraries :** Pandas, NumPy, sklearn <br>
**Visualization :** Matplotlib, Seaborn, yellow-brick <br>


## 📁 STAGE 0 : Problem Statement

### Introduction

The skincare industry is experiencing rapid growth with thousands of new products entering the market every year. Increasing competition requires companies to understand product characteristics and consumer behavior more deeply. Unfortunately, the abundance of skincare product data is often presented in static tables, making it difficult to analyze quickly and efficiently. This situation risks causing companies to miss opportunities in identifying the most popular products, recognizing market segments based on price, ratings, and reviews, and optimizing promotional strategies as well as inventory management. To address these challenges, a solution is needed that can transform raw data into actionable insights that are easy to understand and directly applicable to business strategies. Through the development of an **Interactive Dashboard for Skincare Product Segmentation**, companies can leverage the K-Means Clustering algorithm to group products into distinct segments such as mass market, mid-tier, and premium. This interactive dashboard allows management to analyze data in real-time, extract relevant insights, and make faster, more accurate, and data-driven decisions in navigating the dynamic skincare market.


### Goal 
The main goal of this project is to provide a **practical decision-support tool** in the form of an interactive dashboard that presents skincare product segmentation results using the K-Means Clustering algorithm. This tool is designed to help businesses move beyond static spreadsheets by offering **interactive visualizations** that can be easily explored by management to gain deeper market understanding.

### Objectives
To achieve the stated goal, this project is structured into several key objectives:

1. Perform **data preprocessing** on skincare product datasets, including cleaning, transformation, and normalization.

2. Apply **K-Means Clustering** to group products based on attributes such as price, ratings, and reviews.

3. Develop an **interactive dashboard using Streamlit** to visualize clustering results and support real-time data exploration.

4. Provide **business insights** on product distribution and consumer preferences to support marketing strategies and inventory management.



## 📂 Workflow  

<p align="center">
  <img src="https://github.com/user-attachments/assets/5fb107a9-1c3f-4492-b840-399b2a2c0332" alt="Workflow Skincare" width="900"/>
</p>

<p align="center"><b>Figure 1 — Workflow of Model Development</b></p>

## 📂 STAGE 1: Exploratory Data Analysis

### Data Overview
The dataset consists of 7,637 rows and 19 attributes, but only three main numerical features (price_by_combination, average_rating, total_reviews) were selected for clustering. <br>

Table 1 – Feature Description

| Feature                | Description                                        |
|------------------------|----------------------------------------------------|
| `product_name`         | Name of the skincare product                       |
| `brand_name`           | Brand of the product                               |
| `categories`           | Product category (e.g., toner, serum, moisturizer) |
| `price_by_combination` | Price of product in local currency                 |
| `average_rating`       | Average customer rating (scale 1–5)                |
| `total_reviews`        | Total number of product reviews                    |

<br>

### Data Quality Assesment
<br>
Table 2 — Data Quality Assessment Results


| Data Assessment     | Finding                                                                  | Handling                                                       |
|---------------------|---------------------------------------------------------------------------|----------------------------------------------------------------|
| Missing values      | Some missing values found in `price_by_combination` and `average_rating` | Imputed using **median** for numeric, **mode** for categorical |
| Duplicates          | No duplicate records detected                                             | No action required                                              |
| Irrelevant features | Columns such as `url`, and `description`                                 | Removed from dataset                                            |
| Inconsistent values | Minor formatting inconsistencies in categories                           | Standardized and normalized                                     |
| Outliers            | Extreme values found in product prices                                   | Retained (considered as part of market diversity)              |

<br>

### Data Exploration

**Showed skewness and outliers in product price distribution**

The boxplot illustrates the distribution of skincare product prices, showing that the data is **highly right-skewed**. Most skincare products are concentrated in the lower price range, particularly between **IDR 50,000 and IDR 500,000**, while only a small number of products are priced significantly higher. The presence of numerous **outliers** is clearly visible, with certain items reaching prices above **IDR 1,000,000** and even up to IDR **3,000,000**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5b510a98-1587-4e7d-bb17-2349f0b2e62c" alt="Workflow Skincare" width="400"/>
</p>

<p align="center"><b>Figure 2 — Skincare Product Price Boxplot</b></p>

These outliers are not anomalies but rather indicators of **premium and luxury products** that coexist with mass-market items. From a data perspective, the skewness and extreme values highlight the importance of applying techniques such as log transformation or robust scaling before clustering, so that the model is not overly influenced by extreme values. From a business standpoint, this confirms that the skincare market is diverse, with opportunities to serve both **budget-conscious consumers** through affordable products and niche customers through premium offerings.

<br>

**Correlation heatmap revealed the relationships between price, rating, and reviews**

The correlation heatmap provides an overview of the statistical relationships among the three key numerical features used in clustering: **price, average rating, and total reviews**. The visualization shows that the correlations between these variables are generally **weak to moderate**, which means each feature carries unique information for the model. Specifically, **price** has little to no correlation with either **average rating** or **total reviews**, suggesting that higher-priced products do not necessarily receive better ratings or a larger number of reviews. Meanwhile, there is a slightly stronger positive relationship between **average rating and total reviews**, indicating that products with higher ratings tend to attract more customer feedback, although this relationship is not strong enough to be conclusive.


<p align="center">
  <img src="https://github.com/user-attachments/assets/790be001-dddc-44c1-ae27-35e3d0927b08" alt="Workflow Skincare" width="400"/>
</p>

<p align="center"><b>Figure 3 — Correlation Between Variables</b></p>


From a data perspective, this weak correlation is important because it justifies the inclusion of all three features in the clustering model without introducing redundancy. Each variable provides distinct insights into product positioning **price** captures affordability or exclusivity, **rating** reflects customer satisfaction, and **reviews** indicate customer engagement and popularity. From a business standpoint, the heatmap confirms that consumer perceptions are not solely determined by price; instead, product quality and popularity play independent roles in shaping customer choices. This means companies can develop strategies that focus not only on premium pricing but also on building trust through positive customer experiences and encouraging more reviews to strengthen brand credibility.

<br>

## 📂 STAGE 2: Data Pre-processing
