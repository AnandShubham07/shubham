# Write your MySQL query statement below
select a1.machine_id,Round(Avg(abs(a1.timestamp-a2.timestamp)),3)as processing_time 
from Activity a1 join Activity a2 
    on  a1.activity_type='start' 
        and a2.activity_type='end' 
        and a1.process_id=a2.process_id 
        and a1.machine_id=a2.machine_id  
    group by machine_id order by a1.machine_id;