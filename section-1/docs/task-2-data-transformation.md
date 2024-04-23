# Task 2: Data Transformation

**Task**: Transform Data from New York Times API

**Objective**: The objective of this task is to demonstrate your ability to transform and prepare data. 

## Requirements

- Use the data extracted in Task 1.
- From the data extracted, you must obtain the following information per article:
  - `_id`
  - `web_url`
  - `abstract`
  - `print_section`
  - `print_page`
  - main `headline`
  - count of `multimedia` elements
  - average of `multimedia` height elements
  - median of `multimedia` width elements
  - count of `keywords` elements
  - `document_type`
  - `pub_date` formatted as `YYYY-MM-DD`
  - `word_count`
  
> [!NOTE]
> If any of the fields are not present in the data, you should keep the field as `None` or `null`.


## Deliverables:

- Python file named `transform.py` with the code used to transform the information. 
- Code should transform data from Task 1 into the format described above.
- Code should contain a method or function called `test_duplicate_ids` that returns `True` and prints a message in console if there are duplicate `_id` values within the data, else return `False`
- Code should contain a method or function called `count_articles_wordcount_ge50` that prints and returns the number of articles with `word_count` greater than or equal to 50.

---
Go to next task: [Task 3: Data Loading](task-3-data-loading.md)

Go back to section 1 docs: [s1-README.md](../s1-README.md)

Go back to the main docs: [README.md](../../README.md)