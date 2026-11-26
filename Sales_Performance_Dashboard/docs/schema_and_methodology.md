# Schema and methodology

## Suggested star schema
FactSales(order_id, date_key, customer_id, product_id, quantity, gross_sales, net_sales) with Date, Product, Customer and Region dimensions.

## Data preparation
See `analysis.py`. Duplicate business keys are removed; invalid numeric ranges and missing essential fields are excluded. Derived measures are documented in the script.

## Key test cases
- Duplicate primary/business key.
- Missing essential value.
- Boundary or invalid numeric values.
- Aggregation by category/period and reconciliation across tools.

## Acceptance criteria
Top 10 products and monthly trend; total sales reconciles between CSV, Python and Oracle; at least 5 KPIs and 3 slicers.

## Important limitation
All supplied records are synthetic. They demonstrate the workflow and do not establish factual claims about a real organization.
