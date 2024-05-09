# Remember to read the instructions in the task description
# Your implementation here

# Libraries
from sqlalchemy import create_engine, inspect
import os
import pandas as pd


# test_table_exists is a function that validates that the table exists in the database
def test_table_exists(engine_conn, table_name):
    # Create an inspector object
    inspector = inspect(engine_conn)

    # Check if the table exists
    if inspector.has_table(table_name):
        print(f"\nTable '{table_name}' exists.")
    else:
        print(f"\nTable '{table_name}' does not exist.")


# Test_number_of_records is a function that validates that the number of records in the table is equal to the number
# of articles extracted in Task 1
def test_number_of_records(table_name, engine_conn, expected_number):
    query = f"SELECT COUNT(*) AS ELEMENTS FROM {table_name};"
    counter = pd.read_sql_query(query, con=engine_conn)
    counter = int(counter['ELEMENTS'].values[0])
    if counter == expected_number:
        print(f"\nTable '{table_name}' has {expected_number} records. It is the expected number of records.")
    else:
        print(f"\nTable '{table_name}' has {counter} records. It's not the expected number {expected_number}.")


# Main method of the loading process
def load_data():
    # Set origin for the json files
    origin_folder = os.path.join(os.getcwd(), 'csv_transformation_result')

    # DataFrame
    df = pd.read_csv(os.path.join(origin_folder, 'data_transformed.csv'))

    # Database connection
    url = os.getenv("TURSO_DATABASE_URL")
    auth_token = os.getenv("TURSO_AUTH_TOKEN")

    # Create engine with SQL Alchemy and LibSQL
    engine = create_engine(f'sqlite+{url}?authToken={auth_token}&secure=true')
    print('\nConnection successfully established')

    table_target = 'tb_nytimes_articles'

    # Bulk table, this line creates and feed the table
    # In case it is a full load I set the option if_exists='replace',
    # but if I want it to be incremental I would set if_exists='append'
    df.to_sql(table_target, con=engine, if_exists='replace', index=False)
    print('\nTable successfully created and updated')

    # Check if the table Exist
    test_table_exists(engine, table_target)

    # Check if the table Exist
    test_number_of_records(table_target, engine, 100)
