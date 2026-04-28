import pandas as pd
from load_data import load_data

def transform():
    customers, orders, order_items, products = load_data()

    # Clean products
    products["product_category_name"] = products["product_category_name"].fillna("unknown")

    # Create dimension tables
    dim_customers = customers[[
        "customer_id",
        "customer_unique_id",
        "customer_city",
        "customer_state"
    ]].drop_duplicates()

    dim_products = products[[
        "product_id",
        "product_category_name"
    ]].drop_duplicates()

    # Join tables
    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(order_items, on="order_id", how="left")
    df = df.merge(products, on="product_id", how="left")

    # Create fact table
    fact_orders = df[[
        "order_id",
        "customer_id",
        "product_id",
        "seller_id",
        "order_purchase_timestamp",
        "order_status",
        "price",
        "freight_value"
    ]].copy()

    fact_orders["revenue"] = fact_orders["price"]
    fact_orders["total_value"] = fact_orders["price"] + fact_orders["freight_value"]

    # Convert dates
    fact_orders["order_purchase_timestamp"] = pd.to_datetime(
        fact_orders["order_purchase_timestamp"], errors="coerce"
    )

    # Save outputs
    dim_customers.to_csv("output/dim_customers.csv", index=False)
    dim_products.to_csv("output/dim_products.csv", index=False)
    fact_orders.to_csv("output/fact_orders.csv", index=False)

    print("Data transformation complete!")

if __name__ == "__main__":
    transform()
