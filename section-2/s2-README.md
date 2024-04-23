# SQL Assesment

- [Introduction](#introduction)
- [Recomendations](#recomendations)
- [About the database](#about-the-database)
- [Tasks](#tasks)

## Introduction

Workforce management is the strategic process of managing people and resources within a business environment. In the context of contact centers, WFM adapts this process to meet the unique needs of customer experience (CX) operations. Here are the key points: 

- WFM ensures that the right number of agents, with the right skills, are staffed at the right time and in the right places.
- It optimizes and automates scheduling based on factors like forecasted call volume, agent availability, and revenue targets.
- The goal is to balance operational efficiency, cost control, employee satisfaction, and customer service.
- WFM tools help achieve this balance by forecasting, scheduling, and managing intraday activities.

For this section of the test, you are given a dataset that contains historicals about scheduled and actual start and end times per activity per agent data, plus information around activities and agents. 



## Recomendations

1. We recommend you to use [TablePlus](https://tableplus.com/) database client to connect to the database. It's free of charge and supports all operating systems (sadly, tools like DBeaver and DataGrip do not support live cloud connections to libSQL-based db's)
2. Since you will have read and write access to the database, please be careful with the data you are inserting, updating, or deleting. 
   
   If by any chance you need to restore the database, you will have to your disposition backup tables with a `bkp` prefix. 
   
   To restore any table to its original state, you can simply copy the data from the backup table to the original table, here is an example: 

    ```sql
    TRUNCATE TABLE table_to_restore;
    INSERT INTO table_to_restore SELECT * FROM bkp_table_to_restore;
    ```

## About the database

The database schema can be found at [docs/SCHEMA.md](docs/SCHEMA.md)

The database is hosted on a cloud server and accessible via url and api key provided in the email sent to you.

Please take a look at the schema and understand the relationships between the tables before starting the tasks.

## Tasks

Here are the tasks:

1. [Task 1: Schedule Adjustments](docs/task-1-schedule-adjustments.md)
2. [Task 2: Reporting](docs/task-2-reporting.md)

Any issues or questions, please create an `Issue` in GitHub.

Hope you enjoy the challenge! :rocket: