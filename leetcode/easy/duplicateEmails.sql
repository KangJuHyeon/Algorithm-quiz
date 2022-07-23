/* 문제풀이(1) */
select distinct Email 
from Person 
order by rand() 
limit 1;

/* 문제풀이(2) */
select Email 
from Person
group by Email
having count(*) > 1;