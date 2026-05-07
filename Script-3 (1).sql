
CREATE TABLE muestra (valor INTEGER,
PRIMARY KEY (valor)

);

INSERT IGNORE INTO muestra
VALUES 
(1),
(1),
(2),
(3),
(3),
(4);
	

SELECT DISTINCT valor FROM muestra;