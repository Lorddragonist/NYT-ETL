# Task 1: Schedule Adjustments

**Task**: Update data from `tb_schedules_and_actuals` 

**Objective**: The objective of this task is to update the data in the `tb_schedules_and_actuals` table. 


## Requirements

The Workforce Management team is in charge of creating schedules for the agents. 

They noticed some agents arrived early to work on March 10, 2024.

It seems their schedules were generated incorrectly. Unfortunately, when they generated the schedules for Manager 1’s team, they overlooked the recent daylight saving time adjustments. As a result, the start times on their schedules are now off by one hour.

The WFM team asks you to update the first activity schedules start times with the following conditions:

- Adjust the initial scheduled start time (earliest activity by scheduled start time) of each agent from Manager 1 team on March 10, 2024, by subtracting one hour, ensuring that they begin on time.


### Example

Given the following data in the `tb_schedules_and_actuals` table for a particular agent of Manager 1 team on March 10, 2024:

| c_agentid | c_activitycodeid | c_scheduledstart | c_scheduledend | c_actualstart | c_actualend |
|----------|-------------|----------------------|-------------------|-------------------|-----------------|
| `da6b7d0`        | `8d305a7a`    | ***2024-03-10 07:00:00***  | 2024-03-10 08:00:00 | 2024-03-10 05:59:00 | 2024-03-10 07:45:00 |
| `da6b7d0`        | `eeff4a11`    | 2024-03-10 08:00:00  | 2024-03-10 09:00:00 | 2024-03-10 09:00:00 | 2024-03-10 09:45:00 |
| `da6b7d0`        | `9b0689b6`    | 2024-03-10 09:00:00  | 2024-03-10 10:00:00 | 2024-03-10 09:15:00 | 2024-03-10 10:00:00 |


The updated data should be:

| c_agentid | c_activitycodeid | c_scheduledstart | c_scheduledend | c_actualstart | c_actualend |
|----------|-------------|----------------------|-------------------|-------------------|-----------------|
| `da6b7d0`        | `8d305a7a`    | ***2024-03-10 06:00:00*** | 2024-03-10 08:00:00 | 2024-03-10 05:59:00 | 2024-03-10 07:45:00 |
| `da6b7d0`        | `eeff4a11`    | 2024-03-10 08:00:00  | 2024-03-10 09:00:00 | 2024-03-10 09:00:00 | 2024-03-10 09:45:00 |
| `da6b7d0`        | `9b0689b6`    | 2024-03-10 09:00:00  | 2024-03-10 10:00:00 | 2024-03-10 09:15:00 | 2024-03-10 10:00:00 |


## Deliverables

- Update the data in the `tb_schedules_and_actuals` table according to the requirements. 
- Include your SQL query in the file named `task-1.sql` at section 2 `deliverables` folder.


---
Go to next task: [Task 2: Reporting](task-2-reporting.md)

Go to schema docs: [SCHEMA.md](SCHEMA.md)

Go back to section 2 docs: [s2-README.md](../s2-README.md)

Go back to the main docs: [README.md](../../README.md)