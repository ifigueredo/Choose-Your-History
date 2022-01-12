create database if not exists ChoseYourHistory;
use ChoseYourHistory;

#Creacion de tablas 

create table if not exists Users(
id_user int primary key,
Username varchar(45) ,
Password varchar(45),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45) );

create table if not exists Characters(
id_character int Primary key,
Name varchar(45),
Description varchar(45),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));


create table if not exists Steps(
id_steps int primary key,
Name varchar(45),
Description varchar(450),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));

create table if not exists Adventures(
id_adventures int primary key,
Name varchar(45),
Description varchar(45),
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));

create table if not exists Options(
id_options int primary key,
Name varchar(45),
Description varchar(45),
Response int,
id_adventures int,
id_steps int ,
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));


create table if not exists Game(
id_game int primary key,
id_user int,
id_character int,
id_adventure int,
game_date datetime,
usuariocreacion varchar(45),
fechacreacion datetime,
usuariomodificacion varchar(45),
fechamodificacion varchar(45));

create table if not exists Actions(
id_action int primary key,
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



Alter table Users 
modify Username varchar(45) Unique Not null,
modify Password varchar(45) Not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;

Alter table Steps 
modify Name varchar(45) Unique Not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;


Alter table Options 
modify Name varchar(45) Unique Not null,
modify Response varchar(450) Not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;


Alter table Game 
Add constraint fk_game_users foreign key (id_user) references Users(id_user),
Add constraint fk_game_character foreign key (id_character) references Characters(id_character),
Add constraint fk_game_adventure foreign key (id_adventure) references Adventures(id_adventures),
modify game_date datetime not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;

Alter table Characters 
modify Name varchar(45) Unique not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;

Alter table Adventures 
modify Name varchar(45) Unique not null,
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;


Alter table Actions 
Add constraint fk_actions_users foreign key (id_user) references Users(id_user),
Add constraint fk_actions_steps foreign key (id_steps) references Steps(id_steps),
Add constraint fk_actions_adventure foreign key (id_adventures) references Adventures(id_adventures),
Add constraint fk_actions_options foreign key (id_options) references Options(id_options),
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;


