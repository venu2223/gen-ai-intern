import pandas as pd


orders_df = pd.read_csv("orders.csv")
print(orders_df.head())


users_df = pd.read_json("users.json")
print(users_df.head())


import sqlite3

conn = sqlite3.connect("restaurants.db")
conn.execute("DROP TABLE IF EXISTS restaurants")
conn.commit()

with open("restaurants.sql", "r") as f:
    sql_script = f.read()

conn.executescript(sql_script)

restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)

print(restaurants_df.head())
orders_users_df = pd.merge(
    orders_df,
    users_df,
    on="user_id",
    how="left"
)
final_df = pd.merge(
    orders_users_df,
    restaurants_df,
    on="restaurant_id",
    how="left"
)
print(final_df.head())
print(final_df.columns)
final_df.to_csv("final_food_delivery_dataset.csv", index=False)

