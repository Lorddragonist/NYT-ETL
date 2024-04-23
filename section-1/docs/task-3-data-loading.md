# Task 3: Data Loading

**Task**: Load Data into a Database

**Objective**: The objective of this task is to demonstrate your ability to load data into a database.

## Requirements

- Use the data transformed in Task 2.
- Load the data into the given database. Credentials are provided in the email sent to you.

## Deliverables:

- Python file named `load.py` with the code used to load the information. 
- Code should contain table model definition.
- Code should create a table in the database called `tb_nytimes_articles`
- Code should load the data into `tb_nytimes_articles`
- Code should also contain a method or function called `test_table_exists` that validates that the table exists in the database.
- Code should also contain a method or function called `test_number_of_records` that validates that the number of records in the table is equal to the number of articles extracted in Task 1.


> [!NOTE]
> Database given is built on libSQL, the Open Contribution fork of SQLite. 
> 
> The database is hosted on a cloud server and accessible via url and api key provided in the email sent to you.
>
> Guides and examples: https://docs.turso.tech/sdk/python

> [!TIP]
> To verify the uploaded info to the database, we strongly recommend you to use [TablePlus](https://tableplus.com/) database client. It's free of charge and supports all operating systems (sadly, tools like DBeaver and DataGrip do not support live cloud connections to libSQL-based db's)

---
Go to next task: [Task 4: Pipeline](task-4-pipeline.md)

Go back to section 1 docs: [s1-README.md](../s1-README.md)

Go back to the main docs: [README.md](../../README.md)