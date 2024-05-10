UPDATE tb_schedules_and_actuals

--Updating the values that match in the filters activity id
SET c_scheduledstart = strftime('%Y-%m-%d %H:%M:%f', datetime(c_scheduledstart, '-1 hours'))

WHERE c_id IN (

    --Selecting the activity code to update
    SELECT a.c_id
    FROM tb_schedules_and_actuals a
             --Right Join takes only the elements that matches with the second table
             RIGHT JOIN
         (
             --Obtenining the min start time of the agents on '2024-03-10'
             SELECT c.c_agentid, MIN(c.c_scheduledstart) AS c_scheduledstart
             FROM tb_schedules_and_actuals c
             WHERE strftime('%Y-%m-%d', c.c_scheduledstart) = '2024-03-10'
               --Filtering the agents on Manager 1 Team
               AND c.c_agentid IN (
                 --Team of Manager 1
                 SELECT d.c_id
                 FROM tb_agentdata d
                 WHERE d.c_manager = 'Manager 1')
             GROUP BY c.c_agentid) b
         ON a.c_agentid = b.c_agentid
             AND a.c_scheduledstart = b.c_scheduledstart)

