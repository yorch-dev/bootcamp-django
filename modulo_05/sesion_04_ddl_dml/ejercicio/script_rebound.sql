-- Crear empresa
-- INSERT INTO public."Empresa"(
-- 	rut, nombre, direccion, telefono, correo, web)
-- 	VALUES ('12345678-9',
-- 			'Empresa de prueba',
-- 			'La dirección de la empresa',
-- 			'987654321',
-- 			'empresa@correo.com',
-- 		   	'www.empresa.com'
-- );

-- Insertar 2 tipos de vehiculos
-- INSERT INTO public."TipoVehiculo"(
-- 	id_tipo_vehiculo, nombre)
-- 	VALUES (1, 'Tipo uno'),
-- 	(2, 'Tipo dos')
-- ;

-- Insertar 3 clientes
-- INSERT INTO public."Cliente"(
-- 	rut, nombre, correo, direccion, celular, alta)
-- 	VALUES ('13456789-2', 'cliente uno', 'cliente.uno@mail.com', 'direccion cliente 1', '789456123', 'y'),
-- 	('14725836-9', 'cliente dos', 'cliente.dos@mail.com', 'direccion cliente 2', '741852963', 'y'),
-- 	('9876543-2', 'cliente tres', 'cliente.tres@mail.com', 'direccion cliente 3', '963852741', 'y')
-- ;

-- Insertar 2 marcas
-- INSERT INTO public."Marca"(
-- 	id_marca, nombre)
-- 	VALUES (1, 'marca uno'),
-- 	(2, 'marca dos')
-- ;

-- Insertar 5 vehículos
-- INSERT INTO public."Vehiculo"(
-- 	id_vehiculo, patente, marca, modelo, color, precio, frecuencia_mantencion, marca_id_marca, tipo_vehiculo_id_tipo_vehiculo)
-- 	VALUES (1, 'uno', 'marca uno', 'modelo 1', 'verde', 10000, 90, 1, 1),
-- 	(2, 'dos', 'marca uno', 'modelo 2', 'rojo', 12000, 60, 1, 2),
-- 	(3, 'tres', 'marca dos', 'modelo 3', 'azul', 14000, 180, 2, 1),
-- 	(4, 'cuatro', 'marca uno', 'modelo 4', 'café', 16000, 90, 1, 1),
-- 	(5, 'cinco', 'marca dos', 'modelo 5', 'amarillo', 18000, 120, 2, 2)
-- ;

-- Eliminar último cliente
-- DELETE FROM public."Cliente"
-- 	WHERE rut = '9876543-2';

-- Insertar una venta por cliente
-- INSERT INTO public."Venta"(
-- 	folio, fecha, monto, vehiculo_id_vehiculo, cliente_rut)
-- 	VALUES (1, '2022-06-06', 14000, 3, '13456789-2'),
-- 	(2, '2022-06-03', 18000, 5, '14725836-9')
-- ;

-- Modificar nombre del segundo cliente
-- UPDATE public."Cliente"
-- 	SET nombre='Cliente modificado dos'
-- 	WHERE rut = '14725836-9';

-- Listar todas las ventas
-- SELECT * FROM "Venta"

-- Listar ventas del primer cliente
-- SELECT * FROM "Venta" WHERE cliente_rut = '13456789-2'

-- Obtener patentes de todos los vehículos
-- SELECT patente FROM "Vehiculo"