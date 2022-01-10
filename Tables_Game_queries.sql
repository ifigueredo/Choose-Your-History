
#Tables Creation

create database Game;
use Game ;

create table User (
id_user int primary key,
Name varchar(30) unique,
password varchar(30));


create table Characters(
id_character int Primary key,
Name varchar(30) unique,
Description varchar(400));

create table Histories(
id_histories int Primary key,
Name varchar(30) unique,
Description varchar(400));


create table Steps(
id_steps int Primary key,
Description varchar(400));


create table Options(
id_Options int Primary key,
Description varchar(400));

create table Games (
id_Game int primary key,
User_id int,
Character_id int,
History_id int,
Date datetime,
num_games int,
constraint Games_Userid foreign key (User_id)references User(id_user),
constraint Games_ foreign key (User_id)references User(id_user));