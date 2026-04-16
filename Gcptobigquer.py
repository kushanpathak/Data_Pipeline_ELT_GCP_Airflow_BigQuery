# Airflow DAGs

## gcs_to_bigquery_dag.py
Pipeline to ingest CSV data into BigQuery using GCS staging.


from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}


with DAG(
    dag_id='load_gcs_to_bq',
    default_args=default_args,
    description='Loading a CSV file from GCS to BigQuery',
    schedule_interval=None,  # Set as required (e.g., '@daily', '0 12 * * *')
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['bigquery', 'gcs', 'csv'],
) as dag:


   load_csv_to_bigquery = GCSToBigQueryOperator(
        task_id='load_csv_to_bq',
        bucket='bkt-src-healthcare-data', 
        source_objects= ['global_health_data.csv'],  # Path to your file in the bucket
        destination_project_dataset_table='tt-dev-02.stag_dataset.healthcare_data',  # Replace with your project, dataset, and table name
        source_format='CSV', 
        allow_jagged_rows=True,
        ignore_unknown_values=True,
        write_disposition='WRITE_TRUNCATE',  
        skip_leading_rows=1,  # Skip header row
        field_delimiter=',',  # Delimiter for CSV, default is ','
        autodetect=True,  
        #google_cloud_storage_conn_id='google_cloud_default',  # Replace with your Airflow GCP connection ID if not default
        #bigquery_conn_id='google_cloud_default',  # Replace with your Airflow BigQuery connection ID if not default
    )
