# Write your MySQL query statement below

# with three as (
#     select *, dense_rank() over (partition by departmentId order by salary desc) as 'Rank'
#     from Employee
# )

# select 
#     b.name as Department, a.name as Employee, a.salary as Salary 
# from 
#     three a left join Department b
#     on a.departmentId = b.id
# where
#     a.Rank <= 3
    
select 
    b.name as Department, a.name as Employee, a.salary as Salary 
from 
    (
        select *, dense_rank() over (partition by departmentId order by salary desc) as 'Rank'
        from Employee
    ) a left join Department b
    on a.departmentId = b.id
where
    a.Rank <= 3