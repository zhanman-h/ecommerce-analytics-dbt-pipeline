SELECT * 
FROM 'dev_schema'.'fct_order'
WHERE order_status = 'Cancelled' 
ORDER BY total_amount DESC;