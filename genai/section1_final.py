import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

#heighest revenue by gold people
#  Gold members
gold_df = df[df["membership"] == "Gold"]

#  total by revenue city-wise
city_revenue = (
    gold_df
    .groupby("city")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

# City with highest total revenue from Gold members
print(city_revenue.head(1))


# heighest average order value cuisine-wise
cuisine_avg_order = (
    df
    .groupby("cuisine")["total_amount"]
    .mean()
    .sort_values(ascending=False)
)



# Cuisine with highest avg order value
print(cuisine_avg_order.head(1))

#distict user order more than 1000
#  total spending per user
user_total_spend = (
    df
    .groupby("user_id")["total_amount"]
    .sum()
)


#  users count with total spending > 1000
count_users = (user_total_spend > 1000).sum()

print(count_users)


#heighest total based on rating
import numpy as np

# Create rating bins with 0.5 difference
bins = np.arange(3.0, 5.5, 0.5)   

df["rating_range"] = pd.cut(
    df["rating"],
    bins=bins,
    right=False   
)

#total revenue per rating range
rating_revenue = (
    df
    .groupby("rating_range")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

# Rating range with highest total revenue
print(rating_revenue.head(1))


# Filter only Gold members
gold_df = df[df["membership"] == "Gold"]

# Calculate average order value city-wise
city_avg_order = (
    gold_df
    .groupby("city")["total_amount"]
    .mean()
    .sort_values(ascending=False)
)

# City with highest average order value
print(city_avg_order.head(1))

#distinct restaurant count and total revenue per cuisine
cuisine_stats = (
    df
    .groupby("cuisine")
    .agg(
        distinct_restaurants=("restaurant_id", "nunique"),
        total_revenue=("total_amount", "sum")
    )
)

#average revenue across cuisines
avg_revenue = cuisine_stats["total_revenue"].mean()

# cuisines with significant revenue (above average)
significant_cuisines = cuisine_stats[
    cuisine_stats["total_revenue"] > avg_revenue
]

# Sort by lowest restaurant count
result = significant_cuisines.sort_values("distinct_restaurants")


print(result.head(1))

#order by gold people

total_orders = len(df)

# No. orders placed by Gold members
gold_orders = len(df[df["membership"] == "Gold"])

gold_orders_percentage = round((gold_orders / total_orders) * 100)

print(gold_orders_percentage)


#heihghest revenue by combination
combinations = [
    ("Gold", "Indian"),
    ("Gold", "Italian"),
    ("Regular", "Indian"),
    ("Regular", "Chinese")
]

highest_revenue = 0
answer = ""

for membership, cuisine in combinations:
    revenue = df[(df['membership'] == membership) & (df['cuisine'] == cuisine)]['total_amount'].sum()
    if revenue > highest_revenue:
        highest_revenue = revenue
        answer = f"{membership} + {cuisine} cuisine"

print(f"heighest revenue combination: {answer}")
print(f"Revenue: ${highest_revenue:,.2f}")





#total oders by gold members

gold_orders_count = len(df[df['membership'] == 'Gold'])

print(f"Total orders by Gold members: {gold_orders_count}")



#hydrabad revenue
hyderabad_revenue = df[df['city'] == 'Hyderabad']['total_amount'].sum()
print(f"hybd revenue: {round(hyderabad_revenue)}")

#distinct user
distinct_users = df['user_id'].nunique()
print(f"distnict users: {distinct_users}")

# the average order value (rounded to 2 decimals) for Gold members
gold_avg = df[df['membership'] == 'Gold']['total_amount'].mean()
print(f"avg val for gold members: {round(gold_avg, 2)}")


high_rating_orders = len(df[df['rating'] >= 4.5])
print(f" high rating order : {high_rating_orders}")






# Filter for Gold members only
gold_df = df[df['membership'] == 'Gold']

# Find top revenue city among Gold members
city_revenue = gold_df.groupby('city')['total_amount'].sum()
top_city = city_revenue.idxmax()

# Count orders in that city for Gold members
orders_in_top_city = len(gold_df[gold_df['city'] == top_city])


print(f"order in top city: {orders_in_top_city}")




orders = pd.read_csv("orders.csv")
users = pd.read_json("users.json")

print("Orders columns:", orders.columns.tolist())
print("Users columns:", users.columns.tolist())




df = pd.read_csv("final_food_delivery_dataset.csv")
print(f"dataset length: {len(df)}")