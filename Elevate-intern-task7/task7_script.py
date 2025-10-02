import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect/Create the database
con = sqlite3.connect('sales_data.db')
cur = con.cursor()

# Drop sales table if exists
cur.execute('DROP TABLE IF EXISTS sales')

# Create sales table
cur.execute('CREATE TABLE sales(product TEXT, quantity INTEGER, price REAL)')

# Sample sales data

data = [
    ('Laptop', 5, 1200.00),
    ('Mouse', 25, 25.50),
    ('Keyboard', 15, 75.00),
    ('Monitor', 10, 300.75),
    ('Laptop', 3, 1150.00),
    ('Mouse', 30, 24.00),
    ('Webcam', 20, 55.00)
]

# Insert data
cur.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', data)

# Commit and close
con.commit()
con.close()
print("Database created and populated.")

# Reconnect to fetch and analyze
con = sqlite3.connect('sales_data.db')

# Query total revenue per product
sql_query = 'SELECT product, SUM(quantity * price) AS revenue FROM sales GROUP BY product'
df = pd.read_sql_query(sql_query, con)
con.close()

# Display the data fetched
print("Sales summary:")
print(df)

# Plot the chart

df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Sales Revenue')
plt.tight_layout()
plt.savefig('sales_chart.png')

print("Chart saved as sales_chart.png")
