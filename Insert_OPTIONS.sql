select * from OPTIONS;
DESCRIBE OPTIONS;


INSERT INTO OPTIONS (Name,Description,Response,id_steps,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion) VALUES ('Opcion1(2)','Escoge el camino del centro, del que parecen provenir 
Ruidos de ramas al romperse y astillarse …','Piensas que para ser digno de la espada de las valkirias,
 Debes de afrontar tus miedos y peligros que acechan',1,user(),sysdate(),null,null);
 
 INSERT INTO OPTIONS (Name,Description,Response,id_steps,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion) VALUES ('Opcion1(3)','Escoge el camino de la derecha, lleno de flores, ardillas …',
 '¿Que malo puede pasar?, parece salido de Disney.
 Con lo que no contabas es que en realidad has entrado al laberinto
 Sombrio, y al rato vuelves a la misma encruzijada',1,user(),sysdate(),null,null);
 
 INSERT INTO OPTIONS (Name,Description,Response,id_steps,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion) VALUES ('Opcion2(2)','Arrancas la espada de cuajo, ¡ERES %personaje%!',
 '¡La espada es tuya, te invade la ira y la locura y vuelves 
Al poblado...',1,user(),sysdate(),null,null);

update OPTIONS SET id_steps = 2 , usuariomodificacion = user(),fechamodificacion=sysdate() where id_options = 4;

 
  INSERT INTO OPTIONS (Name,Description,Response,id_steps,usuariocreacion,fechacreacion,usuariomodificacion,fechamodificacion) VALUES ('Opcion2(3)','Atento a lo que dice la espada, escuchas levemente 
Las palabras ...matalos a todos ... por lo que decides
 No cogerla.',
 '¡La espada, al ver que eres un hombre fuerte y sensato, 
que eres capaz lo que dice, se entrega a ti como tu fiel 
Aliada.',2,user(),sysdate(),null,null);




 