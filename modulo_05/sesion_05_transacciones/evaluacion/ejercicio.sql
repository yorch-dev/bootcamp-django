-- 2. crear tablas
-- create table public.pelicula(
-- 	id serial not null,
-- 	pelicula character varying(80),
-- 	estreno numeric(4),
-- 	director character varying(50),
-- 	CONSTRAINT pelicula_pk PRIMARY KEY(id)
-- );

-- create table public.reparto(
-- 	id_pelicula serial not null,
-- 	actor character varying(50),
-- 	CONSTRAINT reparto_pelicula_fk FOREIGN KEY (id_pelicula)
-- 		REFERENCES public.pelicula(id)
-- );


-- 3. cargar archivos
-- COPY public.pelicula
-- FROM 'C:/archivos_drilling_s5/peliculas.csv'
-- WITH CSV
-- DELIMITER ',';

-- COPY public.reparto
-- FROM 'C:/archivos_drilling_s5/reparto.csv'
-- WITH CSV
-- DELIMITER ',';


-- 7. Listar todos los actores que aparecen en la película "Titanic", indicando el título de la película, año de estreno, director y todo el reparto.
-- SELECT pelicula, estreno, director, actor FROM REPARTO R
-- JOIN PELICULA P ON P.ID = R.ID_PELICULA
-- WHERE PELICULA = 'Titanic'


-- 8. Listar los 10 directores más populares, indicando su nombre y cuántas películas aparecen en el top 100.
-- select director "Director", COUNT(*) as "Número películas" from pelicula
-- GROUP BY "Director"
-- ORDER BY "Número películas" DESC
-- LIMIT 10


-- 9. Indicar cuántos actores distintos hay.
--SELECT COUNT(DISTINCT(ACTOR)) "ACTORES DISTINTOS" FROM REPARTO


-- 10. Indicar las películas estrenadas entre los años 1990 y 1999 (ambos incluidos), ordenadas por título de manera ascendente.
-- SELECT PELICULA, ESTRENO FROM PELICULA
-- WHERE ESTRENO BETWEEN 1990 AND 1999
-- ORDER BY ESTRENO


-- 11. Listar los actores de la película más nueva.
-- SELECT ACTOR, PELICULA, ESTRENO FROM REPARTO R
-- JOIN PELICULA C ON R.ID_PELICULA = C.ID
-- WHERE ESTRENO IN (SELECT MAX(ESTRENO) FROM PELICULA)
-- ORDER BY PELICULA ASC, ACTOR ASC


-- 12. Inserte los datos de una nueva película solo en memoria, y otra película en el disco duro.
-- BEGIN;
-- INSERT INTO public.pelicula(
-- 	id, pelicula, estreno, director)
-- 	VALUES (
-- 		((SELECT MAX(ID) FROM PELICULA) + 1),
-- 		'Película para rollback', 2020, 'Director rollback');
-- ROLLBACK;
-- INSERT INTO public.pelicula(
-- 	id, pelicula, estreno, director)
-- 	VALUES (
-- 		((SELECT MAX(ID) FROM PELICULA) + 1),
-- 		'Una nueva película', 2020, 'Nuevo director');
-- END;


-- 13. Actualice 5 directores utilizando ROLLBACK.
-- BEGIN;
-- UPDATE public.pelicula
-- 	SET director='OTRO DIRECTOR 1'
-- 	WHERE ID = 1;
-- UPDATE public.pelicula
-- 	SET director='OTRO DIRECTOR 2'
-- 	WHERE ID = 2;
-- UPDATE public.pelicula
-- 	SET director='OTRO DIRECTOR 3'
-- 	WHERE ID = 3;
-- UPDATE public.pelicula
-- 	SET director='OTRO DIRECTOR 4'
-- 	WHERE ID = 4;
-- UPDATE public.pelicula
-- 	SET director='OTRO DIRECTOR 5'
-- 	WHERE ID = 5;
-- ROLLBACK;


-- 14. Inserte 3 actores a la película “Rambo” utilizando SAVEPOINT
-- BEGIN;
-- SAVEPOINT sp;
-- INSERT INTO public.reparto(
-- 	id_pelicula, actor)
-- 	VALUES (
-- 		(SELECT ID FROM PELICULA
-- 			WHERE ID IN (SELECT ID_PELICULA FROM REPARTO WHERE PELICULA = 'Rambo')),
-- 		'Nuevo actor 1'),
-- 		((SELECT ID FROM PELICULA
-- 			WHERE ID IN (SELECT ID_PELICULA FROM REPARTO WHERE PELICULA = 'Rambo')),
-- 		'Nuevo actor 2'),
-- 		((SELECT ID FROM PELICULA
-- 			WHERE ID IN (SELECT ID_PELICULA FROM REPARTO WHERE PELICULA = 'Rambo')),
-- 		'Nuevo actor 3');
-- ROLLBACK TO sp;
-- END;


-- 15. Elimina las películas estrenadas el año 2008 solo en memoria.
-- ALTER TABLE reparto
-- DROP CONSTRAINT reparto_pelicula_fk;

-- ALTER TABLE reparto
-- ADD CONSTRAINT reparto_pelicula_fk
-- FOREIGN KEY (id_pelicula)
-- REFERENCES pelicula (id)
-- ON DELETE CASCADE;

-- BEGIN;
-- DELETE FROM public.pelicula
-- WHERE ESTRENO = 2008;
-- ROLLBACK;


-- 16. Inserte 2 actores para cada película estrenada el 2001.
-- DO $$
-- DECLARE
--     i INTEGER;
-- 	contador INTEGER := 0;
-- 	pelicula_id INTEGER;
-- BEGIN
-- 	SELECT COUNT(*) INTO i FROM pelicula WHERE ESTRENO = 2001;
--     LOOP
-- 		SELECT Id INTO pelicula_id FROM pelicula WHERE ESTRENO = 2001 ORDER BY id ASC OFFSET contador LIMIT 1;
-- 		INSERT INTO public.reparto(
-- 			id_pelicula, actor)
-- 			VALUES (pelicula_id, 'nuevo actor 1'),
-- 			(pelicula_id, 'nuevo actor 2');
--         i := i - 1;
-- 		contador := contador +1;
        
--         EXIT WHEN i = 0;
--     END LOOP;
-- END $$;


-- 17. Actualice la película “King Kong” por el nombre de “Donkey Kong”, sin efectuar cambios en disco duro

-- BEGIN;
-- UPDATE PUBLIC.PELICULA
-- SET PELICULA = 'Donkey Kong'
-- WHERE PELICULA = 'King Kongg';
-- ROLLBACK;
