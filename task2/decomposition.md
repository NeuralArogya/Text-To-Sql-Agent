# Task 2 – Query Decomposition

---

## Simple SELECT Queries (Q1–Q20)

**Q1: List all products**
- Intent: Retrieve all product records
- Tables: products
- Columns: productCode, productName, productLine, buyPrice, MSRP, quantityInStock
- Filters: None
- Joins: None

---

**Q2: Get all customers**
- Intent: Retrieve all customer records
- Tables: customers
- Columns: customerNumber, customerName, city, country, phone, creditLimit
- Filters: None
- Joins: None

---

**Q3: Show all orders**
- Intent: Retrieve all order records
- Tables: orders
- Columns: orderNumber, orderDate, requiredDate, shippedDate, status, customerNumber
- Filters: None
- Joins: None

---

**Q4: List all employees**
- Intent: Retrieve all employee records
- Tables: employees
- Columns: employeeNumber, firstName, lastName, jobTitle, email, officeCode
- Filters: None
- Joins: None

---

**Q5: Get all offices**
- Intent: Retrieve all office locations
- Tables: offices
- Columns: officeCode, city, country, addressLine1, phone
- Filters: None
- Joins: None

---

**Q6: Show all product lines**
- Intent: Retrieve all product line categories
- Tables: productlines
- Columns: productLine, textDescription
- Filters: None
- Joins: None

---

**Q7: List all payments**
- Intent: Retrieve all payment records
- Tables: payments
- Columns: customerNumber, checkNumber, paymentDate, amount
- Filters: None
- Joins: None

---

**Q8: Get product names and prices**
- Intent: Retrieve product names with pricing details
- Tables: products
- Columns: productName, buyPrice, MSRP
- Filters: None
- Joins: None

---

**Q9: Get customer names and cities**
- Intent: Retrieve customer names with their city and country
- Tables: customers
- Columns: customerName, city, country
- Filters: None
- Joins: None

---

**Q10: List employee first and last names**
- Intent: Retrieve employee names and job titles
- Tables: employees
- Columns: firstName, lastName, jobTitle
- Filters: None
- Joins: None

---

**Q11: Get all order dates**
- Intent: Retrieve all unique order dates with count per date
- Tables: orders
- Columns: orderDate
- Filters: None
- Joins: None

---

**Q12: Show product vendor list**
- Intent: Retrieve distinct product vendors with product count
- Tables: products
- Columns: productVendor
- Filters: None
- Joins: None

---

**Q13: Get all product codes**
- Intent: Retrieve all product codes with names and lines
- Tables: products
- Columns: productCode, productName, productLine
- Filters: None
- Joins: None

---

**Q14: List all countries from offices**
- Intent: Retrieve distinct countries where offices are located
- Tables: offices
- Columns: country, city, officeCode
- Filters: None
- Joins: None

---

**Q15: Show all order statuses**
- Intent: Retrieve distinct order statuses with count
- Tables: orders
- Columns: status
- Filters: None
- Joins: None

---

**Q16: Get all payment amounts**
- Intent: Retrieve all payment records ordered by amount
- Tables: payments
- Columns: customerNumber, checkNumber, paymentDate, amount
- Filters: None
- Joins: None

---

**Q17: List all job titles**
- Intent: Retrieve distinct job titles with employee count
- Tables: employees
- Columns: jobTitle
- Filters: None
- Joins: None

---

**Q18: Get customer phone numbers**
- Intent: Retrieve customer names with phone numbers
- Tables: customers
- Columns: customerName, phone, country
- Filters: None
- Joins: None

---

**Q19: Show product MSRP values**
- Intent: Retrieve product MSRP with markup percentage
- Tables: products
- Columns: productName, productLine, buyPrice, MSRP
- Filters: None
- Joins: None

---

**Q20: List order numbers**
- Intent: Retrieve all order numbers with basic details
- Tables: orders
- Columns: orderNumber, orderDate, status, customerNumber
- Filters: None
- Joins: None

