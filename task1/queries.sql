-- Q1: List all products
SELECT productCode, productName, productLine,
       buyPrice, MSRP, quantityInStock
FROM products
ORDER BY productName;

-- Q2: Get all customers
SELECT customerNumber, customerName, city,
       country, phone, creditLimit
FROM customers
ORDER BY customerName;

-- Q3: Show all orders
SELECT orderNumber, orderDate, requiredDate,
       shippedDate, status, customerNumber
FROM orders
ORDER BY orderDate DESC;

-- Q4: List all employees
SELECT employeeNumber, firstName, lastName,
       jobTitle, email, officeCode
FROM employees
ORDER BY lastName, firstName;

-- Q5: Get all offices
SELECT officeCode, city, country,
       addressLine1, phone
FROM offices
ORDER BY country, city;

-- Q6: Show all product lines
SELECT productLine, textDescription
FROM productlines
ORDER BY productLine;

-- Q7: List all payments
SELECT customerNumber, checkNumber,
       paymentDate, amount
FROM payments
ORDER BY paymentDate DESC;

-- Q8: Get product names and prices
SELECT productName, buyPrice, MSRP,
       ROUND(MSRP - buyPrice, 2) AS profit_margin
FROM products
ORDER BY MSRP DESC;

-- Q9: Get customer names and cities
SELECT customerName, city, country
FROM customers
ORDER BY country, city, customerName;

-- Q10: List employee first and last names
SELECT firstName, lastName,
       CONCAT(firstName, ' ', lastName) AS fullName,
       jobTitle
FROM employees
ORDER BY lastName;

-- Q11: Get all order dates
SELECT DISTINCT orderDate,
       COUNT(*) AS ordersOnDate
FROM orders
GROUP BY orderDate
ORDER BY orderDate DESC;

-- Q12: Show product vendor list
SELECT DISTINCT productVendor,
       COUNT(*) AS productCount
FROM products
GROUP BY productVendor
ORDER BY productCount DESC;

-- Q13: Get all product codes
SELECT productCode, productName, productLine
FROM products
ORDER BY productCode;

-- Q14: List all countries from offices
SELECT DISTINCT country, city, officeCode
FROM offices
ORDER BY country;

-- Q15: Show all order statuses
SELECT DISTINCT status,
       COUNT(*) AS orderCount
FROM orders
GROUP BY status
ORDER BY orderCount DESC;

-- Q16: Get all payment amounts
SELECT customerNumber, checkNumber,
       paymentDate, amount
FROM payments
ORDER BY amount DESC;

-- Q17: List all job titles
SELECT DISTINCT jobTitle,
       COUNT(*) AS employeeCount
FROM employees
GROUP BY jobTitle
ORDER BY employeeCount DESC;

-- Q18: Get customer phone numbers
SELECT customerName, phone, country
FROM customers
ORDER BY country, customerName;

-- Q19: Show product MSRP values
SELECT productName, productLine,
       buyPrice, MSRP,
       ROUND(((MSRP - buyPrice) / buyPrice) * 100, 1) AS markupPct
FROM products
ORDER BY MSRP DESC;

-- Q20: List order numbers
SELECT orderNumber, orderDate, status, customerNumber
FROM orders
ORDER BY orderNumber;

-- Q21: Get orders with customer names
SELECT o.orderNumber, o.orderDate, o.status,
       c.customerName, c.country
FROM orders o
JOIN customers c ON o.customerNumber = c.customerNumber
ORDER BY o.orderDate DESC;

-- Q22: Get employees with office city
SELECT e.employeeNumber,
       CONCAT(e.firstName, ' ', e.lastName) AS employeeName,
       e.jobTitle,
       o.city AS officeCity,
       o.country AS officeCountry
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
ORDER BY o.country, e.lastName;

-- Q23: Get payments with customer names
SELECT c.customerName, c.country,
       p.checkNumber, p.paymentDate, p.amount
