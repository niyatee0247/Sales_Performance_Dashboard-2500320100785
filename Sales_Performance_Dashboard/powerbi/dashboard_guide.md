# Power BI dashboard guide — Sales Performance Dashboard

## Import
Home → Get Data → Text/CSV → select `output/cleaned_data.csv`. Confirm date and numeric data types. Rename table to `SALES` or adjust DAX table names below.

## DAX measures
```DAX
Total Sales = SUM(Sales[net_sales])
Total Orders = DISTINCTCOUNT(Sales[order_id])
Units Sold = SUM(Sales[quantity])
Average Order Value = DIVIDE([Total Sales], [Total Orders])
Gross Sales = SUM(Sales[gross_sales])
```

## Recommended report layout
Cards: Total Sales, Total Orders, Units Sold, Average Order Value. Line chart: net_sales by month. Bar chart: Top 10 product by net_sales. Bar/Map: net_sales by region. Slicers: region, category, order_date.

## Interactions and validation
- Add at least 3 slicers and enable cross-filtering.
- Add drill-through to a detail page (product/student/restaurant/post).
- Compare card totals against `output/data_quality_report.csv` and Oracle query output.
- Use a clear title, refresh date, units and data-source note.