---

## JOIN Queries (Q21–Q30)

**Q21: Get orders with customer names**
- Intent: Retrieve orders alongside the customer name who placed them
- Tables: orders, customers
- Columns: orderNumber, orderDate, status, customerName, country
- Filters: None
- Joins: orders.customerNumber = customers.customerNumber

---

**Q22: Get employees with office city**
- Intent: Retrieve employees with their office location
- Tables: employees, offices
- Columns: employeeNumber, firstName, lastName, jobTitle, city, country
- Filters: None
- Joins: employees.officeCode = offices.officeCode

---

**Q23: Get payments with customer names**
- Intent: Retrieve payment records with customer name
- Tables: payments, customers
- Columns: customerName, country, checkNumber, paymentDate, amount
- Filters: None
- Joins: payments.customerNumber = customers.customerNumber

---

**Q24: Get order details with product names**
- Intent: Retrieve order line items with readable product names
- Tables: orderdetails, products
- Columns: orderNumber, productName, quantityOrdered, priceEach
- Filters: None
- Joins: orderdetails.productCode = products.productCode

---

**Q25: Get products with product line description**
- Intent: Retrieve products with their full category description
- Tables: products, productlines
- Columns: productCode, productName, productLine, textDescription
- Filters: None
- Joins: products.productLine = productlines.productLine

---

**Q26: Get customers with sales rep names**
- Intent: Retrieve customers with their assigned sales representative
- Tables: customers, employees
- Columns: customerName, city, country, firstName, lastName, email
- Filters: None
- Joins: customers.salesRepEmployeeNumber = employees.employeeNumber

---

**Q27: Get orders with customer city**
- Intent: Retrieve orders with customer location details
- Tables: orders, customers
- Columns: orderNumber, orderDate, status, customerName, city, country
- Filters: None
- Joins: orders.customerNumber = customers.customerNumber

---

**Q28: Get employees and their manager**
- Intent: Retrieve each employee paired with their manager
- Tables: employees (self join)
- Columns: employeeNumber, firstName, lastName, jobTitle, reportsTo
- Filters: None
- Joins: employees.reportsTo = employees.employeeNumber (LEFT JOIN self)

---

**Q29: Get orderdetails with product vendor**
- Intent: Retrieve order line items with vendor information
- Tables: orderdetails, products
- Columns: orderNumber, productName, productVendor, quantityOrdered, priceEach
- Filters: None
- Joins: orderdetails.productCode = products.productCode

---

**Q30: Get payments with customer country**
- Intent: Retrieve payments with customer country information
- Tables: payments, customers
- Columns: country, customerName, paymentDate, amount
- Filters: None
- Joins: payments.customerNumber = customers.customerNumber

---

## Aggregate & GROUP BY Queries (Q31–Q40)

**Q31: Count customers per country**
- Intent: Count how many customers exist in each country
- Tables: customers
- Columns: country, COUNT(customerNumber)
- Filters: None
- Joins: None

---

**Q32: Total payments per customer**
- Intent: Calculate total amount paid by each customer
- Tables: customers, payments
- Columns: customerName, country, COUNT(checkNumber), SUM(amount), AVG(amount)
- Filters: None
- Joins: customers.customerNumber = payments.customerNumber

---

**Q33: Number of orders per status**
- Intent: Count how many orders exist for each status
- Tables: orders
- Columns: status, COUNT(orderNumber)
- Filters: None
- Joins: None

---

**Q34: Products per product line**
- Intent: Count products in each product line with average pricing
- Tables: products
- Columns: productLine, COUNT(*), AVG(MSRP), AVG(buyPrice)
- Filters: None
- Joins: None

---

**Q35: Employees per office**
- Intent: Count how many employees work in each office
- Tables: offices, employees
- Columns: city, country, COUNT(employeeNumber)
- Filters: None
- Joins: offices.officeCode = employees.officeCode (LEFT JOIN)

