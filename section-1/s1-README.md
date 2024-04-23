# ETL Pipelines (Python)

- [Introduction](#introduction)
- [Recomendations](#recomendations)
- [About the NYT API](#about-the-nyt-api)
- [Tasks](#tasks)

## Introduction

The New York Times is an American newspaper based in New York City with worldwide influence and readership. As one of the longest-running newspapers in the United States, the NYT serves as a prominent source of domestic, national, and international news. 

The NYT provides several APIs that allow developers to access various data sources, including articles, semantic terms, and more.

Your task is to create an ETL pipeline in Python that extracts data from the New York Times `Article Search` API, transform the data into a specific format, and load the data into a database.

> [!TIP]
> Please read carefully the instructions and recommendations for each task in the `docs` folder.

## Recomendations

Before we start here are some key points to consider:

- All files must be saved under the `deliverables` folder.
- Include a requirements file (`.txt` or `.yml`) with the environment configuration for reproducibility at the `deliverables` folder (if possible)
- Consider writing reusable components that can be used across multiple ETL pipelines.
- Consider all security and performance aspects of your code. Don't include any sensitive information in your code. 
- For this test, please add a copy of your `.env` file called `.example.env` without sensitive information, or if you used local environment variables, please let us know in the pull request description.

## About the NYT API

To retrieve data from the New York Times API, you will need to obtain an API key. Here's how you can get an API key:
  - Visit the New York Times Developer Network website (https://developer.nytimes.com/).
  - Create a free account.
  - Follow the instructions to obtain an API key follow the instuctions at https://developer.nytimes.com/get-started, for this challenge you will need the `Article Search API`.

## Tasks

Here are the tasks:

1. [Task 1: Data Extraction](docs/task-1-data-extraction.md)
2. [Task 2: Data Transformation](docs/task-2-data-transformation.md)
3. [Task 3: Data Loading](docs/task-3-data-loading.md)
4. [Task 4: Pipeline](docs/task-4-pipeline.md)

Any issues or questions, please create an `Issue` in GitHub.

Hope you enjoy the challenge! :rocket:
