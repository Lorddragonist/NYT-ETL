# Remember to read the instructions in the task description
# Your implementation here
from extract import extract_data
from transform import transform_data
from load import load_data


# Pipeline that orchestrates the ETL process
def run_etl():
    # Extraction
    extract_data()
    # Transformation
    transform_data()
    # Loading
    load_data()


if __name__ == "__main__":
    run_etl()
