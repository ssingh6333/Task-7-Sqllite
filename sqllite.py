import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Read your CSV file
df = pd.read_csv("Sales data.csv")

# Create SQLite database and save table
conn = sqlite3.connect("sales_data.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# Run SQL query
query = """
SELECT ProductList AS product, 
       SUM(Quant) AS total_quantity, 
       SUM(TotalAmount) AS total_revenue
FROM sales
GROUP BY ProductList
"""
summary = pd.read_sql_query(query, conn)
print(summary)

# Plot
summary.plot(kind='bar', x='product', y='total_revenue', color='skyblue')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue (₹)")
plt.tight_layout()
plt.show()

plt.savefig("sales_chart.png")

conn.close()
