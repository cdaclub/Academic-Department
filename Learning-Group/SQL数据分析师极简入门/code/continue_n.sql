select count(distinct userId) num_users
from
(select userId,b_createdTime,count(1) cts
from
    (select *,date_sub(a_createdTime,interval a_rk day ) b_createdTime
    from
        (
        select userID,a_createdTime,row_number() over(partition by userId order by a_createdTime) a_rk
        from
            (
            select userID,date(from_unixtime(createdTime)) a_createdTime
            from user_active_log
            where substr(from_unixtime(createdTime),1,7) = '2021-12'
            group by userId,a_createdTime
            ) t0
        ) t1
    ) t2 group by userId,b_createdTime having  count(1)>6
) t3;
