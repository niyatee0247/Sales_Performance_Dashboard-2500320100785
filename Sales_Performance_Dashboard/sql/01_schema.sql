-- Run in Oracle SQL Developer
CREATE TABLE sales_stg (
  order_id VARCHAR2(20), order_date DATE, customer_id VARCHAR2(20), product_id VARCHAR2(20), product_name VARCHAR2(100), category VARCHAR2(40), region VARCHAR2(30), quantity NUMBER, unit_price NUMBER(10,2), discount_pct NUMBER(5,2), gross_sales NUMBER(12,2), net_sales NUMBER(12,2), month_key VARCHAR2(7)
);
-- Import output/cleaned_data.csv into this table using SQL Developer:
-- Right-click table > Import Data > select CSV > map columns.
-- Ensure DATE columns are parsed as YYYY-MM-DD (or use staging VARCHAR2 then TO_DATE).
