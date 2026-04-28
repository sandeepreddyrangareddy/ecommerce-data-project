import pandas as pd

def load_data():
    customers = pd.read_csv("data/olist_customers_dataset.csv")
    orders = pd.read_csv("data/olist_orders_dataset.csv")
    order_items = pd.read_csv("data/olist_order_items_dataset.csv")
    products = pd.read_csv("data/olist_products_dataset.csv")

    return customers, orders, order_items, products
