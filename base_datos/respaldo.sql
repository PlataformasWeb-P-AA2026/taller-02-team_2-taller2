CREATE TABLE empleados (
id SERIAL PRIMARY KEY,
nombre VARCHAR(100),
departamento VARCHAR(100),
salario INT
);

INSERT INTO empleados VALUES
(1,'Ana','TI',1200),
(2,'Luis','Finanzas',1500),
(3,'Carlos','Marketing',1100),
(4,'Maria','TI',1400);

