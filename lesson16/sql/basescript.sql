select *
from superstore_data
where income > 100000;

select id, education, income, marital_status
from superstore_data
where income > 10000 and kidhome > 1;

select id, education, income, marital_status
from superstore_data
where income > 10000 and (kidhome > 1 or teenhome > 1) and education = 'PhD';

select count(*) from superstore_data;

select * from superstore_data where teenhome = 2;

select count(id) from superstore_data;

select count(*) from superstore_data where teenhome = 1;

select * from superstore_data where year_birth between 1970 and 1980;

select max(income) from superstore_data;
select min(income) from superstore_data;

select cast(avg(income)as decimal(10, 2)) as avg_income,
	   avg(mntwines) as avg_wines,
	   avg(mntfruits) as avg_fruits
from superstore_data;

select round(avg(income), 2) as avg_income,
	   avg(mntwines) as avg_wines,
	   avg(mntfruits) as avg_fruits,
	   min(income) as min_income
from superstore_data sd;

--select superstore_data.income from superstore_data;
--select sd.income from superstore_data sd;

select id, teenhome, kidhome, teenhome + kidhome as total_kids_per_id from superstore_data; 

select sum(teenhome + kidhome) as total_kids_of_all from superstore_data;

select income from (select * from superstore_data where id = 837) as new_table;

select * from superstore_data limit 10;

select *from superstore_data limit 1 offset 6;

select * 
from superstore_data 
where income is not null
order by income desc
limit 1; 

select * 
from superstore_data
where income = 
	(select max(income) from superstore_data);

select distinct(education) from superstore_data;
select education from superstore_data;

select education,
		round(avg(income), 0) as avg_income,
		round(min(income), 0) as min_income,
		round(max(income), 0) as max_income
from superstore_data
group by education
order by avg_income desc;

select education,
		marital_status ,
		count(id) as people_num,
		round(avg(income), 0) as avg_income,
		round(min(income), 0) as min_income,
		round(max(income), 0) as max_income
from superstore_data
group by education, marital_status 
order by education asc, marital_status asc, people_num asc;



select education,
		round(avg(income), 0) as avg_income,
		round(min(income), 0) as min_income,
		round(max(income), 0) as max_income,
		sum(kidhome + teenhome)  as total_kids
from superstore_data 
where kidhome + teenhome = 0
group by education;



select education,
		round(avg(income), 0) as avg_income,
		round(min(income), 0) as min_income,
		round(max(income), 0) as max_income
from superstore_data
group by education
having sum(kidhome + teenhome) = 0;


select education,
		round(avg(income), 0) as avg_income,
		round(min(income), 0) as min_income,
		round(max(income), 0) as max_income,
		sum(kidhome + teenhome)  as total_kids
from superstore_data 
where education != 'Basic'
group by education;


select education,
		round(avg(income), 0) as avg_income,
		round(min(income), 0) as min_income,
		round(max(income), 0) as max_income,
		sum(kidhome + teenhome)  as total_kids
from superstore_data
group by education
having education != 'Basic';

--select * from imdb_top where lower(movie_name) like '&king&';








