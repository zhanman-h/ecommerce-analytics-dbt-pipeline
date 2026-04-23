SELECT 
    order_status, 
    SUM(total_amount) AS grant_total 
FROM 'dev_schema'.'fct_order'
GROUP BY 1 
ORDER BY 2 DESC;