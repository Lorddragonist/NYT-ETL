# Database Schema

- [`tb_schedules_and_actuals`](#tb_schedules_and_actuals)
- [`tb_agentdata`](#tb_agentdata)
- [`tb_activitycodes`](#tb_activitycodes)
- [`tb_entity`](#tb_entity)
- [`tb_entityassignments`](#tb_entityassignments)


## `tb_schedules_and_actuals`

This table contains agent schedule and actual primary information

**Foreign Keys** 
- `c_agentid` references `c_id` at `tb_agentdata`
- `c_activitycodeid` references `c_id` at `tb_activitycodes`

| Column Name | Description | Type |
|-------------|-------------| ---- |
| c_id        | Unique identifier for each record | INTEGER |
| c_agentid   | Unique identifier for each agent | STRING |
| c_activitycodeid | Unique identifier of the activity | STRING |
| c_scheduledstart | Scheduled start date and time of the activity | DATETIME |
| c_scheduledend | Scheduled end date and time of the activity | DATETIME |
| c_actualstart | Actual start date and time of the activity | DATETIME |
| c_actualend | Actual end date and time of the activity | DATETIME |


## `tb_agentdata`

This table contains data items describing agents.

| Column Name | Description | Type |
|-------------|-------------| ---- |
| c_id        | Unique identifier for each agent | STRING |
| c_name      | Name of the agent | STRING |
| c_manager   | Name of the agent's manager | STRING |

## `tb_activitycodes`

This table contains data items describing activity codes.

| Column Name | Description | Type |
|-------------|-------------| ---- |
| c_id        | Unique identifier for each activity | STRING |
| c_name      | Name of the activity | STRING |
| c_billable  | Boolean value indicating if the activity is billable - 0 for false, 1 for true | INTEGER |

## `tb_entity`

This table contains data items describing entity.

| Column Name | Description | Type |
|-------------|-------------| ---- |
| c_id        | Unique identifier for each entity | INTEGER |
| c_name      | Name of the entity | STRING |
| c_type      | Type of the entity | STRING |
| c_active    | Boolean value indicating if the entity is active - 0 for false, 1 for true | INTEGER |

## `tb_entityassignments`

This table contains the assignments of agents to entities.

**Foreign Keys**
- `c_entityid` references `c_id` at `tb_entity`
- `c_agentid` references `c_id` at `tb_agentdata`	

| Column Name | Description | Type |
|-------------|-------------| ---- |
| c_id        | Unique identifier for each entity assignment | INTEGER |
| c_entityid  | Unique identifier for each entity | STRING |
| c_agentid   | Unique identifier for each agent | STRING |




---

Go to task 1: [Task 1: Schedule Adjustments](task-1-schedule-adjustments.md)

Go to task 2: [Task 2: Reporting](task-2-reporting.md)
