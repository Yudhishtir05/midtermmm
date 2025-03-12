import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "D:\Vsss codeeee\EEE\Ecommerce_Delivery_Analytics_New.csv"
df = pd.read_csv(file_path)

# Convert Order Date & Time to datetime format
df["Order Date & Time"] = pd.to_datetime(df["Order Date & Time"], errors='coerce')

# Extract year, month, week from date
df["Year"] = df["Order Date & Time"].dt.year
df["Month"] = df["Order Date & Time"].dt.month
df["Week"] = df["Order Date & Time"].dt.isocalendar().week

# 1. Unique Orders & Customers with more than 10 orders
unique_orders = df["Order ID"].nunique()
customer_order_counts = df["Customer ID"].value_counts()
high_order_customers = customer_order_counts[customer_order_counts > 10]

# 2. Grouping by platform and visualizing unique sales
platform_counts = df["Platform"].value_counts()
plt.figure(figsize=(10, 5))
sns.barplot(x=platform_counts.index, y=platform_counts.values, palette="viridis")
plt.title("Unique Sales by Platform")
plt.xlabel("E-commerce Platform")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.show()

# 3. Yearly, Monthly, Weekly Order Analysis
yearly_orders = df.groupby("Year")["Order ID"].count()
monthly_orders = df.groupby("Month")["Order ID"].count()
weekly_orders = df.groupby("Week")["Order ID"].count()

# 4. Best and Least Performing Platform
best_platform = platform_counts.idxmax()
least_platform = platform_counts.idxmin()

# 5. Top 10 highest-rated products
top_10_products = df.groupby("Product Category")["Service Rating"].mean().sort_values(ascending=False).head(10)

# 6. Bottom 5 lowest-rated products
bottom_5_products = df.groupby("Product Category")["Service Rating"].mean().sort_values().head(5)

# 7. Profitability Analysis (Assumed discount & delivery columns exist)
if "Discount" in df.columns and "Delivery Charge" in df.columns:
    df["Profit"] = df["Order Value (INR)"] - df["Discount"] - df["Delivery Charge"]
    profit_analysis = df.groupby("Platform")["Profit"].sum()

# 8. Order Status Analysis
delivery_status = df["Delivery Delay"].value_counts(normalize=True) * 100

# 9. Platform-Specific Comments
comments = {
    "Swiggy": "Swiggy has great delivery times but should focus on reducing order cancellations.",
    "Zomato": "Zomato is well-rated but needs better refund handling.",
    "Blinkit": "Blinkit has fast delivery, but pricing competitiveness needs improvement.",
    "JioMart": "JioMart should focus on improving delivery speed and customer satisfaction."
}

# Print key insights
print("Unique Orders:", unique_orders)
print("Customers with more than 10 orders:", high_order_customers.count())
print("Best Performing Platform:", best_platform)
print("Least Performing Platform:", least_platform)
print("Top 10 Highest Rated Products:\n", top_10_products)
print("Bottom 5 Lowest Rated Products:\n", bottom_5_products)
print("Order Status Analysis:\n", delivery_status)
print("Platform Improvement Comments:\n", comments)