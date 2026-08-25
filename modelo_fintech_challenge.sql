/*******************************************************************************
 PROYECTO: Challenge Data Analyst — Fintech Préstamos
 ANALISTA: Jazmín Guazzora
 DESCRIPCIÓN: Construcción del modelo dimensional curado
*******************************************************************************/

-- Crear e inicializar base de datos
CREATE DATABASE IF NOT EXISTS fintech_challenge;
USE fintech_challenge;

-- =====================================================
-- 0. LIMPIEZA DE TABLAS FINALES
-- Se eliminan en orden inverso a sus dependencias.
-- Las tablas staging NO se eliminan.
-- =====================================================

DROP TABLE IF EXISTS fact_prestamos;
DROP TABLE IF EXISTS cliente_sucursal;
DROP TABLE IF EXISTS dim_variables_crediticias;
DROP TABLE IF EXISTS dim_geografia;
DROP TABLE IF EXISTS dim_cliente;

SHOW TABLES;

-- =====================================================
-- 1. DIMENSIÓN CLIENTE
-- Granularidad: una fila por cliente
-- Universo: clientes presentes en al menos una fuente
-- descriptiva (offline, online, laboral o demográfica)
-- =====================================================

CREATE TABLE dim_cliente (
    id_cliente INT NOT NULL,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE,
    fecha_alta DATE,
    segmento VARCHAR(20),
    canal_adquisicion VARCHAR(20),
    origen VARCHAR(30),

    PRIMARY KEY (id_cliente)
);

INSERT INTO dim_cliente (
    id_cliente,
    nombre,
    apellido,
    fecha_nacimiento,
    fecha_alta,
    segmento,
    canal_adquisicion,
    origen
)

WITH universo_clientes AS (

    SELECT id_cliente
    FROM stg_clientes_offline

    UNION

    SELECT customer_id AS id_cliente
    FROM stg_clientes_online

    UNION

    SELECT id_cliente
    FROM stg_variables_laboral

    UNION

    SELECT id_cliente
    FROM stg_variables_demografica
),

offline_unico AS (

    SELECT
        id_cliente,
        MAX(nombre) AS nombre,
        MAX(apellido) AS apellido,
        MAX(fecha_nacimiento) AS fecha_nacimiento,
        MAX(fecha_alta) AS fecha_alta,
        MAX(segmento) AS segmento
    FROM stg_clientes_offline
    GROUP BY id_cliente
),

online_unico AS (

    SELECT
        customer_id,
        MAX(first_name) AS first_name,
        MAX(last_name) AS last_name,
        MAX(birth_date) AS birth_date,
        MAX(signup_date) AS signup_date,
        MAX(segment) AS segment,
        MAX(acquisition_channel) AS acquisition_channel
    FROM stg_clientes_online
    GROUP BY customer_id
)

SELECT
    u.id_cliente,
    COALESCE(o.nombre, n.first_name) AS nombre,
    COALESCE(o.apellido, n.last_name) AS apellido,
    COALESCE(o.fecha_nacimiento, n.birth_date) AS fecha_nacimiento,
    COALESCE(o.fecha_alta, n.signup_date) AS fecha_alta,
    COALESCE(o.segmento, n.segment) AS segmento,
    n.acquisition_channel AS canal_adquisicion,

    CASE
        WHEN o.id_cliente IS NOT NULL
             AND n.customer_id IS NOT NULL
            THEN 'ambos'
        WHEN o.id_cliente IS NOT NULL
            THEN 'offline'
        WHEN n.customer_id IS NOT NULL
            THEN 'online'
        ELSE 'solo variables'
    END AS origen

FROM universo_clientes u

LEFT JOIN offline_unico o
    ON u.id_cliente = o.id_cliente

LEFT JOIN online_unico n
    ON u.id_cliente = n.customer_id;
    
SELECT
    COUNT(*) AS filas,
    COUNT(DISTINCT id_cliente) AS clientes_unicos
FROM dim_cliente;

INSERT INTO dim_cliente (
    id_cliente,
    nombre,
    apellido,
    fecha_nacimiento,
    fecha_alta,
    segmento,
    canal_adquisicion,
    origen
)
VALUES (
    -1,
    'Cliente no identificado',
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    'no identificado'
);

-- =====================================================
-- 2. TABLA PUENTE CLIENTE - SUCURSAL
-- Granularidad: una fila por combinación cliente-sucursal
-- Preserva clientes asociados a más de una sucursal
-- =====================================================

CREATE TABLE cliente_sucursal (
    id_cliente INT NOT NULL,
    sucursal VARCHAR(50) NOT NULL,

    PRIMARY KEY (id_cliente, sucursal),

    CONSTRAINT fk_cliente_sucursal_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES dim_cliente(id_cliente)
);

