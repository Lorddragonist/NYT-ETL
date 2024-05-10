
--Creates a view called vw_entity_billable_conformance
CREATE VIEW vw_entity_billable_conformance AS
-- Selects the entity name and the desired date format
SELECT
    d.c_name AS entity_name,  -- Name of the entity (aliased as 'entity_name')
    strftime('%Y-%m-%d', b.c_scheduledstart) AS date,  -- Scheduled start date formatted as 'YYYY-MM-DD'

    -- Calculates the total sum of scheduled minutes by taking the difference in days between start and end columns
    SUM((JULIANDAY(c_scheduledend) - JULIANDAY(c_scheduledstart)) * 24 * 60) AS scheduled_minutes,

    -- Calculates the total sum of actual minutes by taking the difference in days between start and end columns
    SUM((JULIANDAY(c_actualend) - JULIANDAY(c_actualstart)) * 24 * 60) AS actual_minutes,

    -- Calculates the conformance percentage by comparing actual minutes to scheduled minutes
    (
        SUM((JULIANDAY(c_actualend) - JULIANDAY(c_actualstart)) * 24 * 60) /
        SUM((JULIANDAY(c_scheduledend) - JULIANDAY(c_scheduledstart)) * 24 * 60)
        ) * 100 AS conformance_pct  -- Calculates conformance percentage (aliased as 'conformance_pct')

-- From the schedules and actuals table (tb_schedules_and_actuals)
FROM tb_schedules_and_actuals b

-- Inner join with the entity assignments table (tb_entityassignments)
         INNER JOIN tb_entityassignments c ON b.c_agentid = c.c_agentid

-- Inner join with the entity table (tb_entity)
         INNER JOIN tb_entity d ON d.c_id = c.c_entityid

-- Filters rows where activity codes are billable
WHERE c_activitycodeid IN (
    SELECT a.c_id FROM tb_activitycodes a
    WHERE a.c_billable = 1  -- Filters only billable activity codes
)

-- Groups results by entity name and the formatted scheduled date
GROUP BY
    d.c_name,
    strftime('%Y-%m-%d', b.c_scheduledstart);
