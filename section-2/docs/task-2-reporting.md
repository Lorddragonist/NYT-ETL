# Task 2: Reporting

**Task**: Create a view in the database given a set of requirements. 

**Objective**: The objective of this task is to demonstrate your ability to create a view in a database. 


## Requirements

Management plays a crucial role in the success of any organization. They need to have access to real-time data to make informed decisions.

Conformance is a key performance indicator, which is the time the agent complies with the total time scheduled for a particular activity, regardless of when it occurs (even if it deviates from the original schedule)

Conformance can be calculated as follows:

```
conformance_pct = (actual_minutes / scheduled_minutes) x 100
```

Management wants to have a general overview per day of their business taking into account only billable activities.


## Deliverables

- Create a view called `vw_entity_billable_conformance` that contains the following columns:
    - `entity_name`: The name of the entity
    - `date`: date in `YYYY-MM-DD` format
    - `scheduled_minutes`: Total billable scheduled minutes for the entity per day
    - `actual_minutes`: Total billable actual minutes for the entity per day
    - `conformance_pct`: Conformance percentage for the entity per day



- Include the query to create the view in a file named `task-2.sql` at section 2 `deliverables` folder.


---
Go to next section: [Section 3: Presentation and Code Review](../../section-3/s3-README.md)

Go to schema docs: [SCHEMA.md](SCHEMA.md)

Go back to section 2 docs: [s2-README.md](../s2-README.md)

Go back to the main docs: [README.md](../../README.md)