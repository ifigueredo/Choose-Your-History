describe OPTIONS;
SELECT* FROM OPTIONS;

insert into OPTIONS(Name,Description,Response,id_steps,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion) VALUES('Opcion1(1)',
'Escoge el camino de la izquierda, a lo lejos se ve un puente colgante.,','Decidido, piensas que es el camino más rapido 
Para atravesar el bosque.',1,user(),sysdate(),null,null);

select id_steps , Description from STEP where id_adventures = 1;


update OPTIONS SET id_adventures = 1 ;