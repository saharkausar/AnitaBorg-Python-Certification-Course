DROP DATABASE birthdayDB;
CREATE DATABASE birthdayDB; 
USE birthdayDB;

create table tourneys(Name varchar(100), friend_num int, tourney_win int, best_score int, shoe_size int);
insert into tourneys values("Sally", 1, 30, 98, 6);
insert into tourneys values("Jeff", 2, 18, 120, 9);
insert into tourneys values("Ryan", 3, 23, 89, 10);

create table dinners(Name varchar(100), Birthdate varchar(100), Entree varchar(100), Side varchar(100), Dessert varchar(100));
insert into dinners values("Sally", "10/16/1995", "Pizza", "Fries", "Icecream");
insert into dinners values("Jeff", "08/15/1991", "Chicken", "Potatoes", "Pie");
insert into dinners values("Ryan", "02/23/2000", "Sushi", "Salad", "Mochi");

select * from tourneys;
select * from dinners;

select Name from dinners where Name = 'Name';