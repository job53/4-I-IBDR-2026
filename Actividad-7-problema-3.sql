CREATE TABLE Fechas_futuras(
 inicio DATE NOT NULL ,
 final DATE NOT NULL ,
  PRIMARY KEY (inicio,final)
);

INSERT INTO Fechas_futuras
VALUES
	('2025-01-01','2025-01-05'),
	('2025-01-03','2025-01-09'),
	('2025-01-10','2025-01-11'),
	('2025-01-12','2025-01-16'),
	('2025-01-15','2025-01-19');

SELECT DATE_FORMAT(inicio,'%Y-%m-%d') as inicio, DATE_FORMAT(final,'%Y-%m-%d') as final FROM Fechas_futuras WHERE '2025-01-01' <= final AND '2025-01-05' >= inicio ;