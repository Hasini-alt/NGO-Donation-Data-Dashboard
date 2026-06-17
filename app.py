import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("NGO Donation Data Dashboard")

# Load dataset
df = pd.read_csv("data/donations.csv")

# Show dataset
st.subheader("Donation Dataset")
st.dataframe(df)

# Total donations
st.metric("Total Donations", f"₹{df['Amount'].sum()}")

# Category-wise donations
st.subheader("Category-wise Donations")
category_sum = df.groupby("Category")["Amount"].sum()

fig, ax = plt.subplots()
ax.bar(category_sum.index, category_sum.values)
plt.xticks(rotation=45)
plt.ylabel("Amount")
st.pyplot(fig)

# Monthly trend
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
monthly = df.groupby("Month")["Amount"].sum()

st.subheader("Monthly Donation Trend")

fig2, ax2 = plt.subplots()
ax2.plot(monthly.index, monthly.values, marker='o')
plt.xlabel("Month")
plt.ylabel("Amount")
st.pyplot(fig2)

# Pie chart
st.subheader("Donation Share")

fig3, ax3 = plt.subplots()
ax3.pie(category_sum, labels=category_sum.index, autopct="%1.1f%%")
st.pyplot(fig3)