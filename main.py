# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql_query("""
SELECT e.firstName, e.lastName, e.jobTitle
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = "Boston"
""", conn)
print(df_boston)
# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql_query("""
SELECT o.*
FROM offices o
LFET JOIN employees e ON o.offieCode = e.officeCode
WHERE e.employeeNumber IS NULL
""", conn)
print(df_zero_emp)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql_query("""
SELECT e.firstName, e.lastName, o.city, o.state
FROM employees e
LEFT JOIN offices o ON e.officeCode = officeCode
ORDER BY e.firstName, e.lastName
""", conn)
print(df_employee)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql_query("""
SELECT c.contractFirstName, c.contactLastName,c.phone, c.salesRepEmployeeNumber
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber
WHERE o.orderNumber IS NULL
ORDER BY c.contactLastName
""",conn)
print(df_contacts)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql_query("""
SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
ORDER BY CAST(p.amount AS REAL) DESC
""", conn)
print(df_payment)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql_query("""
SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) AS numcustomers
FROM employees e
JOIN customers c ON e.employeeNu,ber = c.salesRepEmployeeNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
HAVING AVG(c.creditLimit) > 90000
ORDER BY numcustomers DESC
""", conn)
print(df_credit)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql_query("""
SELECT p.productName,
       COUNT(od.orderNumber) AS numorders,
       SUM(od.quantityOrdered) AS totalunits
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
GROUP BY p.productName
ORDER BY totalunits DESC
""", conn)
print(df_product_sold)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql_query("""
SELECT p.productName, p.productCode, COUNT(DISTINCT o.customerNumber) AS numpurchasers
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON  od.orderNumber = o.orderNumber
GROUP BY p.productName, p.productCode
ORDER BY numpurchasers DESC
""", conn)
print(df_total_customers)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql_query("""
SELECT o.officode, o.city, COUNT(c.customerNumber) AS n_customers
FROM offices o
LEFT JOIN employees e ON o.officeCode = e.officeCode
LEFT JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY o.officeCode, o.city
ORDER BY n_customers DESC
""", conn)
print(df_customers)

# STEP 10
# Replace None with your code
df_under_20 = df_under_20 = pd.read_sql_query("""
SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders ord ON c.customerNumber = ord.customerNumber
JOIN orderdetails od ON ord.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
WHERE p.productCode IN (
    SELECT p2.productCode
    FROM products p2
    JOIN orderdetails od2 ON p2.productCode = od2.productCode
    JOIN orders ord2 ON od2.orderNumber = ord2.orderNumber
    GROUP BY p2.productCode
    HAVING COUNT(DISTINCT ord2.customerNumber) < 20
)
""", conn)
print(df_under_20)

conn.close()