INSERT INTO cliente_sucursal (
    id_cliente,
    sucursal
)
SELECT DISTINCT
    o.id_cliente,
    o.sucursal
FROM stg_clientes_offline o
INNER JOIN dim_cliente c
    ON o.id_cliente = c.id_cliente
WHERE o.sucursal IS NOT NULL;

-- Total de relaciones cliente-sucursal
SELECT COUNT(*) AS relaciones_cliente_sucursal
FROM cliente_sucursal;

-- Clientes asociados a más de una sucursal
SELECT
    id_cliente,
    COUNT(*) AS cantidad_sucursales
FROM cliente_sucursal
GROUP BY id_cliente
HAVING COUNT(*) > 1
ORDER BY cantidad_sucursales DESC;

-- =====================================================
-- 3. DIMENSIÓN GEOGRAFÍA
-- Granularidad: una fila por provincia
-- =====================================================

CREATE TABLE dim_geografica (
    id_provincia INT AUTO_INCREMENT PRIMARY KEY,
    provincia VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL DEFAULT 'Argentina',

    CONSTRAINT uq_dim_geografica_provincia
        UNIQUE (provincia)
);

INSERT INTO dim_geografica (
    provincia,
    pais
)
SELECT DISTINCT
    provincia,
    'Argentina'
FROM stg_variables_demografica
WHERE provincia IS NOT NULL;

SELECT COUNT(*) AS cantidad_geo
FROM dim_geografica;

SELECT * FROM dim_geografica ORDER BY provincia;

-- =====================================================
-- 4. DIMENSIÓN VARIABLES CREDITICIAS
-- Granularidad: una fila por cliente
-- Integra variables laborales y demográficas
-- =====================================================

CREATE TABLE dim_variables_crediticias (
    id_cliente INT NOT NULL,

    ingreso_mensual DECIMAL(12,2),
    antiguedad_laboral_anios DECIMAL(5,2),
    situacion_laboral VARCHAR(30),
    atrasos_historicos_12m INT,
    ratio_endeudamiento DECIMAL(5,4),

    edad INT,
    estado_civil VARCHAR(30),
    nivel_educativo VARCHAR(30),
    cantidad_dependientes INT,

    id_provincia INT,

    PRIMARY KEY (id_cliente),

    CONSTRAINT fk_variables_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES dim_cliente(id_cliente),

    CONSTRAINT fk_variables_provincia
        FOREIGN KEY (id_provincia)
        REFERENCES dim_geografica(id_provincia)
);

INSERT INTO dim_variables_crediticias (
    id_cliente,
    ingreso_mensual,
    antiguedad_laboral_anios,
    situacion_laboral,
    atrasos_historicos_12m,
    ratio_endeudamiento,
    edad,
    estado_civil,
    nivel_educativo,
    cantidad_dependientes,
    id_provincia
)

WITH universo_variables AS (

    SELECT id_cliente
    FROM stg_variables_laboral

    UNION

    SELECT id_cliente
    FROM stg_variables_demografica
)

SELECT
    u.id_cliente,

    l.ingreso_mensual,
    l.antiguedad_laboral_anios,
    l.situacion_laboral,
    l.atrasos_historicos_12m,
    l.ratio_endeudamiento,

    d.edad,
    d.estado_civil,
    d.nivel_educativo,
    d.cantidad_dependientes,

    g.id_provincia

FROM universo_variables u

LEFT JOIN stg_variables_laboral l
    ON u.id_cliente = l.id_cliente

LEFT JOIN stg_variables_demografica d
    ON u.id_cliente = d.id_cliente

LEFT JOIN dim_geografica g
    ON d.provincia = g.provincia;
    
SELECT
    COUNT(*) AS filas,
    COUNT(DISTINCT id_cliente) AS clientes_unicos
FROM dim_variables_crediticias;

SELECT COUNT(*) AS variables_sin_cliente
FROM dim_variables_crediticias v
LEFT JOIN dim_cliente c
    ON v.id_cliente = c.id_cliente
WHERE c.id_cliente IS NULL;

SELECT
    COUNT(CASE WHEN ingreso_mensual IS NOT NULL THEN 1 END) AS con_datos_laborales,
    COUNT(CASE WHEN edad IS NOT NULL THEN 1 END) AS con_datos_demograficos,
    COUNT(CASE
        WHEN ingreso_mensual IS NOT NULL
         AND edad IS NOT NULL
        THEN 1
    END) AS con_ambas_fuentes
FROM dim_variables_crediticias;

