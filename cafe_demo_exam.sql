-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Сен 30 2024 г., 10:19
-- Версия сервера: 5.5.22
-- Версия PHP: 5.3.10-1ubuntu3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `cafe_demo_exam`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Drinks`
--

CREATE TABLE IF NOT EXISTS `Drinks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `Drinks`
--

INSERT INTO `Drinks` (`id`, `name`, `price`) VALUES
(1, 'Кола', 95),
(2, 'Апельсиновый сок', 119),
(3, 'Морс брусничный', 149),
(4, 'Чай зеленый', 79),
(5, 'Кофе', 179);

-- --------------------------------------------------------

--
-- Структура таблицы `Foods`
--

CREATE TABLE IF NOT EXISTS `Foods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `Foods`
--

INSERT INTO `Foods` (`id`, `name`, `price`) VALUES
(1, 'Салат Цезарь', 355),
(2, 'Паста Мясная', 379),
(3, 'Пицца Пепперони', 529),
(4, 'Паста Карбонара', 379),
(5, 'Пицца  Сырная', 409);

-- --------------------------------------------------------

--
-- Структура таблицы `Orders`
--

CREATE TABLE IF NOT EXISTS `Orders` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `count_cliens` int(11) NOT NULL,
  `table_id` int(11) NOT NULL,
  `drink_id` int(11) NOT NULL,
  `food_id` int(11) NOT NULL,
  `shift_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `Orders`
--

INSERT INTO `Orders` (`id`, `count_cliens`, `table_id`, `drink_id`, `food_id`, `shift_id`, `status_id`) VALUES
(1, 1, 2, 5, 4, 2, 4),
(2, 2, 5, 3, 1, 3, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `Roles`
--

CREATE TABLE IF NOT EXISTS `Roles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `role` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `Roles`
--

INSERT INTO `Roles` (`id`, `role`) VALUES
(1, 'Администратор'),
(2, 'Повар'),
(3, 'Официант');

-- --------------------------------------------------------

--
-- Структура таблицы `Shifts`
--

CREATE TABLE IF NOT EXISTS `Shifts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `cook` int(11) NOT NULL,
  `oficiant_1` int(11) NOT NULL,
  `oficiant_2` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `Shifts`
--

INSERT INTO `Shifts` (`id`, `date`, `cook`, `oficiant_1`, `oficiant_2`) VALUES
(1, '2024-09-29 10:00:00', 3, 5, 6),
(2, '2024-09-30 09:00:00', 2, 6, 7),
(3, '2024-10-01 11:00:00', 3, 7, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `Statuces`
--

CREATE TABLE IF NOT EXISTS `Statuces` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Дамп данных таблицы `Statuces`
--

INSERT INTO `Statuces` (`id`, `name`) VALUES
(1, 'принят'),
(2, 'оплачен'),
(3, 'готовится'),
(4, 'готов');

-- --------------------------------------------------------

--
-- Структура таблицы `Tables`
--

CREATE TABLE IF NOT EXISTS `Tables` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `Tables`
--

INSERT INTO `Tables` (`id`, `number`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `Users`
--

CREATE TABLE IF NOT EXISTS `Users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `password` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `role_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Дамп данных таблицы `Users`
--

INSERT INTO `Users` (`id`, `login`, `password`, `name`, `role_id`, `status`) VALUES
(1, 'admin_Ekaterina', '11111', 'Екатерина', 1, 1),
(2, 'cook_Alexandr', '123456', 'Александр', 2, 1),
(3, 'cook_Ivan', 'qwerty', 'Иван', 2, 0),
(4, 'cook_Petr', 'qazxsw', 'Петр', 2, 1),
(5, 'waiter_Anna', '54321', 'Анна', 3, 1),
(6, 'waiter_Ilya', 'Gfhjkm0', 'Илья', 3, 1),
(7, 'waiter_Sergey', 'Пароль0', 'Сергей', 3, 1),
(8, 'waiter_Angelina', 'Angelina89', 'Ангелина', 3, 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
