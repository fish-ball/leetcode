# Write your MySQL query statement below
select * 
from Stadium s
where s.people >= 100 and (
    (
        not exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id - 1)
        and exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id + 1)
        and exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id + 2)
    ) or (
        exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id - 1)
        and exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id + 1)
    ) or (
        not exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id + 1)
        and exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id - 1)
        and exists (select * from Stadium s1 where s1.people>=100 and s1.id = s.id - 2)
    ) 
)

