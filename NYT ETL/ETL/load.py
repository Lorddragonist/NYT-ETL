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
def test_number_of_records(table_name, engine_conn, df):
    query = f"SELECT COUNT(*) AS elements FROM {table_name};"
    counter = pd.read_sql_query(query, con=engine_conn)
    counter = counter['elements'].to_list()
    counter = int(counter[0])

    expected_number = df.shape[0]

    if counter == expected_number:
        print(f"\nTable '{table_name}' has {expected_number} records. It is the expected number of records.")
    else:
        print(f"\nTable '{table_name}' has {counter} records. It's not the expected number {expected_number}.")


# Main method of the loading process
def load_data(df):

    # Database connection
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    server = 'localhost:5432'
    database = 'NYT'

    url = f'postgresql+psycopg2://{user}:{password}@{server}/{database}'

    # Create engine with SQL Alchemy and LibSQL
    engine = create_engine(url)
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
    test_number_of_records(table_target, engine, df)