FROM payments p
JOIN customers c ON p.customerNumber = c.customerNumber
ORDER BY p.amount DESC;

-- Q24: Get order details with product names
SELECT od.orderNumber, p.productName,
       od.quantityOrdered, od.priceEach,
       ROUND(od.quantityOrdered * od.priceEach, 2) AS lineTotal
FROM orderdetails od
JOIN products p ON od.productCode = p.productCode
ORDER BY od.orderNumber, lineTotal DESC;

-- Q25: Get products with product line description
SELECT p.productCode, p.productName,
       p.productLine, pl.textDescription
FROM products p
JOIN productlines pl ON p.productLine = pl.productLine
ORDER BY p.productLine, p.productName;

-- Q26: Get customers with sales rep names
SELECT c.customerName, c.city, c.country,
       CONCAT(e.firstName, ' ', e.lastName) AS salesRepName,
       e.email AS salesRepEmail
FROM customers c
JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
ORDER BY e.lastName, c.customerName;

-- Q27: Get orders with customer city
SELECT o.orderNumber, o.orderDate, o.status,
       c.customerName, c.city, c.country
FROM orders o
JOIN customers c ON o.customerNumber = c.customerNumber
ORDER BY c.country, c.city;

-- Q28: Get employees and their manager
SELECT e.employeeNumber,
       CONCAT(e.firstName, ' ', e.lastName) AS employee,
       e.jobTitle,
       CONCAT(m.firstName, ' ', m.lastName) AS manager,
       m.jobTitle AS managerTitle
FROM employees e
LEFT JOIN employees m ON e.reportsTo = m.employeeNumber
ORDER BY m.lastName, e.lastName;

-- Q29: Get orderdetails with product vendor
SELECT od.orderNumber, p.productName,
       p.productVendor, od.quantityOrdered,
       od.priceEach
FROM orderdetails od
JOIN products p ON od.productCode = p.productCode
ORDER BY p.productVendor, od.orderNumber;

-- Q30: Get payments with customer country
SELECT c.country, c.customerName,
       p.paymentDate, p.amount
FROM payments p
JOIN customers c ON p.customerNumber = c.customerNumber
ORDER BY c.country, p.amount DESC;

-- Q31: Count customers per country
SELECT country,
       COUNT(*) AS customerCount
FROM customers
GROUP BY country
ORDER BY customerCount DESC;

-- Q32: Total payments per customer
SELECT c.customerName, c.country,
       COUNT(p.checkNumber)    AS paymentCount,
       SUM(p.amount)           AS totalPaid,
       ROUND(AVG(p.amount), 2) AS avgPayment
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber, c.customerName, c.country
ORDER BY totalPaid DESC;

-- Q33: Number of orders per status
SELECT status,
       COUNT(*) AS orderCount
FROM orders
GROUP BY status
ORDER BY orderCount DESC;

-- Q34: Products per product line
SELECT productLine,
       COUNT(*)                 AS productCount,
       ROUND(AVG(MSRP), 2)     AS avgMSRP,
       ROUND(AVG(buyPrice), 2) AS avgBuyPrice
FROM products
GROUP BY productLine
ORDER BY productCount DESC;

-- Q35: Employees per office
SELECT o.city, o.country,
       COUNT(e.employeeNumber) AS employeeCount
FROM offices o
LEFT JOIN employees e ON o.officeCode = e.officeCode
GROUP BY o.officeCode, o.city, o.country
ORDER BY employeeCount DESC;

-- Q36: Total stock per product vendor
SELECT productVendor,
       COUNT(*)                        AS productVarieties,
       SUM(quantityInStock)            AS totalStock,
       ROUND(AVG(quantityInStock), 0)  AS avgStockPerProduct
FROM products
GROUP BY productVendor
ORDER BY totalStock DESC;

