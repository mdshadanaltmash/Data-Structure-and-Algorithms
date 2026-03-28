--customers
--    customer_id
--    customer_name
--    region
--
--Orders
--    order_id
--    customer_id
--    order_date
--    amount
--
--Question:
--Write a query to find the total order amount for each customer for each month (YYYY-MM).

select
    c.customer_id,
    c.cusotmer_name,
    trunc(order_date, 'month') as order_date,
    sum(amount) as total_order_amt
from orders o
join customers c
 on o.customer_id = c.customer_id
 group by c.customer_id, c.cusotmer_name, trunc(order_date, 'month');




You have the following tables:
Products
    product_id
    product_name

Orders
    order_id
    product_id
    customer_id
    order_date
    amount

Question:
Find the top 2 products (by total sales amount) for each month.

Output should include:
    month (YYYY-MM)
    product_id
    product_name
    total_sales_amount
    rank (1 or 2)

If two products have the same sales amount, give them the same rank.

with total_data as (
select
    to_char(trunc(order_date, 'month'), 'YYYY-MM') as order_month,
    o.product_id,
    p.product_name,
    sum(o.amount) as total_sales_amount
from orders o
join products p
    on o.product_id = p.product_id
group by to_char(trunc(order_date, 'month'), 'YYYY-MM'), o.product_id, p.product_name
)
select * from (
select
 order_month, product_id, product_name, total_sales_amount,
 dense_rank() over(partition by order_month order by total_sales_amount desc) as rank
 from total_data
 ) where rank <= 2;




You have the following tables:

Customers
customer_id
customer_name
region

Orders
order_id
customer_id
order_date
amount

Goal: Find the top 3 customers by total order amount within each region.

Output:
region
customer_id
customer_name
total_order_amount
rank (1 to 3)

Tie handling: If two customers have the same total amount, they should have the same rank (use DENSE_RANK).

with sales_data as (
select
c.region, c.customer_id, c.customer_name, sum(amount) as total_order_amount
from orders o
join customers c on o.customer_id = c.customer_id
group by c.region, c.customer_id, c.customer_name
)
select * from (
select region, customer_id, customer_name, total_order_amount,
dense_rank() over(partition by region order by total_order_amount desc) as rank
from sales_data
)
where rank <= 3;



🟥 Hard SQL Question
You have the following tables:

Orders
order_id
customer_id
order_date
amount

Customers
customer_id
customer_name
signup_date

Goal: Find customers whose monthly spending has increased for 3 consecutive months.

Specifically: Compute total spending per customer per month (YYYY-MM)

Identify customers where:
(month2 > month1) AND (month3 > month2)

A customer may have many months — you must detect any 3-month increasing streak.

Output:
customer_id
customer_name
month1
amount1
month2
amount2
month3
amount3

Where those 3 months form an increasing pattern.
-- APPROACH 1
with monthly_spend_data as (
select
trunc(order_date, 'month') as order_month,
c.customer_id, c.customer_name, sum(o.amount) as monthly_spent
from orders o
join customers c on o.customer_id = c.customer_id
group by trunc(order_date, 'month'), c.customer_id, c.customer_name
)

select
    customer_id, customer_name,
    m1.order_month as month1, m1.monthly_spent as amount1,
    m2.order_month as month2, m2.monthly_spent as amount2,
    m3.order_month as month3, m3.monthly_spent as amount3
from monthly_spend_data m1
join monthly_spend_data m2 on m1.customer_id = m2.customer_id and ADD_MONTHS(m1.order_month, 1) = m2.order_month
join monthly_spend_data m3 on m1.customer_id = m3.customer_id and ADD_MONTHS(m1.order_month, 2) = m3.order_month
where m2.monthly_spent> m1.monthly_spent and m3.monthly_spent > m2.monthly_spent;



-- APPROACH 2 --USING LAG

with monthly_spend_data as (
select
trunc(order_date, 'month') as order_month,
c.customer_id, c.customer_name, sum(o.amount) as monthly_spent
from orders o
join customers c on o.customer_id = c.customer_id
group by trunc(order_date, 'month'), c.customer_id, c.customer_name
)
select
 customer_id,
    customer_name,
    month1,
    amount1,
    prev_month   AS month2,
    prev_month_spent AS amount2,
    prev_two_month AS month3,
    prev_two_month_spent AS amount3
    from (
select
customer_id,
customer_name,
order_month as month1,
monthly_spent as amount1,
lag(order_month, 1) over(partition by customer_id order by order_month) as prev_month,
lag(monthly_spent, 1) over(partition by customer_id order by order_month) as prev_month_spent,
lag(order_month, 2) over(partition by customer_id order by order_month) as prev_two_month,
lag(monthly_spent, 2) over(partition by customer_id order by order_month) as prev_two_month_spent
from monthly_spend_data
)
where amount1 > prev_month_spent and prev_month_spent > prev_two_month_spent;




| cust_id | month | amount |
| ------- | ----- | ------ |
| 1       | Jan   | 10     |
| 1       | Feb   | 20     |
| 1       | Mar   | 15     |
| 1       | Apr   | 30     |



Write a query to find months where the customer SPENT LESS than the previous month.

So expected result should show:
month
amount
prev_amount


select * from (
select
    month,
    amount,
    lag(amount, 1) over(partition by cust_id order by month) as prev_amount
from table)
where amount < prev_amount;


This is one of the most common real interview questions.
Here is a table:

| cust_id | month | status   |
| ------- | ----- | -------- |
| 1       | Jan   | Active   |
| 1       | Feb   | Active   |
| 1       | Mar   | Inactive |
| 1       | Apr   | Inactive |
| 1       | May   | Active   |


We want to find period boundaries, meaning:
👉 Months where a customer's status changed from one month to the next.

For example:
Feb → Mar (Active → Inactive)
Apr → May (Inactive → Active)

So the expected output is:
| cust_id | month | status   | next_status |
| ------- | ----- | -------- | ----------- |
| 1       | Feb   | Active   | Inactive    |
| 1       | Apr   | Inactive | Active      |

select * from (
select
cust_id, month, status,
lead(status, 1) over(partition by cust_id order by month) as next_status
from table )
where status <> next_status;











--ISLANDS AND GAPS


WITH lagged AS (
    SELECT
        user_id,
        ts,
        LAG(ts) OVER (PARTITION BY user_id ORDER BY ts) AS prev_ts
    FROM events
),
marked AS (
    SELECT
        user_id,
        ts,
        CASE
            WHEN prev_ts IS NULL
                 OR ts - prev_ts > INTERVAL '20' MINUTE
            THEN 1 ELSE 0 END AS is_new_island
    FROM lagged
),
islands AS (
    SELECT
        user_id,
        ts,
        SUM(is_new_island) OVER (PARTITION BY user_id ORDER BY ts) AS island_id
    FROM marked
)
SELECT
    user_id,
    island_id,
    MIN(ts) AS island_start,
    MAX(ts) AS island_end
FROM islands
GROUP BY user_id, island_id
ORDER BY user_id, island_id;