-- =====================================================
-- 5. TABLA DE HECHOS PRÉSTAMOS
-- Granularidad: una fila por préstamo
-- =====================================================

CREATE TABLE fact_prestamos (
    id_prestamo INT NOT NULL,
    id_cliente INT NOT NULL,
    id_cliente_origen INT NOT NULL,
    fecha_otorgamiento DATE,
    monto DECIMAL(12,2),
    tasa_interes DECIMAL(6,4),
    cantidad_cuotas INT,

    PRIMARY KEY (id_prestamo),

    CONSTRAINT fk_prestamos_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES dim_cliente(id_cliente)
);

INSERT INTO fact_prestamos (
    id_prestamo,
    id_cliente,
    id_cliente_origen,
    fecha_otorgamiento,
    monto,
    tasa_interes,
    cantidad_cuotas
)

SELECT
    p.id_prestamo,

    CASE
        WHEN c.id_cliente IS NOT NULL
            THEN p.id_cliente
        ELSE -1
    END AS id_cliente,

    p.id_cliente AS id_cliente_origen,

    p.fecha_otorgamiento,
    p.monto,
    p.tasa_interes,
    p.cantidad_cuotas

FROM stg_prestamos p

LEFT JOIN dim_cliente c
    ON p.id_cliente = c.id_cliente;
    
SELECT
    COUNT(*) AS prestamos,
    COUNT(DISTINCT id_prestamo) AS prestamos_unicos
FROM fact_prestamos;

SELECT COUNT(*) AS prestamos_cliente_no_identificado
FROM fact_prestamos
WHERE id_cliente = -1;

SELECT
    COUNT(*) AS prestamos_no_identificados,
    COUNT(DISTINCT id_cliente_origen) AS ids_originales,
    SUM(monto) AS monto_total
FROM fact_prestamos
WHERE id_cliente = -1;

-- =====================================================
-- 6. VALIDACIONES FINALES DEL MODELO
-- =====================================================

-- dim_cliente
SELECT 
    COUNT(*) AS filas,
    COUNT(DISTINCT id_cliente) AS ids_unicos
FROM dim_cliente;

-- dim_variables_crediticias
SELECT 
    COUNT(*) AS filas,
    COUNT(DISTINCT id_cliente) AS ids_unicos
FROM dim_variables_crediticias;

-- fact_prestamos
SELECT 
    COUNT(*) AS filas,
    COUNT(DISTINCT id_prestamo) AS ids_unicos
FROM fact_prestamos;

-- Préstamos sin correspondencia en dim_cliente
SELECT COUNT(*) AS prestamos_sin_cliente
FROM fact_prestamos f
LEFT JOIN dim_cliente c
    ON f.id_cliente = c.id_cliente
WHERE c.id_cliente IS NULL;

-- Variables crediticias sin cliente
SELECT COUNT(*) AS variables_sin_cliente
FROM dim_variables_crediticias v
LEFT JOIN dim_cliente c
    ON v.id_cliente = c.id_cliente
WHERE c.id_cliente IS NULL;

-- Provincias sin correspondencia
SELECT COUNT(*) AS variables_sin_provincia_valida
FROM dim_variables_crediticias v
LEFT JOIN dim_geografica g
    ON v.id_provincia = g.id_provincia
WHERE v.id_provincia IS NOT NULL
  AND g.id_provincia IS NULL;
  
-- huerfanos
SELECT
    COUNT(*) AS prestamos_no_identificados,
    COUNT(DISTINCT id_cliente_origen) AS ids_originales,
    ROUND(SUM(monto), 2) AS monto_total
FROM fact_prestamos
WHERE id_cliente = -1;

-- prestamos
SELECT
    (SELECT COUNT(*) FROM stg_prestamos) AS staging,
    (SELECT COUNT(*) FROM fact_prestamos) AS modelo_final;
    
-- monto total
SELECT
    ROUND((SELECT SUM(monto) FROM stg_prestamos), 2) AS monto_staging,
    ROUND((SELECT SUM(monto) FROM fact_prestamos), 2) AS monto_modelo;

-- cobertura de variables
SELECT
    COUNT(*) AS total_clientes_reales,
    SUM(CASE WHEN v.id_cliente IS NOT NULL THEN 1 ELSE 0 END) AS con_variables,
    SUM(CASE WHEN v.id_cliente IS NULL THEN 1 ELSE 0 END) AS sin_variables,
    ROUND(
        100.0 * SUM(CASE WHEN v.id_cliente IS NOT NULL THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS pct_cobertura
FROM dim_cliente c
LEFT JOIN dim_variables_crediticias v
    ON c.id_cliente = v.id_cliente
WHERE c.id_cliente <> -1;