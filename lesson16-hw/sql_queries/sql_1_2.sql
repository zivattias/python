--With GROUP BY:
--Get total amount of customers for each marital status
select
	count(*),
	marital_status
from
	superstore_data
group by
	marital_status
order by
	count;
--Get total purchases of sweets and wine per each education status
select
	sum(mntsweetproducts) as total_sweets,
	sum(mntwines) as total_wine,
	education
from
	superstore_data
group by
	education;
--Get the maximum and the minimum age of customers with the same marital status and education ordered by education, and then minimum age
select
	education,
	marital_status,
	min(date_part('year', now()) - year_birth) as min_age,
	max((date_part('year', now()) - year_birth)) as max_age
from
	superstore_data
group by
	education,
	marital_status
order by
	education,
	min(date_part('year', now()) - year_birth);
--Get amount of customers of each age that have accepted the offer and have not complained in the past 2 years
select
	count(*),
	date_part('year', now()) - year_birth as _age
from
	superstore_data
group by
	distinct(date_part('year', now()) - year_birth),
	response = 1,
	complain = 0
order by
	date_part('year', now()) - year_birth;
--Get the youngest customer for each education level (id,  education, age)
select
	distinct on
	(education)
	education,
	id,
	min(date_part('year', now()) - year_birth) as min_age
from
	superstore_data
group by
	education,
	id
order by
	education,
	min_age;
--Get average amount of purchases for each product type (fish, meat, sweets, wine, gold) for groups of customers with the same amounts of children at home (kids and teens)
select
	distinct on
	(kidhome + teenhome) kidhome + teenhome as total_kids_home,
	round(avg(mntfishproducts)) as avg_meat,
	round(avg(mntmeatproducts)) as avg_meat,
	round(avg(mntsweetproducts)) as avg_sweets,
	round(avg(mntwines)) as avg_wines,
	round(avg(mntgoldprods)) as avg_gold
from
	superstore_data
group by
	total_kids_home,
	mntfishproducts,
	mntmeatproducts,
	mntsweetproducts,
	mntwines,
	mntgoldprods;
--Get the youngest customer id and birth year, for every possible number of teens at home that exist in the table
select
	distinct on
	(teenhome) teenhome,
	id,
	min(date_part('year', now()) - year_birth) as min_age
from
	superstore_data
group by
	id,
	teenhome;
--Get total number of customers who accepted and did not accept the offer
select
	count(*)
from
	superstore_data
group by
	response
order by
	response = 1;
--Get average number of kids and average number of teens for customers with the same marital status (per status)
select
	distinct on
	(marital_status) marital_status,
	round(avg(kidhome)) as avg_k,
	round(avg(teenhome)) as avg_t
from
	superstore_data
group by
	marital_status,
	kidhome,
	teenhome;
--Get the minimum, maximum, and average income for every education level of customers
select
	education,
	min(income) as min_income,
	max(income) as max_income,
	round(avg(income)) as avg_income
from
	superstore_data
group by
	education
order by
	education;