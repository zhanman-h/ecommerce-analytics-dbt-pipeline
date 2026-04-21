{{ config(materialized='table') }}

WITH cleaned AS (
    SELECT
        order_id, 
        customer_id, 
        product_id, 
        CAST(order_date AS date) AS order_date,
        CASE 
            WHEN payment_method IN ('Credit and Debit Cards', 'Digital Wallets', 'Bank Transfers','BNPL Services', 'Cryptocurrency', 'Cash on Delivery') THEN payment_method
            ELSE 'Invalid'
        END AS payment_method,
        product_category,
        CASE    
            WHEN quantity > 0 THEN quantity
            ELSE 1
        END AS quantity, 
        CASE 
            WHEN price > 0 THEN price   
            ELSE 0
        END AS price, 
        order_status
    FROM {{ ref('stg_ecommerce_sales') }}
    WHERE customer_id IS NOT NULL
        AND CAST(order_date AS date) <= current_date
), 

deduplicated AS (
    SELECT *, 
        ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY order_date DESC) AS rn
    FROM cleaned
)

SELECT *
FROM deduplicated
WHERE rn = 1