-- Q37: Average buy price per product line
SELECT productLine,
       ROUND(MIN(buyPrice), 2) AS minBuyPrice,
       ROUND(AVG(buyPrice), 2) AS avgBuyPrice,
       ROUND(MAX(buyPrice), 2) AS maxBuyPrice
FROM products
GROUP BY productLine
ORDER BY avgBuyPrice DESC;

-- Q38: Orders per customer
SELECT c.customerName, c.country,
       COUNT(o.orderNumber) AS totalOrders,
       MIN(o.orderDate)     AS firstOrder,
       MAX(o.orderDate)     AS lastOrder
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY c.customerNumber, c.customerName, c.country
ORDER BY totalOrders DESC;

-- Q39: Max MSRP per product line
SELECT productLine,
       MAX(MSRP)                       AS maxMSRP,
       MIN(MSRP)                       AS minMSRP,
       ROUND(MAX(MSRP) - MIN(MSRP), 2) AS msrpRange
FROM products
GROUP BY productLine
ORDER BY maxMSRP DESC;

-- Q40: Min buy price per vendor
SELECT productVendor,
       MIN(buyPrice) AS minBuyPrice,
       MAX(buyPrice) AS maxBuyPrice,
       COUNT(*)      AS productCount
FROM products
GROUP BY productVendor
ORDER BY minBuyPrice ASC;

-- Q41: Total number of customers
SELECT COUNT(*) AS totalCustomers
FROM customers;

-- Q42: Total number of products
SELECT COUNT(*)                    AS totalProducts,
       COUNT(DISTINCT productLine) AS distinctProductLines,
       COUNT(DISTINCT productVendor) AS distinctVendors
FROM products;

-- Q43: Total revenue from payments
SELECT COUNT(*)              AS totalPayments,
       SUM(amount)           AS totalRevenue,
       ROUND(AVG(amount), 2) AS avgPayment,
       MIN(amount)           AS minPayment,
       MAX(amount)           AS maxPayment
FROM payments;

-- Q44: Average product price
SELECT ROUND(AVG(buyPrice), 2)       AS avgBuyPrice,
       ROUND(AVG(MSRP), 2)           AS avgMSRP,
       ROUND(AVG(MSRP - buyPrice), 2) AS avgMargin
FROM products;

-- Q45: Max payment amount
SELECT p.amount AS maxPayment,
       c.customerName,
       c.country,
       p.paymentDate
FROM payments p
JOIN customers c ON p.customerNumber = c.customerNumber
WHERE p.amount = (SELECT MAX(amount) FROM payments);

-- Q46: Min payment amount
SELECT p.amount AS minPayment,
       c.customerName,
       c.country,
       p.paymentDate
FROM payments p
JOIN customers c ON p.customerNumber = c.customerNumber
WHERE p.amount = (SELECT MIN(amount) FROM payments);

-- Q47: Count total orders
SELECT COUNT(*)                     AS totalOrders,
       COUNT(DISTINCT customerNumber) AS customersWhoOrdered,
       COUNT(DISTINCT status)        AS distinctStatuses
FROM orders;

-- Q48: Total quantity in stock
SELECT SUM(quantityInStock)           AS totalUnitsInStock,
       COUNT(*)                       AS totalProducts,
       ROUND(AVG(quantityInStock), 0) AS avgStockPerProduct,
       MIN(quantityInStock)           AS minStock,
       MAX(quantityInStock)           AS maxStock
FROM products;

-- Q49: Average MSRP
SELECT ROUND(AVG(MSRP), 2)    AS overallAvgMSRP,
       ROUND(STDDEV(MSRP), 2) AS stdDevMSRP,
       MIN(MSRP)              AS lowestMSRP,
       MAX(MSRP)              AS highestMSRP
FROM products;

-- Q50: Number of employees
SELECT COUNT(*)                  AS totalEmployees,
       COUNT(DISTINCT jobTitle)  AS distinctTitles,
       COUNT(DISTINCT officeCode) AS officesRepresented
FROM employees;