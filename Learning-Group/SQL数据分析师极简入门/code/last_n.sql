select
    t1.first_time,
    sum( case when t1.delta_time = 1 then 1 else 0 end ) / count(distinct t1.userID)  day_1,
    sum( case when t1.delta_time = 2 then 1 else 0 end ) / count(distinct t1.userID) day_2,
    sum( case when t1.delta_time = 3 then 1 else 0 end ) / count(distinct t1.userID) day_3,
    sum( case when t1.delta_time = 5 then 1 else 0 end ) / count(distinct t1.userID) day_5,
    sum( case when t1.delta_time = 7 then 1 else 0 end ) / count(distinct t1.userID) day_7,
    sum( case when t1.delta_time = 30 then 1 else 0 end )/ count(distinct t1.userID) day_30
from
     (
        select
               userID,
               a_createdTime,
               first_value(a_createdTime) over(partition by userId order by a_createdTime ) first_time,
               datediff(a_createdTime , first_value(a_createdTime) over(partition by userId order by a_createdTime )) delta_time
        from
             (
                 select userID,date(from_unixtime(createdTime)) a_createdTime
                 from user_active_log
                 group by userId,a_createdTime
            )t0
    ) t1
group by t1.first_time
order by t1.first_time;
