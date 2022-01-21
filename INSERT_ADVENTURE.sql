use CHOSE_YOUR_STORY;
describe ADVENTURE;

insert into ADVENTURE values(1,'La historia de Jordi','No se','LaMaquinita',sysdate(),null,null);

insert into ADVENTURE values('1','La Busqueda de la Espada','Un heroe se envarca en una aventura en busca de una legendaria espada para que le ayude a erradicar el mal','Edu',SYSDATE(),NULL,NULL); 

insert into ADVENTURE(Name,Description,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion) values('Alicia en el país de las maravillas','Unete a la aventura de la pequeña Alicia en una historia llena de recuerdos y guiños a otros mundos','Edu',SYSDATE(),NULL,NULL); 

 
 
 SELECT * FROM ADVENTURE
