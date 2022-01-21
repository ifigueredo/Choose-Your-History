USE CHOSE_YOUR_STORY;

describe ADVENTURE;

insert into ADVENTURE values('1','La Busqueda de la Espada','Un heroe se envarca en una aventura en busca de una legendaria espada para que le ayude a erradicar el mal','Edu',SYSDATE(),NULL,NULL); 

insert into ADVENTURE(Name,Description,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion) values('Alicia en el país de las maravillas','Unete a la aventura de la pequeña Alicia en una historia llena de recuerdos y guiños a otros mundos','Edu',SYSDATE(),NULL,NULL); 



#OPTIONS

describe OPTIONS;
select * from OPTIONS;


# STEP
Describe STEP;
Select * from STEP;


Insert into STEP values(1,'Primer Paso','%personaje% está en el inicio del Bosque Maldito,
 Donde se encuentra 3 caminos ... ¿por donde irá?',user(),sysdate(),null,null,false,1); 

Insert into STEP (Name,Description,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion,final_step,id_adventures) values ('Paso2(1)','Efectivamente, el puente es el cámino mas corto, 
no contabas con que el puente se descolgaría, 
Y no sobrevives a la caida. FIN',user(),sysdate(),null,null,false,1);

Insert into STEP (Name,Description,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion,final_step,id_adventures) values ('Paso2(2)','Sorteando los peligros, llegas de noche al centro 
del bosque, y ves clavada en un cadaver una 
espada llameante que te susurra al oido... 
¿Que haces?',user(),sysdate(),null,null,false,1);

Insert into STEP (Name,Description,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion,final_step,id_adventures) values ('Paso2(3)','%personaje% está en el inicio del Bosque Maldito,
 Donde se encuentra 3 caminos ... ¿por donde irá?',user(),sysdate(),null,null,false,1);

Insert into STEP (Name,Description,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion,final_step,id_adventures) values ('Paso3(1)','Matas a toda tu gente, e invadido por la tristeza, decides arrancarte la vida. FIN',
user(),sysdate(),null,null,false,1);


Insert into STEP (Name,Description,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion,final_step,id_adventures) values ('Paso3(2)','Mas fuerte que nunca, decides que es el momento de erradicar el mal junto 
A tu nueva aliada, y te embarcas en una nueva aventura. FIN.',user(),sysdate(),null,null,true,1);


