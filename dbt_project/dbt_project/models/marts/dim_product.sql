{{ config(materialized='table') }}

SELECT DISTINCT
    product_id, 
    product_category
FROM {{ ref('int_ecommerce_sales') }}