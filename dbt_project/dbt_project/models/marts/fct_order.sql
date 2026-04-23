{{ config(materialized='table') }}

SELECT 
    order_id, 
    customer_id, 
    product_id,
    product_category, 
    order_date, 
    quantity, 
    price, 
    quantity * price AS total_amount,
    order_status
FROM {{ ref('int_ecommerce_sales') }}