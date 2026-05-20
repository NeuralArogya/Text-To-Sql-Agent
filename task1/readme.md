# Task 1 – SQL Benchmark Dataset

Writing ground truth SQL queries for 50 natural language questions using the ClassicModels PostgreSQL database.


## What's in here

- `queries.sql` — all 50 SQL queries organized by category
- `README.md` — this file


## Query Categories

| Simple SELECT | Q1–Q20 | Single table queries |
| JOIN Queries | Q21–Q30 | Multi-table joins |
| Aggregate & GROUP BY | Q31–Q40 | Grouping and aggregation |
| Scalar Aggregates | Q41–Q50 | Summary statistics |

## Database
ClassicModels PostgreSQL — 8 tables: `products`, `customers`, `orders`,
`orderdetails`, `employees`, `offices`, `payments`, `productlines`

## How to run
1. Load `seed.sql` into PostgreSQL
2. Open pgAdmin and connect to the classicmodels database
3. Copy any query from `queries.sql` into the pgAdmin Query Tool
4. Hit F5 to run
