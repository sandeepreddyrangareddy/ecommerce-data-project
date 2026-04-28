# E-Commerce Data Analysis & Pipeline Project

## Overview
This project started as a way to practice building a real data pipeline from scratch — not just querying a clean table someone handed me, but actually taking raw, messy source files and shaping them into something useful.  

The dataset is from Olist, a Brazilian e-commerce platform available on Kaggle. It covers real orders, customers, products, and sellers across multiple CSV files — which made it a good exercise in joining and modeling data the way you'd encounter it in a real analytics role.

---

## What I Built
The core of the project is a simple star schema:

- **fact_orders** — one row per order item, with revenue and freight values  
- **dim_customers** — unique customers with city and state  
- **dim_products** — products with category names  

I wrote the entire pipeline in Python using Pandas, broken into separate scripts for loading, transforming, and analyzing the data. Keeping them separate made it easier to debug when something broke mid-join (which happened more than once).

---

## What I Found
A few things stood out once the data was clean:

- The repeat purchase rate was around 3%, which is surprisingly low. It suggests Olist customers tend to be one-time buyers rather than loyal shoppers — something a retention strategy would need to address.  
- Revenue wasn't spread evenly across categories. A handful of product types drove the majority of sales, which shows up clearly in the top categories output.  
- There were some messy product category names — nulls and inconsistencies — that had to be handled before any category-level analysis made sense.

---

## Tools Used
- Python (Pandas)  
- Jupyter Notebook for exploratory work  
- CSV outputs for downstream use in Power BI (in progress)  

---

## What's Next
I want to connect the output to a Power BI dashboard to make the revenue trends and category breakdowns visual.  

Eventually I'd like to schedule the pipeline with Apache Airflow to simulate how this would run in a production environment.

---

## How to Run
```bash
python src/transform_data.py   # builds the fact and dimension tables
python src/analysis.py         # generates monthly revenue and category outputs
```

---

## Lessons Learned
The main thing I'd do differently next time is add data quality checks earlier in the pipeline — I spent more time than expected tracking down where nulls were coming from before realizing they were in the source files themselves.
