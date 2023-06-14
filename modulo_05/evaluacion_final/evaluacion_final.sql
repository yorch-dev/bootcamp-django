-- Consultas para insertar, modificar y eliminar un Customer, Staff y Actor

-- Insertar Customer
-- INSERT INTO public.customer(
-- 	customer_id, store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active)
-- 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

-- Insertar Staff
-- INSERT INTO public.staff(
-- 	staff_id, first_name, last_name, address_id, email, store_id, active, username, password, last_update, picture)
-- 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

-- Insertar Actor
-- INSERT INTO public.actor(
-- 	actor_id, first_name, last_name, last_update)
-- 	VALUES (?, ?, ?, ?);

-- Modificar Customer
-- UPDATE public.customer
-- 	SET customer_id=?, store_id=?, first_name=?, last_name=?, email=?, address_id=?, activebool=?, create_date=?, last_update=?, active=?
-- 	WHERE <condition>;

-- Modificar Staff
-- UPDATE public.staff
-- 	SET staff_id=?, first_name=?, last_name=?, address_id=?, email=?, store_id=?, active=?, username=?, password=?, last_update=?, picture=?
-- 	WHERE <condition>;

-- Modificar Actor
-- UPDATE public.actor
-- 	SET actor_id=?, first_name=?, last_name=?, last_update=?
-- 	WHERE <condition>;

-- Eliminar Customer
-- DELETE FROM public.customer
-- 	WHERE <condition>;

-- Eliminar Staff
-- DELETE FROM public.staff
-- 	WHERE <condition>;

-- Eliminar Actor
-- DELETE FROM public.actor
-- 	WHERE <condition>;


-- Listar todas las “rental” con los datos del “customer” dado un año y mes.
-- SELECT * FROM RENTAL R
-- INNER JOIN CUSTOMER C ON C.CUSTOMER_ID = R.CUSTOMER_ID
-- WHERE TO_CHAR(RENTAL_DATE, 'YYYY-MM') = '2005-08'


-- Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”.
-- SELECT PAYMENT_ID "Número", DATE(PAYMENT_DATE) "Fecha", AMOUNT "Total" FROM payment


-- Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0
-- SELECT * FROM FILM
-- WHERE RELEASE_YEAR = 2006 AND RENTAL_RATE > 4


-- Realiza un Diccionario de datos que contenga el nombre de las tablas y columnas, si estas pueden ser nulas, y su tipo de dato correspondiente
-- SELECT
-- 	t1.TABLE_NAME AS tabla_nombre,
-- 	t1.COLUMN_NAME AS columna_nombre,
-- 	t1.IS_NULLABLE AS columna_nulo,
-- 	t1.DATA_TYPE AS columna_tipo_dato
-- FROM
-- 	INFORMATION_SCHEMA.COLUMNS t1
-- INNER JOIN PG_CLASS t2 ON (t2.RELNAME = t1.TABLE_NAME)
-- WHERE
-- 	t1.TABLE_SCHEMA = 'public'
-- ORDER BY
-- 	t1.TABLE_NAME;
