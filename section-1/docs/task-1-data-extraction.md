# Task 1: Data Extraction

**Task**: Retrieve Data from New York Times API

**Objective**: The objective of this task is to demonstrate your ability to retrieve data from an API and save it into a common data format.

## Requirements
- Use the [New York Times Article Search API](https://developer.nytimes.com/docs/articlesearch-product/1/overview) to retrieve data.
- You must retrieve data for a specific search term (of your preference), such as "sports" or "economy", and retrieve at least 100 articles

## Deliverables

- Python file named `extract.py` with the code used to extract the information. 
- Extract code should have search term and number of articles to retrieve as input parameters.
- Extraction code should be able to handle pagination and retrieve all articles for the search term.
- Your code must also contain a method or function called `test_number_of_articles` that validates that there are at least 100 articles. 

> [!NOTE]
> The New York Times API limits the number of articles per request and also has a daily limit, you must workaround to retrieve at least 100 articles. Please also note, The New York Times API has a request limit per minute and per day (https://developer.nytimes.com/faq).
>
> We included an succesful API's response example in the `sample.json` file for reference.

--- 
Go to next task: [Task 2: Data Transformation](task-2-data-transformation.md) 

Go back to section 1 docs: [s1-README.md](../s1-README.md)

Go back to the main docs: [README.md](../../README.md)

