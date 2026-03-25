CREATE  TABLE Desagrupacion(
	producto varchar(50) NOT NULL,
	Cantidad int NOT NULL,
PRIMARY KEY (Cantidad,producto)
);

INSERT INTO  Desagrupacion
values
('Lapiz',3),
('Borrador',4),
('Cuaderno',2);

WITH Numeros AS (
    SELECT 1 AS numero UNION ALL
   SELECT 2 UNION ALL
    SELECT 3 UNION ALL
   SELECT 4 UNION ALL
    SELECT 5 
)
SELECT producto, 1 AS cantidad
FROM Desagrupacion
JOIN Numeros on numero <= cantidad;


