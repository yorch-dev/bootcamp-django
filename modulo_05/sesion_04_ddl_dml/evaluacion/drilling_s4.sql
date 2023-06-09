-- Insertar datos de una empresa
-- INSERT INTO public."Empresa"(
-- 	rut, nombre, direccion, telefono, correo, web)
-- 	VALUES ('12345678-9', 'Empresa uno', 'Direccion 1', '987654321', 'empresa@correo.com', 'www.empresa.cl');

--Insertar 5 herramientas
-- INSERT INTO public."Herramienta"(
-- 	id_herramienta, nombre, precio_dia)
-- 	VALUES (1, 'Herramienta 1', 10000),
-- 	(2, 'Herramienta 2', 12000),
-- 	(3, 'Herramienta 3', 14000),
-- 	(4, 'Herramienta 4', 16000),
-- 	(5, 'Herramienta 5', 18000)
-- ;

-- Insertar 3 clientes
-- INSERT INTO public."Cliente"(
-- 	rut, nombre, correo, direccion, celular)
-- 	VALUES ('14712315-9', 'cliente 1', 'cliente1@mail.com', 'direccion 1', '987654321'),
-- 	('13254678-9', 'cliente 2', 'cliente2@mail.com', 'direccion 2', '963852741'),
-- 	('14569873-9', 'cliente 3', 'cliente3@mail.com', 'direccion 3', '789456123')
-- ;

-- Eliminar último cliente
-- DELETE FROM public."Cliente"
-- 	WHERE rut = '14569873-9';

-- Eliminar la primera herramienta
-- DELETE FROM public."Herramienta"
-- 	WHERE id_herramienta = 1;

-- Insertar 2 arriendos por cada cliente
-- INSERT INTO public."Arriendo"(
-- 	folio, fecha, dias, valor_dia, garantia, herramienta_id_herramienta, cliente_rut)
-- 	VALUES (1, '2022-06-08', 5, 10000, 'garantía acá', 2, '13254678-9'),
-- 	(2, '2022-06-08', 6, 12000, 'garantía acá', 3, '13254678-9'),
-- 	(3, '2022-06-08', 7, 14000, 'garantía acá', 4, '14712315-9'),
-- 	(4, '2022-06-08', 8, 16000, 'garantía acá', 5, '14712315-9')
-- ;

-- Modificar correo del primer cliente
-- UPDATE public."Cliente"
-- 	SET correo = 'cliente_uno@mail.com'
-- 	WHERE rut = '14712315-9';

-- Listar todas las herramientas
-- select * from "Herramienta"

-- Listar arriendos del segundo cliente
-- SELECT * FROM "Arriendo"
-- 	WHERE cliente_rut = '13254678-9'

-- Listar clientes cuyo nombre contenga una a
-- SELECT * from "Cliente"
-- 	WHERE nombre LIKE '%a%'

-- Obtener nombre de segunda herramienta insertada
-- SELECT nombre FROM "Herramienta"
-- 	WHERE id_herramienta = 2

-- Modificar fecha de los 2 primeros arriendos ('2020-01-15')
-- UPDATE public."Arriendo"
-- 	SET fecha = '2020-01-15'
-- 	WHERE folio in (1, 2);

-- Listar folio, fecha y valor_dia de arriendos del '2020'
-- SELECT folio as "Folio", fecha as "Fecha", valor_dia as "Valor día" FROM "Arriendo"
-- 	WHERE extract(year from fecha) = 2020 and extract(month from fecha) = 1
