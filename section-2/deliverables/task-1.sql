UPDATE tb_schedules_and_actuals

-- Adjusts the start time by subtracting one hour for the entries matching the specified criteria
SET c_scheduledstart = strftime('%Y-%m-%d %H:%M:%f', datetime(c_scheduledstart, '-1 hours'))

WHERE c_id IN (

    -- Selects the activity code IDs to update from `tb_schedules_and_actuals`
    SELECT a.c_id
    FROM tb_schedules_and_actuals a
             -- A RIGHT JOIN is used to select only the matching elements from the second table
             RIGHT JOIN
         (
             -- Gets the earliest start time of agents scheduled for '2024-03-10'
             SELECT c.c_agentid, MIN(c.c_scheduledstart) AS c_scheduledstart
             FROM tb_schedules_and_actuals c
             WHERE strftime('%Y-%m-%d', c.c_scheduledstart) = '2024-03-10'
               -- Filters agents who are part of 'Manager 1' team
               AND c.c_agentid IN (
                 -- List of agents under 'Manager 1'
                 SELECT d.c_id
                 FROM tb_agentdata d
                 WHERE d.c_manager = 'Manager 1')
             GROUP BY c.c_agentid) b
        -- Matches entries where the agent and start time align with the minimum start time found
         ON a.c_agentid = b.c_agentid
             AND a.c_scheduledstart = b.c_scheduledstart)
