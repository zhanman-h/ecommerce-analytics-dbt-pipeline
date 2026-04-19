import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

NUM_RECORDS = 1000
ERROR_PERCENTAGE = 0.07

categories = ["Fashion & Accessories", "Consumer Electronics", 
              "Food & Beverage", "Health & Beauty", "Home & Garden", 
              "Pet Care & Supplies", "Media & Books"]

payment_methods = ["Credit and Debit Cards", "Digital Wallets", "Bank Transfers",
                   "BNPL Services", "Cryptocurrency", "Cash on Delivery"]

order_status = ["Shipped", "In Transit", "Delivered", "Cancelled"]

def generate_data():
    data = []

    for i in range(NUM_RECORDS): 
        data.append({
            "order_id": f"ORD{i+1}",
            "customer_id": f"CUS{random.randint(1, 500)}",
            "product_id": f"P{random.randint(1, 300)}",
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(10.0, 500.0), 2),
            "product_category": random.choice(categories),
            "payment_method": random.choice(payment_methods),
            "order_date": fake.date_between(start_date="-1y", end_date="today"),
            "order_status": random.choice(order_status)
        })
    
    df = pd.DataFrame(data)
    
    inject_errors(df)

    df.to_csv("ecommerce_sales_data.csv", index = False)
    print("CSV file generated successfully.")

def inject_errors(df):
    num_errors = int(len(df) * ERROR_PERCENTAGE)

    for _ in range(num_errors):
        row = random.randint(0, len(df) - 1)
        error_type = random.choice([
            "null_customer",
            "negative_quantity",
            "invalid_price",
            "future_date",
            "invalid_payment_method",
            "duplicate_transaction"
        ])

        if error_type == "null_customer":
            df.at[row, "customer_id"] = None

        elif error_type == "negative_quantity":
            df.at[row, "quantity"] = -random.randint(1, 5)

        elif error_type == "invalid_price":
            df.at[row, "price"] = -random.uniform(1, 100)

        elif error_type == "future_date":
            df.at[row, "order_date"] = datetime.now() + timedelta(days=30)

        elif error_type == "invalid_payment_method":
            df.at[row, "payment_method"] = "Invalid Payment"

        elif error_type == "duplicate_order":
            df.at[row, "order_id"] = "ORD1"

if __name__ == "__main__":
    generate_data()