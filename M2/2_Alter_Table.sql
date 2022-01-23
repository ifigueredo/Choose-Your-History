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
Add constraint FK_STEP_ADVENTURE foreign key (id_adventures) references ADVENTURE(id_adventures),
Add constraint FK_STEP_OPTIONS foreign key (id_options) references OPTIONS(id_options),
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
Add constraint FK_GAME_ADVENTURE foreign key (id_adventures) references ADVENTURE(id_adventures),
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



Alter table ANSWERS 
Add constraint FK_ANSWERS_STEP foreign key (id_steps) references STEP(id_steps),
Add constraint FK_ANSWERS_ADVENTURE foreign key (id_adventures) references ADVENTURE(id_adventures),
Add constraint FK_ANSWERS_OPTIONS foreign key (id_options) references OPTIONS(id_options),
modify usuariocreacion varchar(45) not null,
modify usuariomodificacion varchar(45) null,
modify fechacreacion datetime not null,
modify fechamodificacion datetime null;