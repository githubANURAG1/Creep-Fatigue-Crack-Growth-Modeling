create table crack_data(crack_length float,crack_opening float,crosshead float,cycle_number int, cycles int,displacement float,force_val float,measuring_voltage float,reference_voltage float ,strain float,stress float,time float,key_val float)

select * from crack_data;
drop table crack_data;
truncate table crack_data;
select count(*) from crack_data;

show variables like 'max_allowed_packet';
set global max_allowed_packet=838860800;

select avg(crack_length),cycles
from crack_data
where cycles !=0
group by cycles;

select crack_length, time
from crack_data;

select avg(crack_length)
from crack_data
group by cycles;

select avg(time)/3600
from crack_data
group by cycles;