Customer
customer_id, customer_name, region

product
product_id, product_name

orders
order_id, customer_id, product_id, order_date, order_amt

--top 3 products per region by order count
--find customers who have ordered more than 3 times in a month



with order_details as(
select
--order_id,
c.region, p.product_name, count(*) as order_count
orders o join product p on o.product_id = p.product_id
join customer c on o.customer_id = c.customer_id
group by c.region, p.product_name
)
select region, product_name from (
select region, product_name, row_number() over(partition by region order by order_count desc) as rn
from order_details
)
where rn <=3;




select customer_name, order_month, order_year, count(*) as total_order
from (
select
order_id, c.customer_name, extract (month from o.order_date) as order_month, extract (year from o.order_date) as order_year,
from orders o join customer c on o.customer_id = c.customer_id
)
group by customer_name, order_month, order_year
having count(*) > 3;



--SELF PRACTICE

select
 c.customer_id,
 c.customer_name,
 date_trunc('month', order_date) as order_month,
 count(*) as order_count
from orders o
join customer c
on o.customer_id = c.customer_id
group by c.customer_id, c.customer_name, order_month
having count(*) > 3;