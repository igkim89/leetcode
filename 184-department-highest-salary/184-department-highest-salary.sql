# Write your MySQL query statement below

select s.name as Department, e.name as Employee, e.salary as Salary
from Employee e left join 
(
    select d.id as id ,d.name as name, max(e.salary) as salary
    from Employee e left join Department d
    on e.departmentId = d.id
    group by d.name
) s
on e.departmentId = s.id
where e.salary = s.salary;