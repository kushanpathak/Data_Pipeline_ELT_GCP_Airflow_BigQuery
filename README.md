# 🚀 Global Healthcare Data Pipeline (Airflow + GCP + BigQuery)

## 📌 Overview

This project implements an **end-to-end data pipeline** to process global healthcare data from a CSV file and transform it into analytics-ready datasets using **Google Cloud Platform** and **Apache Airflow**.

The pipeline automates:

* Data ingestion from GCS to BigQuery
* Transformation into country-specific tables
* Creation of reporting views for BI tools

---

## 🧠 Architecture

```
CSV → GCS → BigQuery (Staging) → Transform Tables → Reporting Views → Power BI / Looker
                  ↑
            Apache Airflow (DAG)
```

---

## ⚙️ Tech Stack

* Python
* Apache Airflow
* Google Cloud Storage (GCS)
* BigQuery
* SQL
* Power BI / Looker

---

<img width="944" height="481" alt="image" src="https://github.com/user-attachments/assets/164efa81-b12c-483a-982b-34b4745e342c" />

## 📂 Dataset Schema

The dataset includes the following healthcare and socioeconomic attributes:

* Country
* Year
* Disease Name
* Disease Category
* Prevalence Rate
* Incidence Rate
* Mortality Rate
* Age Group
* Gender
* Population Affected
* Healthcare Access
* Doctors per 1000
* Hospital Beds per 1000
* Treatment Type
* Average Treatment Cost USD
* Availability of Vaccines Treatment
* Recovery Rate
* DALYs
* Improvement in 5 Years
* Per Capita Income USD
* Education Index
* Urbanization Rate

---

## 🔄 Pipeline Workflow

### 🔹 1. File Validation

* Uses Airflow **GCSObjectExistenceSensor**
* Ensures CSV file is available before processing

---

### 🔹 2. Data Ingestion

* CSV file (`global_health_data.csv`) is loaded from GCS
* Data is ingested into BigQuery staging table:

```
staging_dataset.global_data
```

* Uses:

  * `GCSToBigQueryOperator`
  * Auto schema detection
  * Header skipping

---

### 🔹 3. Data Transformation

* Creates **country-specific tables** dynamically:

```
transform_dataset.{country}_table
```

* Example:

```
transform_dataset.india_table
transform_dataset.usa_table
```

* Logic:

```sql
SELECT *
FROM staging_dataset.global_data
WHERE country = 'India'
```

---

### 🔹 4. Reporting Layer (Views)

* Creates **optimized reporting views** for BI tools:

```
reporting_dataset.{country}_view
```

* Example:

```
reporting_dataset.india_view
```

* View logic:

```sql
SELECT 
    Year,
    Disease Name,
    Disease Category,
    Prevalence Rate,
    Incidence Rate
FROM transform_dataset.india_table
WHERE Availability of Vaccines Treatment = FALSE
```

---

## 📊 Key Features

* Automated pipeline using Airflow DAG
* Data validation using sensors
* Scalable ingestion with BigQuery
* Dynamic table creation for multiple countries
* Reporting layer abstraction using views
* BI-ready dataset for analytics

---

## ▶️ How to Run

1. Start Airflow:

```bash
airflow webserver
airflow scheduler
```

2. Upload CSV to GCS:

```
gs://bkt-src-global-data/global_health_data.csv
```

3. Trigger DAG:

```
load_and_transform_view
```

4. Verify:

* Data loaded in `staging_dataset.global_data`
* Country tables created in `transform_dataset`
* Views created in `reporting_dataset`

---
FINAL PIPELINE 


<img width="1278" height="735" alt="image" src="https://github.com/user-attachments/assets/6a3ebf1b-b6a8-4dfb-a5b6-c272f268d24e" />




## 📈 Use Cases

* Country-wise disease trend analysis
* Healthcare accessibility insights
* Vaccine availability impact analysis
* Public health decision-making
* Cost vs recovery analysis

---

## 🔥 Learnings

* Built production-style Airflow DAG with sensors and operators
* Implemented multi-layer data architecture (staging → transform → reporting)
* Used dynamic task generation in Airflow
* Designed BI-ready data models using BigQuery views

---

## 📌 Future Enhancements

* Add incremental data loads
* Implement data quality checks (Great Expectations)
* Add partitioning & clustering in BigQuery
* Deploy using Docker / Cloud Composer
* Integrate real-time streaming data

---

## 👤 Author

Kushan Pathak
Data Analyst | Data Engineering Enthusiast
