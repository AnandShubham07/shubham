# Write your MySQL query statement below
select Department.name as Department ,e.name as Employee ,e.salary as Salary 
from
    Employee e left join Department 
    on e.departmentId=Department.id
    where e.salary in (select Max(e2.salary) from Employee e2 where e.departmentId=e2.departmentId )
   ;