# Write your MySQL query statement below
select Person.firstName,Person.lastName,city,state 
from person left join Address 
on person.personid=address.personid