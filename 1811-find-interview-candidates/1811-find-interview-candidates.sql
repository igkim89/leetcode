# Write your MySQL query statement below

with cte as (
    select contest_id, gold_medal medal from Contests
    union
    select contest_id, silver_medal medal from Contests
    union
    select contest_id, bronze_medal medal from Contests
)

select name, mail 
from 
    users 
where 
    user_id in (
        select distinct c1.medal 
        from 
            cte c1 join cte c2 on c1.contest_id=c2.contest_id+1
            join cte c3 on c1.contest_id=c3.contest_id-1
        where 
            c1.medal=c2.medal and c1.medal=c3.medal
    )
or user_id in (
    select gold_medal from Contests group by gold_medal having count(*)>=3
)