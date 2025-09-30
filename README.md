# 🧴 Interactive Dashboard for Skincare Product Segmentation using K-Means Clustering
<br>

**Tool :** Jupyter Notebook <br>
**Programming Language :** Python <br>
**Libraries :** Pandas, NumPy, sklearn <br>
**Visualization :** Matplotlib, Seaborn, yellow-brick <br>

### Table of Contents
- [STAGE 0 Problem Statement](#stage-0-problem-statement)
  - [Introduction](#introduction)
  - [Goal](#goal)
  - [Objective](#objective)
  - [Workflow](#workflow)
- [STAGE 1 Exploratory Data Analysis](#stage-1-exploratory-data-analysis)
  - [Data Overview](#data-overview)
  - [Data Quality Assesment](#data-quality-assesment)
  - [Data Exploration](#data-exploration)
- [STAGE 2 Data Pre-processing](#stage-2-data-pre-processing)
- [STAGE 3 Visualization and Model Building](#stage-3-visualization-and-model-building)
  - [Brands Analysis](#brands-analysis)
  - [Determining Optimal Number of Clusters with Elbow Method](#determining-optimal-number-of-clusters-with-elbow-method)
  - [Data Exploration](#data-exploration)
- [Model Simulation using Streamlit](#model-simulation-using-streamlit)
- [Recommendations](#recommendations)
-----


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
  <img src="https://github.com/user-attachments/assets/5b510a98-1587-4e7d-bb17-2349f0b2e62c" alt="Workflow Skincare" width="500"/>
</p>

<p align="center"><b>Figure 2 — Skincare Product Price Boxplot</b></p>

These outliers are not anomalies but rather indicators of **premium and luxury products** that coexist with mass-market items. From a data perspective, the skewness and extreme values highlight the importance of applying techniques such as log transformation or robust scaling before clustering, so that the model is not overly influenced by extreme values. From a business standpoint, this confirms that the skincare market is diverse, with opportunities to serve both **budget-conscious consumers** through affordable products and niche customers through premium offerings.

<br>

**Correlation heatmap revealed the relationships between price, rating, and reviews**

The correlation heatmap provides an overview of the statistical relationships among the three key numerical features used in clustering: **price, average rating, and total reviews**. The visualization shows that the correlations between these variables are generally **weak to moderate**, which means each feature carries unique information for the model. Specifically, **price** has little to no correlation with either **average rating** or **total reviews**, suggesting that higher-priced products do not necessarily receive better ratings or a larger number of reviews. Meanwhile, there is a slightly stronger positive relationship between **average rating and total reviews**, indicating that products with higher ratings tend to attract more customer feedback, although this relationship is not strong enough to be conclusive.


<p align="center">
  <img src="https://github.com/user-attachments/assets/790be001-dddc-44c1-ae27-35e3d0927b08" alt="Workflow Skincare" width="500"/>
</p>

<p align="center"><b>Figure 3 — Correlation Between Variables</b></p>


From a data perspective, this weak correlation is important because it justifies the inclusion of all three features in the clustering model without introducing redundancy. Each variable provides distinct insights into product positioning **price** captures affordability or exclusivity, **rating** reflects customer satisfaction, and **reviews** indicate customer engagement and popularity. From a business standpoint, the heatmap confirms that consumer perceptions are not solely determined by price; instead, product quality and popularity play independent roles in shaping customer choices. This means companies can develop strategies that focus not only on premium pricing but also on building trust through positive customer experiences and encouraging more reviews to strengthen brand credibility.

<br>

## 📂 STAGE 2: Data Pre-processing

Missing Values per Feature

<p align="center">
  <img src="https://github.com/user-attachments/assets/ecc3d892-1ee1-4011-a64d-6495c0925fdb" alt="Workflow Skincare" width="500"/>
</p>

<p align="center"><b>Figure 4 — Missing Values per Feature</b></p>

<br>

## 📂 STAGE 3: Visualization and Model Building

**Brands Analysis**

The first chart shows the distribution of top brands within Cluster 1, which is primarily composed of affordable skincare products with relatively consistent characteristics. Among these brands, COSRX dominates the cluster with the highest frequency, followed by Etude and Nacific. Other brands such as Dear Klairs, Beautyblender, and The Body Shop also appear in notable counts. This distribution indicates that Cluster 1 represents a mix of K-beauty brands and established global names that are positioned in the affordable to mid-range segment. From a business perspective, brands in this cluster compete heavily on accessibility and variety. Companies targeting this segment can leverage competitive pricing strategies, product bundling, and strong distribution channels to maintain market share.

<p align="center">
  <img src="https://github.com/user-attachments/assets/855b5d18-ff4a-4823-b418-459970255faa" alt="Workflow Skincare" width="600"/>
</p>

<p align="center"><b>Figure 5 — Top brands identified 1</b></p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4bcc4379-a4d5-4c44-b77f-6826b6753181" alt="Workflow Skincare" width="600"/>
</p>

<p align="center"><b>Figure 6 — Top brands identified 2</b></p>

The second chart highlights the top brands within Cluster 2, which contains a broader spread of product types with higher variability in attributes. The most dominant brands in this cluster are Jacquelle and Eze-nails, followed by Etude, Holika Holika, and You Beauty. International and local brands coexist here, with strong representation from Scarlett Whitening and The Body Shop, suggesting this cluster captures a diverse consumer base. From a business perspective, Cluster 2 represents a more mixed-market environment, where both niche and mainstream brands compete. This suggests that companies operating in this segment need to differentiate through brand identity, innovation, and targeted campaigns rather than relying solely on price. The diversity of brands also reflects consumer openness to experiment with both local and international products in this category.

<br>

**Determining Optimal Number of Clusters with Elbow Method**

The Elbow Method was applied to identify the optimal number of clusters (k) for K-Means clustering. The chart above plots the distortion score (sum of squared distances from each point to its assigned cluster center) against the number of clusters. As the number of clusters increases, the distortion score decreases, but the rate of improvement slows down after a certain point. From the chart, the “elbow point” is observed at k = 4, where the distortion score drops significantly before the curve starts to flatten. This suggests that segmenting the skincare products into four clusters strikes a balance between underfitting (too few clusters) and overfitting (too many clusters).

<p align="center">
  <img src="https://github.com/user-attachments/assets/909cc6a1-ce37-4479-9daf-4e9897cd05da" alt="Workflow Skincare" width="600"/>
</p>

<p align="center"><b>Figure 7 — Elbow Method</b></p>

Identifying four distinct clusters provides a practical segmentation of the skincare product market. Each cluster potentially represents unique product groups, such as affordable mass-market products, mid-range brands, premium selections, and niche items. Using this segmentation, businesses can tailor their strategies for pricing, promotions, and brand positioning to better target the needs of different customer groups.


## 📂 Model Simulation using Streamlit

<p align="center">
  <img src="https://github.com/user-attachments/assets/63420ee3-5ce5-494a-a967-ed4920550efe" alt="Workflow Skincare" width="800"/>
</p>

<p align="center"><b>Figure 8 — Screenshot Part 1</b></p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/decb1847-11fe-4dce-a5ab-110e23543627" alt="Workflow Skincare" width="800"/>
</p>

<p align="center"><b>Figure 9 — Screenshot Part 2</b></p>

<br>

## 📂 Recommendations

The clustering analysis segmented skincare products into four distinct groups, each with unique characteristics and business implications. The first cluster represents mass market products, typically affordable items with high review counts, dominated by popular K-beauty and global brands. For this segment, businesses should focus on competitive pricing strategies, bundle promotions, and flash sales while expanding distribution through online marketplaces to attract price-sensitive consumers. The second cluster corresponds to mid-range popular brands, which show a balance between price and rating with relatively consistent demand and strong brand loyalty. To strengthen this position, loyalty programs such as membership benefits or cashback, combined with influencer campaigns involving mid-tier key opinion leaders (KOLs), can help maintain consumer trust and drive higher engagement. The third cluster highlights premium and niche products, which tend to have higher prices, fewer reviews, but strong ratings that reflect exclusivity and luxury positioning. For this group, companies should emphasize exclusive branding and storytelling to communicate premium value, targeting affluent customers through tailored campaigns such as beauty events and exclusive online or offline promotions. The fourth cluster captures a mixed or experimental segment, composed of diverse local and international brands with moderate performance. This segment is best approached through differentiation strategies, including continuous innovation, new product launches, and targeted campaigns to appeal to consumers who are open to trying a mix of local and global products.

This segmentation allows companies to adopt a multi-segment strategy, balancing volume sales from affordable products, building long-term loyalty in the mid-range, and securing niche profitability through premium offerings. By aligning promotions, pricing, and distribution with the unique profile of each segment, businesses can optimize resource allocation and strengthen their competitive advantage in the skincare market.