---

**Q36: Total stock per product vendor**
- Intent: Calculate total inventory units per vendor
- Tables: products
- Columns: productVendor, COUNT(*), SUM(quantityInStock), AVG(quantityInStock)
- Filters: None
- Joins: None

---

**Q37: Average buy price per product line**
- Intent: Calculate min, average and max buy price per product line
- Tables: products
- Columns: productLine, MIN(buyPrice), AVG(buyPrice), MAX(buyPrice)
- Filters: None
- Joins: None

---

**Q38: Orders per customer**
- Intent: Count total orders placed by each customer
- Tables: customers, orders
- Columns: customerName, country, COUNT(orderNumber), MIN(orderDate), MAX(orderDate)
- Filters: None
- Joins: customers.customerNumber = orders.customerNumber (LEFT JOIN)

---

**Q39: Max MSRP per product line**
- Intent: Find maximum and minimum MSRP per product line
- Tables: products
- Columns: productLine, MAX(MSRP), MIN(MSRP)
- Filters: None
- Joins: None

---

**Q40: Min buy price per vendor**
- Intent: Find minimum and maximum buy price per vendor
- Tables: products
- Columns: productVendor, MIN(buyPrice), MAX(buyPrice), COUNT(*)
- Filters: None
- Joins: None

---

## Scalar Aggregate Queries (Q41–Q50)

**Q41: Total number of customers**
- Intent: Count all customers in the database
- Tables: customers
- Columns: COUNT(*)
- Filters: None
- Joins: None

---

**Q42: Total number of products**
- Intent: Count total products, distinct product lines and vendors
- Tables: products
- Columns: COUNT(*), COUNT(DISTINCT productLine), COUNT(DISTINCT productVendor)
- Filters: None
- Joins: None

---

**Q43: Total revenue from payments**
- Intent: Calculate total revenue and payment statistics
- Tables: payments
- Columns: COUNT(*), SUM(amount), AVG(amount), MIN(amount), MAX(amount)
- Filters: None
- Joins: None

---

**Q44: Average product price**
- Intent: Calculate average buy price, MSRP and margin
- Tables: products
- Columns: AVG(buyPrice), AVG(MSRP), AVG(MSRP - buyPrice)
- Filters: None
- Joins: None

---

**Q45: Max payment amount**
- Intent: Find the single largest payment with customer details
- Tables: payments, customers
- Columns: amount, customerName, country, paymentDate
- Filters: amount = MAX(amount)
- Joins: payments.customerNumber = customers.customerNumber

---

**Q46: Min payment amount**
- Intent: Find the single smallest payment with customer details
- Tables: payments, customers
- Columns: amount, customerName, country, paymentDate
- Filters: amount = MIN(amount)
- Joins: payments.customerNumber = customers.customerNumber

---

**Q47: Count total orders**
- Intent: Count total orders, distinct customers and statuses
- Tables: orders
- Columns: COUNT(*), COUNT(DISTINCT customerNumber), COUNT(DISTINCT status)
- Filters: None
- Joins: None

---

**Q48: Total quantity in stock**
- Intent: Calculate total and average inventory across all products
- Tables: products
- Columns: SUM(quantityInStock), COUNT(*), AVG(quantityInStock), MIN(quantityInStock), MAX(quantityInStock)
- Filters: None
- Joins: None

---

**Q49: Average MSRP**
- Intent: Calculate average, stddev, min and max MSRP
- Tables: products
- Columns: AVG(MSRP), STDDEV(MSRP), MIN(MSRP), MAX(MSRP)
- Filters: None
- Joins: None

---

**Q50: Number of employees**
- Intent: Count total employees, distinct titles and offices
- Tables: employees
- Columns: COUNT(*), COUNT(DISTINCT jobTitle), COUNT(DISTINCT officeCode)
- Filters: None
- Joins: None
