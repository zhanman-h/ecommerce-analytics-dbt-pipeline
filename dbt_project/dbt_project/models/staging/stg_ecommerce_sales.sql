{{ config(materialized='view') }}

SELECT *
FROM {{ ref('ecommerce_sales_data')}}