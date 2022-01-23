create database if not exists CHOSE_YOUR_STORY;
use CHOSE_YOUR_STORY;

#Creacion de tablas 

create table if not exists USER(
id_user int primary key auto_increment,
Username varchar(45) ,
Password varchar(45),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45) );

create table if not exists CHARACTERS(
id_character int Primary key auto_increment,
Name varchar(45),
Description varchar(45),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));


create table if not exists STEP(
id_steps int primary key auto_increment,
Name varchar(45),
Description varchar(850),
id_adventures int,
id_options int ,
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));

create table if not exists ADVENTURE(
id_adventures int primary key auto_increment,
Name varchar(45),
Description varchar(450),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));

create table if not exists OPTIONS(
id_options int primary key auto_increment,
Name varchar(45),
Description varchar(45),
Response int,
id_adventures int,
id_steps int ,
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));


create table if not exists GAME(
id_game int primary key auto_increment,
id_user int,
id_character int,
id_adventures int,
game_date datetime,
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));

create table if not exists ACTION(
id_action int primary key auto_increment,
id_user int,
id_adventures int,
id_steps int,
id_options int,
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45)
 );
 
 
 create table if not exists ANSWERS(
id_answers int primary key auto_increment,
Name varchar(45),
id_user int,
id_adventures int,
id_steps int,
id_options int,
Description varchar(450),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));
 
 
