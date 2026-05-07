CREATE TABLE Paginacion(
 id_orden int NOT NULL,
 id_cliente int NOT NULL,
 fecha DATE NOT NULL ,
 cantidad varchar(25) NOT NULL,
 estado varchar(25),
  PRIMARY KEY (id_orden,id_cliente,fecha,cantidad,estado)
);

INSERT INTO Paginacion
VALUES
	(1, 1001 ,'2025-01-01' ,'$100', 'JAL'),
	(2 ,1001 ,'2025-01-01' ,'$100' ,'COL'),
	(3, 1001 ,'2025-01-03' ,'$100' ,'JAL'),
	(4, 1001 ,'2025-01-02' ,'$150' ,'JAL'),
	(5, 1001 ,'2025-01-02' ,'$100' ,'JAL'),
	(6, 2002 ,'2025-01-05' ,'$50' ,'COL'),
	(7, 2002 ,'2025-01-01' ,'$150' ,'JAL'),
	(8, 3003 ,'2025-01-03' ,'$100' ,'COL'),
	(9, 3003 ,'2025-01-04' ,'$100' ,'COL'),
	(10, 3003 ,'2025-01-01' ,'$75' ,'JAL'),
	(11, 4004 ,'2025-01-02' ,'$75' ,'JAL'),
	(12, 4004 ,'2025-01-02' ,'$100' ,'COL'),
	(13, 4004 ,'2025-01-05' ,'$100' ,'COL');

SELECT * FROM Paginacion ORDER BY id_orden ASC LIMIT 5 OFFSET 4;