/* 시도한 쿼리(1) */
SELECT name FROM Customers
INNER JOIN Orders
ON Customers.id = customerId
WHERE Orders.id IS NULL

/* 시도한 쿼리(2) */
SELECT name FROM Customers
INNER JOIN Orders
ON Customers.id = customerId
WHERE Orders.id IS NULL

/* 문제 풀이(1) */
SELECT name as Customers FROM Customers
LEFT JOIN Orders
ON Customers.id = Orders.customerId
WHERE Orders.id IS NULL
