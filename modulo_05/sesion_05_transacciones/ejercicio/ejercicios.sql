-- 1. Crear tabla “editoriales”, con los atributos código y nombre. Definir el código como llave primaria.
-- CREATE TABLE IF NOT EXISTS public.editoriales
-- (
--     codigo serial NOT NULL,
--     nombre character varying(50),
--     CONSTRAINT editoriales_pkey PRIMARY KEY (codigo)
-- );

-- 2. Crear tabla “libros”, con los atributos código, título, y codigoeditorial. Definir el código como llave primaria, y codigoeditorial como llave foránea, referenciando a la tabla editoriales
-- CREATE TABLE IF NOT EXISTS public.libros
-- (
--     codigo serial NOT NULL,
--     titulo character varying(50),
--     codigoeditorial integer NOT NULL,
--     CONSTRAINT libros_pkey PRIMARY KEY (codigo),
-- 	CONSTRAINT libros_editoriales_fk FOREIGN KEY (codigoeditorial)
-- 		REFERENCES public.editoriales (codigo)
-- );

-- 3 Insertando editoriales y libros

-- INSERT INTO public.editoriales(
-- 	nombre)
-- 	VALUES ('Anaya'),
-- 	('Andina'),
-- 	('S.M.')
-- ;

-- INSERT INTO public.libros(
-- 	titulo, codigoeditorial)
-- 	VALUES ('Don Quijote de la Mancha I', 1),
-- 	('El principito', 2),
-- 	('El príncipe', 3),
-- 	('Diplomacia', 3),
-- 	('Don Quijote de la Mancha II', 1)
-- ;

-- 4. Modificar la tabla “libros”, agregando la columna autor y precio.
-- ALTER TABLE IF EXISTS public.libros
--     ADD COLUMN autor character varying(50);
-- ALTER TABLE IF EXISTS public.libros
--     ADD COLUMN precio numeric(5);

-- 5. Agregar autor y precio a los libros ya ingresados.
-- UPDATE public.libros
-- 	SET autor = 'Miguel de Cervantes', precio = 150
-- 	WHERE codigo = 1;
-- UPDATE public.libros
-- 	SET autor = 'Antoine SaintExupery', precio = 120
-- 	WHERE codigo = 2;
-- UPDATE public.libros
-- 	SET autor = 'Maquiavelo', precio = 180
-- 	WHERE codigo = 3;
-- UPDATE public.libros
-- 	SET autor = 'Henry Kissinger', precio = 170
-- 	WHERE codigo = 4;
-- UPDATE public.libros
-- 	SET autor = 'Miguel de Cervantes', precio = 140
-- 	WHERE codigo = 5;
	
-- 6. Insertar 2 nuevos libros.
-- INSERT INTO public.editoriales(
-- 	nombre)
-- 	VALUES ('Edhasa'),
-- 	('Marcombo')
-- ;
-- INSERT INTO public.libros(
-- 	titulo, codigoeditorial, autor, precio)
-- 	VALUES ('Yo, Robot', 4, 'Isaac Asimov', 10720),
-- 	('Python Deep Learning', 5, 'Jordi Torres', 24080)
-- ;

-- 7. Eliminar los libros de la editorial Anaya, solo en memoria (ROLLBACK).
-- BEGIN;
-- DELETE FROM public.libros WHERE codigoeditorial = 1;
-- ROLLBACK;

-- otra opción
-- BEGIN;
-- 	DELETE FROM public.libros WHERE codigoeditorial in (SELECT codigo FROM public.editoriales
-- 	WHERE nombre = 'Anaya');
-- ROLLBACK;

-- 8. Actualizar el nombre de la editorial Andina a Iberlibro en memoria, y actualizar el nombre de la editorial S.M. a Mountain en disco duro (SAVEPOINT / ROLLBACK TO)
-- BEGIN;
-- 	UPDATE public.editoriales
-- 		SET nombre = 'Iberlibro'
-- 		WHERE nombre = 'Andina';
-- SAVEPOINT sp_actualizar;
-- 	UPDATE public.editoriales
-- 		SET nombre = 'Mountain'
-- 		WHERE nombre = 'S.M.';
-- ROLLBACK TO sp_actualizar;
-- COMMIT;
