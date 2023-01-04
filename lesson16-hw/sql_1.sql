--Get all the data from superstore_data table (all the rows and all the columns)
select * from superstore_data;
--Get the amount of rows (records) in the superstore_data table
select count(*) as records from superstore_data;
--Get first 10 rows from the superstore_data table
select * from superstore_data limit 10;
--Get rows from 20 to 45 from the table
select * from superstore_data limit 25 offset 19;
--Get only id, year_birth, and marital_status columns for the 20 first rows of the table.
select id, year_birth, marital_status from superstore_data limit 20;
--Get ids of the customers who spent more than $1000 on wine in the past 2 years
select id from superstore_data where mntwines > 1000;
--Get the age and the marital status of the customers who spent less than $500 on fish products, and more than $500 on meat products in the past 2 years.
select date_part('year', now()) - year_birth as _age, marital_status from superstore_data where mntfishproducts < 500 and mntmeatproducts > 500;
--Get the amount of customers who accepted the offer
select count(*) as customers_amnt from superstore_data where response = 1;
--Get all the possible Education values that exist in the table. Sort them alphabetically
select distinct(education) from superstore_data order by education;
--Get the data for the youngest customer(s)
select * from superstore_data order by year_birth desc limit 1;
--Get id, age, and marital status of the oldest customers
select id, date_part('year', now()) - year_birth as _age, marital_status
from superstore_data where date_part('year', now()) - year_birth =
(select max(date_part('year', now()) - year_birth) from superstore_data);
--Get the average income of the customers who complained in the past 2 years
select avg(income) as avg_income_for_complaining_custs from superstore_data where complain != 0;
--Get the total number of kids of all the customers
select sum(kidhome + teenhome) from superstore_data;
--Get the id, income, and age, and marital status of the customers that made more purchases in web rather than in store
select id, income, date_part('year', now()) - year_birth as _age, marital_status from superstore_data
where numwebpurchases > numstorepurchases;
--Get the ids and total number of children (kids and teens) of the customers who made a purchase in the past 30 days
select id, kidhome + teenhome as total_kids from superstore_data where recency <= 30;
--Get the amount of customers who did not make any purchases of meat or fish in the past 2 years
select count(*) from superstore_data where mntmeatproducts = 0 or mntfishproducts = 0;
--Get all the details about the customer(s) who spent the maximum amount on gold products in the past 2 years
select * from superstore_data
where mntgoldprods = (select max(mntgoldprods) from superstore_data);
--Get ids and age of the customers who are between 20 and 40 years old, sort them from the oldest to the youngest
select id, date_part('year', now()) - year_birth as _age from superstore_data where date_part('year', now()) - year_birth between 20 and 40
order by date_part('year', now()) - year_birth desc;
--Get all the unique birth years of the customers
select distinct(year_birth) from superstore_data;
--Get top 10 customers who spent the biggest amount of money to buy sweets in the past 2 years
select * from superstore_data
order by mntsweetproducts desc
limit 10;
