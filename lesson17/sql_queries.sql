CREATE TABLE public.directors (
	director_id serial primary key,
	director_name varchar(256) not null

);

CREATE TABLE public.movies (
	id serial primary key,
	movie_name varchar(256) not null,
	release_year int not null,
	director_id int not null,
	CONSTRAINT fk_director
      FOREIGN KEY(director_id)
	  REFERENCES directors(director_id)

);


insert into directors(director_name) values ('Frank Darabont');
insert into directors(director_name) values ('Francis Ford Coppola');
insert into directors(director_name) values ('Steven Spielberg');
insert into directors(director_name) values ('Quentin Tarantino');
insert into directors(director_name) values ('James Cameron');


INSERT INTO movies (id, movie_name, release_year, director_id) VALUES(1, 'The Godfather', 1972, 2);
INSERT INTO movies (id, movie_name, release_year, director_id) VALUES(2, 'The Shawshank Redemption', 1994, 1);
insert into movies (id, movie_name, release_year, director_id) values (3, 'The Green Mile', 1999, 1);
insert into movies (id, movie_name, release_year, director_id) values (4, 'The Mist', 2007, 1);
insert into movies (id, movie_name, release_year, director_id) values (5, 'Dracula', 1992, 2);
insert into movies (id, movie_name, release_year, director_id) values (6, 'Gardens of stone', 1987, 2);
insert into movies (id, movie_name, release_year, director_id) values (7, 'Pulp fiction', 1994, 4);


alter table movies add length_in_min float;

update movies set length_in_min = 175 where id = 1;
update movies set length_in_min = 142 where id = 2;
update movies set length_in_min = 189 where id = 3;
update movies set length_in_min = 126 where id = 4;
update movies set length_in_min = 128 where id = 5;
update movies set length_in_min = 112 where id = 6;
update movies set length_in_min = 154 where id = 7;

select * from movies;
select * from directors;

create table series (
   id serial primary key,
   series_name varchar(128) not null,
);

INSERT INTO movies (movie_name, release_year, director_id, length_in_min) VALUES('The Godfather 2', 1974, 2, 202);
INSERT INTO movies (movie_name, release_year, director_id, length_in_min) VALUES('The Godfather 3', 1990, 2, 162);
insert into movies (movie_name, release_year, director_id, length_in_min) values('Avatar', 2009, 5, 161);
insert into movies (movie_name, release_year, director_id, length_in_min) values('Avatar 2', 2022, 5, 192);

select * from movies;

insert into series (series_name) values('The Godfather');
insert into series (series_name) values('Avatar');

select * from series;

alter table movies add series_id int;

alter table series drop constraint fk_movie;

alter table movies add constraint fk_series foreign key(series_id) references series(id);

update movies set series_id = 1 where id = 1 or id = 8 or id = 9;
update movies set series_id = 2 where id = 10 or id = 11;

create table actors (
	id serial primary key,
	actor_name varchar(256) not null,
	birth_year smallint not null, check (birth_year > 1800)
);

create table movie_actors (
	id serial primary key,
	movie_id int not null,
	actor_id int not null,
	is_main_role bool not null,
	constraint fk_movie_id foreign key (movie_id) references movies(id),
	constraint fk_actor_id foreign key (actor_id) references actors(id)
);

-- Display The Godfather's actors

select
	m.movie_name,
	a.actor_name,
	ma.is_main_role
from
	movies m
join movie_actors ma on
	m.id = ma.movie_id
join actors a on
	a.id = ma.actor_id
where m.movie_name = 'The Godfather';

-- Display a table that contains all the data for all the movies (including to which series the movie is related, and director’s name)

select
	m.id,
	movie_name,
	release_year,
	d.director_name,
	length_in_min,
	s.series_name
from
	movies m
left join series s on
	m.series_id = s.id
left join directors d on
	d.director_id = m.director_id;

-- Display a table that contains series name and amount of movies in the series

select
	series_name,
	count(*)
from
	movies m
left join series s on
	m.series_id = s.id
group by s.series_name
having s.series_name is not null;

-- Display a table that shows director name and amount of movies for this director

select
	director_name,
	count(id) as movies_count
from
	movies m
right join directors d on
	d.director_id = m.director_id
group by d.director_name;

-- Display a table that contains all the directors in the db, amount of movies for each director, and amount of series for each

select
	director_name,
	count(m.id) as movies_count,
	count(distinct(s.id)) as series_count
from
	movies m
left join directors d on
	d.director_id = m.director_id
left join series s on
	s.id = m.series_id
group by
	d.director_name;

--Display all the movies, their series and directors that have at least 2 movies in the series
--Display movies that are not part of any series and their directors



