-- Analysis queries for Sales Performance Dashboard
SELECT product_name, SUM(net_sales) total_sales FROM sales_stg GROUP BY product_name ORDER BY total_sales DESC FETCH FIRST 10 ROWS ONLY;
SELECT TO_CHAR(order_date,'YYYY-MM') month_key, SUM(net_sales) monthly_sales FROM sales_stg GROUP BY TO_CHAR(order_date,'YYYY-MM') ORDER BY month_key;
SELECT region, SUM(net_sales) total_sales, COUNT(DISTINCT order_id) orders FROM sales_stg GROUP BY region ORDER BY total_sales DESC;

-- Reconciliation
SELECT COUNT(*) row_count FROM sales_stg;
