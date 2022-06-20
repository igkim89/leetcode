# Write your MySQL query statement below

select w1.id
from Weather w1, Weather w2
where w1.recordDate = date_sub(w2.recordDate, interval -1 day)
and w1.temperature > w2.temperature;