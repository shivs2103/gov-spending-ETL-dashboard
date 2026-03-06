import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="Gov Data Analytics Platform", layout="wide")


# Load Data
df = pd.read_csv("../data/raw/gov_spending.csv")
df.columns = df.columns.str.strip()

# Sidebar Filters
st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", sorted(df["year"].unique()))
filtered_year = df[df["year"] == year]

state = st.sidebar.selectbox("Select State", sorted(filtered_year["state"].unique()))
filtered = filtered_year[filtered_year["state"] == state]

# Title
st.title("Enterprise Government Data Analytics System")

st.markdown("---")

# KPI Section
col1, col2, col3 = st.columns(3)

total_spending = filtered["amount_spent"].sum()
total_beneficiaries = filtered["beneficiaries"].sum()
avg_spending = filtered["amount_spent"].mean()

col1.metric("Total Spending", f"₹ {total_spending:,.0f}")
col2.metric("Total Beneficiaries", f"{total_beneficiaries:,}")
col3.metric("Average Scheme Spending", f"₹ {avg_spending:,.0f}")

st.markdown("---")

# State-wise Overall Comparison
st.subheader("🏛 Overall Spending by State (Selected Year)")
state_summary = filtered_year.groupby("state")["amount_spent"].sum()
st.bar_chart(state_summary)

st.markdown("---")

# Scheme-wise Breakdown
st.subheader("📌 Scheme-wise Spending (Selected State)")
scheme_summary = filtered.groupby("scheme")["amount_spent"].sum()
st.bar_chart(scheme_summary)

st.markdown("---")

# Year-wise Trend
st.subheader("📈 Year-wise Spending Trend")
year_trend = df.groupby("year")["amount_spent"].sum()
st.line_chart(year_trend)

st.markdown("---")

st.caption("Built using Python ETL, Spark Processing, Star Schema Warehouse & Streamlit Dashboard")