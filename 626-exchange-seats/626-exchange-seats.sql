# Write your MySQL query statement below

select
    if(mod(id, 2)=0, 
       id-1,
       if(
           id != (select count(*) from Seat),
           id+1,
           id
       )
    ) as id,
    student
from
    Seat
order by id;