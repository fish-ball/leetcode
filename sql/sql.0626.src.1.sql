# Write your MySQL query statement below
select if(a.id%2=1 and not exists(select id from seat b where b.id>a.id), a.id, (a.id+if(a.id%2=1,1,-1))) as id, 
    a.student
from seat a
order by a.id+if(a.id%2=1,1,-1)
