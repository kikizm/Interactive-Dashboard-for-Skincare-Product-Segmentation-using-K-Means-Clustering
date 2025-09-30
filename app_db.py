import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

st.set_page_config(page_title="Skincare Dashboard", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
DATA_PATH = "Sociolla_cluster(new).csv"

@st.cache_data
def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

try:
    df = load_data()
except:
    st.error("⚠️ Gagal load CSV. Pastikan file ada di folder data/")
    st.stop()

# -----------------------------
# Mapping kolom standar
# -----------------------------
def find_col(df, keywords):
    for kw in keywords:
        matches = [c for c in df.columns if kw in c]
        if matches:
            return matches[0]
    return None

mapping = {
    "brand_name": find_col(df, ["brand"]),
    "product_name": find_col(df, ["product"]),
    "price": find_col(df, ["price"]),
    "rating": find_col(df, ["rating"]),
    "reviews": find_col(df, ["review"])
}

df_work = df.copy()
for std, orig in mapping.items():
    if orig:
        df_work[std] = df_work[orig]
    else:
        df_work[std] = np.nan

# Pastikan numerik
for col in ["price", "rating", "reviews"]:
    df_work[col] = pd.to_numeric(df_work[col], errors="coerce")

# -----------------------------
# Clustering otomatis
# -----------------------------
if "cluster" not in df_work.columns:
    scaler = StandardScaler()
    X = scaler.fit_transform(df_work[["price","rating","reviews"]].fillna(0))
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df_work["cluster"] = kmeans.fit_predict(X)

# -----------------------------
# KPI Cards di atas
# -----------------------------
st.title("💄 Skincare Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Products", f"{df_work.shape[0]:,}")
col2.metric("Brands", f"{df_work['brand_name'].nunique():,}")
col3.metric("Clusters", f"{df_work['cluster'].nunique():,}")
col4.metric("Reviews", f"{int(df_work['reviews'].sum(skipna=True)):,}")

st.markdown("---")

# -----------------------------
# 2 Kolom Visualisasi Utama
# -----------------------------
col_left, col_right = st.columns(2)

# Donut Chart: distribusi cluster
with col_left:
    st.subheader("Proporsi Produk per Segmen")
    fig_donut = px.pie(
        df_work, names="cluster", hole=0.4,
        title="Proporsi Produk per Cluster",
        color="cluster"
    )
    st.plotly_chart(fig_donut, use_container_width=True)

# Line Chart: trend avg price per cluster
with col_right:
    st.subheader("Price & Reviews Overview by Cluster")
    cluster_stats = df_work.groupby("cluster").agg({
        "price": "mean",
        "reviews": "mean"
    }).reset_index()

    fig_line = px.line(
        cluster_stats, x="cluster", y=["price","reviews"],
        markers=True, title="Line Chart — Avg Price & Reviews by Cluster"
    )
    st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")

# -----------------------------
# Bar Chart: Top Brands across Clusters
# -----------------------------
st.subheader("Top Brands Across Clusters")
groups = df_work.groupby(["cluster","brand_name"]).size().reset_index(name="count")
top_brands = groups.groupby("brand_name")["count"].sum().reset_index().sort_values("count", ascending=False).head(10)
top_merge = groups.merge(top_brands[["brand_name"]], on="brand_name")

fig_bar = px.bar(
    top_merge, x="brand_name", y="count", color="cluster",
    barmode="group", title="Top 10 Brands across Clusters"
)
fig_bar.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_bar, use_container_width=True)