CREATE TABLE Rellenado(
 Fila  int NOT NULL ,
 Aplicacion varchar(25) NOT NULL ,
 Estado varchar(25)NOT NULL,
  PRIMARY KEY (Fila,Aplicacion,Estado)
);

INSERT INTO Rellenado (Fila,Aplicacion,Estado)
VALUES
(1,'Web','Aprobado'),
(2,'','Fallo'),
(3,'','Fallo'),
(4,'','Fallo'),
(5,'App','Aprobado'),
(6,'','Fallo'),
(7,'','Fallo'),
(8,'','Aprobado'),
(9,'','Aprobado'),
(10,'RESTAPI','Fallo'),
(11,'','Fallo'),
(12,'','Fallo');


SELECT 
    Fila,
    Estado,
    CASE 
        WHEN Fila <= 4 THEN 'Web'
        WHEN Fila <= 9 THEN 'App'
        ELSE 'RESTAPI'
    END AS Aplicacion
FROM Rellenado;





