# Sales Performance Dashboard

**Domain:** Retail and e-commerce

## Problem statement
Analyze retail transactions to identify revenue trends, profitable products, and regional performance.

## Objectives
- Clean and validate the supplied transaction/record data.
- Use Python (Pandas) for preparation and exploratory analysis.
- Use Oracle SQL for aggregations, rankings and reusable views.
- Build an interactive Power BI dashboard for decision support.

## KPIs
- Total Sales
- Total Orders
- Units Sold
- Average Order Value
- Monthly Sales Growth

## Dataset
`data/sales_transactions.csv` — 1,201 rows including a few intentional quality issues (e.g. duplicate or missing/invalid values) for cleaning practice.


## Tools
- Python 3.10+ (pandas, numpy, matplotlib, seaborn)
- Oracle Database / Oracle SQL Developer
- Power BI Desktop

## Run
1. Create a Python environment and install `requirements.txt`.
2. Run `python analysis.py`. It reads the raw CSV in `data/`, cleans it, prints QA checks and writes outputs to `output/`.
3. In Oracle SQL Developer, run `sql/01_schema.sql`, then import the cleaned CSV using **Table > Import Data** (map columns to the staging table), and run `sql/02_analysis.sql`.
4. In Power BI Desktop, Get Data > Text/CSV and import the cleaned CSV (or Oracle view). Follow `powerbi/dashboard_guide.md`; create the DAX measures and visuals listed there.
5. Compare totals in the Python output, Oracle query results and Power BI cards.

## Dataset note
The included data is synthetic, generated for learning and reproducible demonstrations. It is not real customer/student/restaurant/social-media data and must not be presented as a real-world source. Replace it with an approved public dataset if your instructor requires external-source evidence.

## Submission checklist
- [ ] Problem statement and KPI definitions
- [ ] ER/star-schema diagram
- [ ] Python notebook/script and data-quality report
- [ ] Oracle DDL, import instructions, queries and views
- [ ] Power BI `.pbix` built in Power BI Desktop
- [ ] Insights summary, README and GitHub repository
- [ ] 2–3 minute demo recording

