SELECT 
    product_category,
    SUM(total_amount) AS grant_total 
FROM 'dev_schema'.'fct_order'
GROUP BY product_category 
ORDER BY 2 DESC;  