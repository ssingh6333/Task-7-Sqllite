# Task-7-Sqllite
# 🧩 Task 7 – Basic Sales Summary using SQLite and Python

### 🎯 Objective
The goal of this task was to extract and summarize basic sales information (like total quantity sold and total revenue per product) from a small SQLite database using Python.  
The data came from a CSV file containing detailed sales transactions.

---

### 🛠️ Tools and Libraries Used
- **Python 3**
- **SQLite3** (built-in database in Python, no installation required)
- **pandas** – for reading CSV files and handling tabular data
- **matplotlib** – for data visualization

---

### 📂 Dataset Description
The dataset was provided as `Sales data.csv` and includes:
| Column | Description |
|--------|--------------|
| OrderID | Unique order number |
| CusName / CustomerName | Name of the customer |
| ProductList | Product purchased |
| Quant | Quantity sold |
| PriceItem | Price per item |
| OrderDate | Date of the order |
| TotalAmount | Total sale amount |

---

### 🧠 Steps Performed

1. **Loaded the CSV file** into a pandas DataFrame (`pd.read_csv()`).
2. **Created a new SQLite database** (`sales_data.db`) using `sqlite3.connect()`.
3. **Stored the CSV data** into a table named `sales` using `df.to_sql()`.
4. **Executed SQL queries** inside Python to calculate:
   ```sql
   SELECT ProductList AS product,
          SUM(Quant) AS total_quantity,
          SUM(TotalAmount) AS total_revenue
   FROM sales
   GROUP BY ProductList;
