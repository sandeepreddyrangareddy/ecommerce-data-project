import pandas as pd

# Load processed data
fact_orders = pd.read_csv("output/fact_orders.csv")
dim_products = pd.read_csv("output/dim_products.csv")
dim_customers = pd.read_csv("output/dim_customers.csv")

# Convert date
fact_orders["order_purchase_timestamp"] = pd.to_datetime(fact_orders["order_purchase_timestamp"])

# KPIs
total_revenue = fact_orders["revenue"].sum()
total_orders = fact_orders["order_id"].nunique()

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)

# Monthly revenue
fact_orders["order_month"] = fact_orders["order_purchase_timestamp"].dt.to_period("M")
monthly_revenue = fact_orders.groupby("order_month")["revenue"].sum()

monthly_revenue.to_csv("output/monthly_revenue.csv")

# Join for category analysis
analysis_df = fact_orders.merge(dim_products, on="product_id", how="left")

top_categories = analysis_df.groupby("product_category_name")["revenue"].sum().sort_values(ascending=False)

top_categories.to_csv("output/top_categories.csv")

print("Analysis complete!")
