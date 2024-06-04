-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-06-2024 a las 19:59:43
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `reinvent_reinventar`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `donacion`
--

CREATE TABLE `donacion` (
  `id_donacion` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `donacion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripto`
--

CREATE TABLE `inscripto` (
  `id_inscripto` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fecha_inscripcion` date NOT NULL,
  `estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inscripto`
--

INSERT INTO `inscripto` (`id_inscripto`, `nombre`, `apellido`, `telefono`, `email`, `fecha_inscripcion`, `estado`) VALUES
(1, 'Sol Agostina', 'Spinelli', 2262652554, 'solagostinaspinelli@gmail.com	', '2024-05-09', 'caminante'),
(2, 'Pia Maria', 'Bedini Crocci', 2262652554, 'piabedinicrocci@gmail.com	', '2024-05-09', 'Corredor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `necesidad`
--

CREATE TABLE `necesidad` (
  `id_necesidad` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `necesidad` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticia`
--

CREATE TABLE `noticia` (
  `id_noticia` int(11) NOT NULL,
  `titulo` varchar(300) NOT NULL,
  `epigrafe` varchar(300) NOT NULL,
  `imagen` varchar(2083) NOT NULL,
  `cuerpo` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `noticia`
--

INSERT INTO `noticia` (`id_noticia`, `titulo`, `epigrafe`, `imagen`, `cuerpo`) VALUES
(1, 'Reinventar, una ONG que ilumina el camino de los más vulnerables en Tandil', 'La ONG de Tandil Reinventar ejerce un rol social preponderante en la ciudad: a través del deporte inculca valores a los más chicos para formar jóvenes líderes positivos. Su fundadora, Catalina Granel, recibió a Rugido Sagrado para conocer en profundidad el trabajo que realizan', 'https://rugidosagrado.com/uploads/noticias/5/2022/10/20221005104039_img-20221002-wa0084.jpg', 'El barrio Las Tunitas es uno de los lugares más vulnerables de Tandil, con personas en situación de calle y con otras tantas que son protagonistas de hechos vandálicos de forma recurrente. Hace 17 años, en ese mismo lugar, comenzaba un sueño para un grupo de profesionales, que buscaba contener, de alguna manera, a los adolescentes y niños de ahí a través del deporte, y una ONG, denominada “Reinventar”, surge para dicho fin.\n\nCatalina Granel es la fundadora de la ONG y recibió a Rugido Sagrado para dar a conocer esta nueva aventura en su vida laboral y personal: “Educamos a través del deporte para formar jóvenes lideres positivos, y el hockey es nuestro puente para transformar una vida. La idea surge en 2005 de forma extraoficial y la fuimos llevando adelante como podíamos, sin personería jurídica; ya en 2008 la pudimos tener. El municipio siempre nos acompañó desde nuestros comienzos”.La profesora de educación física cuenta los detalles del origen de “Reinventar”: “Un sacerdote, que fue mi guia, me ayudó a hacer la ONG; siempre me empujaba a descubrir el talento en las personas y desarrollarlo de alguna forma. Al principio, queríamos hacer un centro de referencia, pero todo se volcó para otro lado. Mi talento era enseñar hockey, así que comencé de esa forma, y con los años fuimos construyendo un lugar que es fundamental a nivel social”.\n\nEl lugar, ubicado en las calles Ezeiza y Velez Sarsfield, posee una imponente cancha de hockey, y no existe un día que no esté repleta de chicos y chicas quienes, justamente, integran o integrarán en un futuro el equipo “Las Pumas”. “Entre otras actividades, el hockey es nuestro deporte insignia. Actualmente tenemos entre 50 y 60 jóvenes, desde los 5 hasta los 18 años, que se divierten en los entrenamientos y partidos que organizamos con clubes de Tandil y ciudades aledañas”, contó la dirigente, que supo tener al rugby como disciplina en sus instalaciones.'),
(2, 'REINVENTAR concreta una gran obra\r\n', 'Con la colaboración de la comunidad tandilense, la cancha de Las Pumas luce transformada.', 'https://cdn.eleco.com.ar/media/2022/05/reinventar_tandil_3.JPG', 'Fue un día de celebración para la comunidad de Las Tunitas. Reinventar Tandil es uno de sus espacios de referencia e identidad, donde además de jugar al hockey aprenden de valores y educación. Tras un enorme esfuerzo mancomunado finalizaron los muros y cerramientos de la cancha y lo festejaron. Tras el corte de cinta Miguel Lunghi les donó 200 mi pesos para que completen las luminarias faltantes.\n\nAds\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFue un día de celebración para la comunidad de Las Tunitas. Reinventar Tandil es uno de sus espacios de referencia e identidad, donde además de jugar al hockey aprenden de valores y educación. Tras un enorme esfuerzo mancomunado finalizaron los muros y cerramientos de la cancha y lo festejaron. Tras el corte de cinta Miguel Lunghi les donó 200 mi pesos para que completen las luminarias faltantes.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `user` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `user`, `password`) VALUES
(1, 'admin', 'admin');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `donacion`
--
ALTER TABLE `donacion`
  ADD PRIMARY KEY (`id_donacion`);

--
-- Indices de la tabla `inscripto`
--
ALTER TABLE `inscripto`
  ADD PRIMARY KEY (`id_inscripto`);

--
-- Indices de la tabla `necesidad`
--
ALTER TABLE `necesidad`
  ADD PRIMARY KEY (`id_necesidad`);

--
-- Indices de la tabla `noticia`
--
ALTER TABLE `noticia`
  ADD PRIMARY KEY (`id_noticia`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `donacion`
--
ALTER TABLE `donacion`
  MODIFY `id_donacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inscripto`
--
ALTER TABLE `inscripto`
  MODIFY `id_inscripto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `necesidad`
--
ALTER TABLE `necesidad`
  MODIFY `id_necesidad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `noticia`
--
ALTER TABLE `noticia`
  MODIFY `id_noticia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
