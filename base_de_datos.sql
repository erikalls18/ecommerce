-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2021 a las 21:24:01
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ecommerce`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `categoria_id` varchar(12) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`categoria_id`, `nombre`) VALUES
('De05', 'Deportes'),
('El01', 'Electrodomesticos'),
('HM04', 'Hogar y muebles'),
('Md03', 'Moda'),
('Tec02', 'Tecnologia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudad`
--

CREATE TABLE `ciudad` (
  `ciudad_id` varchar(4) NOT NULL,
  `nombre` varchar(120) DEFAULT NULL,
  `id_provincia` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ciudad`
--

INSERT INTO `ciudad` (`ciudad_id`, `nombre`, `id_provincia`) VALUES
('1', 'CABA', '1'),
('11', ' Múnich', '220'),
('12', 'Carmelo', '75'),
('15', 'Montevideo', '77'),
('2', 'Rosario', '5'),
('25', 'Potsdam', '125'),
('3', 'Santa Rosa', '8'),
('71', 'Barcelona', '96'),
('9', 'La Plata', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `cod_compras` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `nombre_user` varchar(120) NOT NULL,
  `email_user` varchar(100) NOT NULL,
  `id_producto` int(12) NOT NULL,
  `nombre_producto` varchar(20) NOT NULL,
  `precio` double NOT NULL,
  `total_compra` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `compras`
--

INSERT INTO `compras` (`cod_compras`, `id_user`, `nombre_user`, `email_user`, `id_producto`, `nombre_producto`, `precio`, `total_compra`) VALUES
(3, 51, 'Alan Jimenez', 'alan145@mail.com', 450, 'Zapatillas', 22000, 0),
(4, 52, 'Samantha Torres', 'samth32@hotmail.com', 323, 'Pantalon', 4000, 0),
(5, 52, 'Samantha Torres', 'samth32@hotmail.com', 320, 'Camisa', 5000, 0),
(9, 51, 'Alan Jimenez', 'alan145@mail.com', 451, 'Remera', 4000, 0),
(10, 51, 'Alan Jimenez', 'alan145@mail.com', 450, 'Zapatillas', 22000, 0),
(11, 51, 'Alan Jimenez', 'alan145@mail.com', 170, 'Alfombra', 1500, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ecommerce`
--

CREATE TABLE `ecommerce` (
  `id_user` int(11) DEFAULT NULL,
  `id_producto` varchar(12) DEFAULT NULL,
  `total_compras` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marca`
--

CREATE TABLE `marca` (
  `id_marca` varchar(12) NOT NULL,
  `nombre` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `marca`
--

INSERT INTO `marca` (`id_marca`, `nombre`) VALUES
('Ap', 'Apple'),
('GP', 'Gap'),
('LG01', 'LG'),
('NK', 'Nike'),
('Sg022', 'Samgsung');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pais`
--

CREATE TABLE `pais` (
  `pais_id` varchar(4) NOT NULL,
  `nombre` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pais`
--

INSERT INTO `pais` (`pais_id`, `nombre`) VALUES
('34', 'España'),
('49', 'Alemania'),
('54', 'Argentina'),
('598', 'Uruguay');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `codigo` varchar(12) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `modelo` varchar(12) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `id_marca` varchar(12) DEFAULT NULL,
  `id_categoria` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`codigo`, `nombre`, `modelo`, `precio`, `id_marca`, `id_categoria`) VALUES
('021', 'lavadora', 'lvg21', 15000, 'Sg022', 'El01'),
('024', 'secadora', 'sc21', 12000, 'LG01', 'El01'),
('025', 'Cafetera', 'CF36', 5000, 'LG01', 'El01'),
('034', 'Celular', 'Sjprime', 20000, 'Sg022', 'Tec02'),
('035', 'Ipad', '8TH Gem', 100000, 'Ap', 'Tec02'),
('036', 'Laptop', 'MacBook Air', 150000, 'Ap', 'Tec02'),
('170', 'Alfombra', 'Multicolor', 1500, 'GP', 'HM04'),
('171', 'Indumentaria escolar', 'urb', 2000, 'GP', 'Md03'),
('320', 'Camisa', 'primaver', 5000, 'NK', 'Md03'),
('322', 'Campera', 'Inv12', 7000, 'GP', 'Md03'),
('323', 'Pantalon', 'Inv58', 4000, 'GP', 'Md03'),
('450', 'Zapatillas', 'NKaereo', 22000, 'NK', 'De05'),
('451', 'Remera', 'Deportiva', 4000, 'NK', 'De05'),
('452', 'Calza', 'DE25', 4500, 'NK', 'De05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provincia`
--

CREATE TABLE `provincia` (
  `provincia_id` varchar(4) NOT NULL,
  `nombre` varchar(120) DEFAULT NULL,
  `id_pais` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `provincia`
--

INSERT INTO `provincia` (`provincia_id`, `nombre`, `id_pais`) VALUES
('1', 'Buenos Aires', '54'),
('125', 'Brandeburgo', '49'),
('220', 'Baviera', '49'),
('5', 'Santa Fé', '54'),
('75', 'Colonia', '598'),
('77', 'Montevideo', '598'),
('8', 'La Pampa', '54'),
('96', 'Cataluña', '34');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `user_Id` int(11) NOT NULL,
  `nombre` varchar(120) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `contrasenia` varchar(120) DEFAULT NULL,
  `id_ciudad` varchar(4) NOT NULL,
  `id_provincia` varchar(4) NOT NULL,
  `id_pais` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`user_Id`, `nombre`, `email`, `contrasenia`, `id_ciudad`, `id_provincia`, `id_pais`) VALUES
(33, 'Pablo Jimenez', 'pablito66@gmail.com', 'UGFibG90ZS00', '3', '8', '54'),
(37, 'Zeldita Vila', 'zeldita666@gmail.com', 'WmVsZGl0YS02', '71', '96', '34'),
(48, 'Daniela  Gomez', 'dani14@gmail.com', 'RGFuaTEyMyE=\n', '11', '220', '49'),
(51, 'Alan Jimenez', 'alan145@mail.com', 'QWxhbjEyMyE=', '25', '125', '49'),
(52, 'Samantha Torres', 'samth32@hotmail.com', 'U2FtdGgxMjMh', '15', '77', '598'),
(54, 'Samanta Gomez', 'sam18@hotmail.com', 'U2FtYW4xMjMh', '11', '220', '49');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`categoria_id`);

--
-- Indices de la tabla `ciudad`
--
ALTER TABLE `ciudad`
  ADD PRIMARY KEY (`ciudad_id`),
  ADD KEY `id_provincia` (`id_provincia`);

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`cod_compras`),
  ADD KEY `id_user` (`id_user`,`nombre_user`,`email_user`,`id_producto`,`nombre_producto`,`precio`);

--
-- Indices de la tabla `ecommerce`
--
ALTER TABLE `ecommerce`
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `marca`
--
ALTER TABLE `marca`
  ADD PRIMARY KEY (`id_marca`);

--
-- Indices de la tabla `pais`
--
ALTER TABLE `pais`
  ADD PRIMARY KEY (`pais_id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `id_categoria` (`id_categoria`),
  ADD KEY `id_marca` (`id_marca`);

--
-- Indices de la tabla `provincia`
--
ALTER TABLE `provincia`
  ADD PRIMARY KEY (`provincia_id`),
  ADD KEY `id_pais` (`id_pais`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`user_Id`),
  ADD KEY `id_ciudad` (`id_ciudad`),
  ADD KEY `id_provincia` (`id_provincia`),
  ADD KEY `id_pais` (`id_pais`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `cod_compras` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `user_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ciudad`
--
ALTER TABLE `ciudad`
  ADD CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`id_provincia`) REFERENCES `provincia` (`provincia_id`);

--
-- Filtros para la tabla `ecommerce`
--
ALTER TABLE `ecommerce`
  ADD CONSTRAINT `ecommerce_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `usuarios` (`user_Id`),
  ADD CONSTRAINT `ecommerce_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`codigo`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_marca`) REFERENCES `marca` (`id_marca`),
  ADD CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`categoria_id`),
  ADD CONSTRAINT `productos_ibfk_3` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`categoria_id`),
  ADD CONSTRAINT `productos_ibfk_4` FOREIGN KEY (`id_marca`) REFERENCES `marca` (`id_marca`);

--
-- Filtros para la tabla `provincia`
--
ALTER TABLE `provincia`
  ADD CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`pais_id`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`ciudad_id`),
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`ciudad_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
