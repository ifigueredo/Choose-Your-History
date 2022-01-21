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
Description varchar(450),
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
id_adventure int,
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
 
 
 #Alteracion de tablas 



Alter table USER 
modify Username varchar(45) Unique Not null,
modify Password varchar(45) Not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;

Alter table STEP 
modify Name varchar(45) Unique Not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;


Alter table OPTIONS 
modify Name varchar(45) Unique Not null,
modify Response varchar(450) Not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;


Alter table GAME 
Add constraint FK_GAME_USER foreign key (id_user) references USER(id_user),
Add constraint FK_GAME_CHARACTER foreign key (id_character) references CHARACTERS(id_character),
Add constraint FK_GAME_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventures),
modify game_date datetime not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;

Alter table CHARACTERS 
modify Name varchar(45) Unique not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;

Alter table ADVENTURE 
modify Name varchar(45) Unique not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;


Alter table ACTION 
Add constraint FK_ACTION_USER foreign key (id_user) references USER(id_user),
Add constraint FK_ACTION_STEP foreign key (id_steps) references STEP(id_steps),
Add constraint FK_ACTION_ADVENTURE foreign key (id_adventures) references ADVENTURE(id_adventures),
Add constraint FK_ACTION_OPTIONS foreign key (id_options) references OPTIONS(id_options),
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;
