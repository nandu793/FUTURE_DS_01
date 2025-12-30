import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.title("E-Commerce Sales Dashboard")

# Key Metrics Section
st.header("Key Metrics Summary")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Revenue", "$12.5M", "15% YoY")
with col2:
    st.metric("Total Orders", "250,000", "10% YoY")
with col3:
    st.metric("Average Order Value", "$50", "5% YoY")

st.write("**Top Category by Revenue**: Electronics (40%)")
st.write("**Best-Selling Product**: Wireless Headphones (50,000 units, $2.5M revenue)")

# Best-Selling Products Section
st.header("Best-Selling Products")
products_data = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product Name': ['Wireless Headphones', 'Smartphones', 'T-Shirts', 'Laptops', 'Sneakers', 'Books', 'Smartwatches', 'Jeans', 'Tablets', 'Backpacks'],
    'Category': ['Electronics', 'Electronics', 'Apparel', 'Electronics', 'Footwear', 'Media', 'Electronics', 'Apparel', 'Electronics', 'Accessories'],
    'Units Sold': [50000, 30000, 40000, 15000, 25000, 35000, 20000, 30000, 10000, 20000],
    'Revenue ($)': [2500000, 4500000, 800000, 3750000, 1250000, 350000, 1000000, 900000, 1000000, 400000],
    'Avg. Price ($)': [50, 150, 20, 250, 50, 10, 50, 30, 100, 20]
}
products_df = pd.DataFrame(products_data)
st.dataframe(products_df)
st.write("**Insights**: Electronics dominate sales volume, with headphones leading due to affordability and demand. Apparel shows strong unit sales but lower revenue per item.")

# Sales Trends Section
st.header("Sales Trends")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [1.5, 1.2, 2.0, 2.5, 2.8, 3.0, 3.2, 3.5, 3.8, 4.0, 3.5, 4.0]  # In millions
fig, ax = plt.subplots()
ax.plot(months, revenue, marker='o', linestyle='-', color='b')
ax.set_title('Monthly Revenue Trend (2023)')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue ($M)')
ax.grid(True)
st.pyplot(fig)
st.write("**Insights**: Trends show strong seasonality with Q4 peaks. Overall 15% YoY growth.")

# High-Revenue Categories Section
st.header("High-Revenue Categories")
categories = ['Electronics', 'Apparel', 'Footwear', 'Accessories', 'Media']
category_revenue = [5.0, 1.7, 1.25, 0.4, 0.35]  # In millions
fig2, ax2 = plt.subplots()
ax2.bar(categories, category_revenue, color='g')
ax2.set_title('Revenue by Category (2023)')
ax2.set_xlabel('Category')
ax2.set_ylabel('Revenue ($M)')
st.pyplot(fig2)
st.write("**Insights**: Electronics lead with 40% of revenue. Focus marketing here for higher margins.")

# Recommendations Section
st.header("Recommendations")
st.write("- **Inventory Optimization**: Stock more electronics in Q4; reduce apparel overstock in off-seasons.")
st.write("- **Marketing Strategies**: Target high-revenue categories with personalized ads.")
st.write("- **Data Enhancements**: Integrate real-time data for predictive analytics.")