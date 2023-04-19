-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 19. Apr 2023 um 21:13
-- Server-Version: 10.4.24-MariaDB
-- PHP-Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `shelly_status`
--
DROP DATABASE IF EXISTS `shelly_status`;
CREATE DATABASE IF NOT EXISTS `shelly_status` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `shelly_status`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `wifi_sta_hist`
--

DROP TABLE IF EXISTS `wifi_sta_hist`;
CREATE TABLE `wifi_sta_hist` (
  `id` int(11) NOT NULL COMMENT 'ID des DS',
  `device_id` int(11) NOT NULL COMMENT 'ID des Gerätes',
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Zeitstempel des Eintrags',
  `connected` tinyint(1) NOT NULL COMMENT 'Boolean (0,1) ob Netzwerk verbunden ist, oder nicht',
  `ssid` varchar(255) NOT NULL COMMENT 'SSID des angeschlossenen Netzwerkes',
  `ip` varchar(255) NOT NULL,
  `rssi` tinyint(127) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Historientabelle für die WLAN Verbindung von Geräten';

--
-- Daten für Tabelle `wifi_sta_hist`
--

INSERT INTO `wifi_sta_hist` (`id`, `device_id`, `timestamp`, `connected`, `ssid`, `ip`, `rssi`) VALUES
(1, 1, '2023-04-19 13:34:30', 0, 'Skyfall', '192.168.178.1', -66),
(2, 1, '2023-04-19 14:48:45', 1, 'Skyfall', '192.168.178.12', -63),
(3, 1, '2023-04-19 15:00:55', 1, 'Skyfall', '192.168.178.12', -63),
(4, 1, '2023-04-19 18:00:30', 1, 'Skyfall', '192.168.178.12', -62),
(5, 1, '2023-04-19 18:13:53', 1, 'Skyfall', '192.168.178.12', -64),
(6, 1, '2023-04-19 18:19:11', 1, 'Skyfall', '192.168.178.12', -63),
(7, 1, '2023-04-19 18:47:44', 1, 'Skyfall', '192.168.178.12', -64),
(8, 1, '2023-04-19 19:03:30', 1, 'Skyfall', '192.168.178.12', -66),
(9, 1, '2023-04-19 19:07:29', 1, 'Skyfall', '192.168.178.12', -67),
(10, 1, '2023-04-19 19:08:48', 1, 'Skyfall', '192.168.178.12', -65),
(11, 1, '2023-04-19 19:08:58', 1, 'Skyfall', '192.168.178.12', -65),
(12, 1, '2023-04-19 19:11:32', 1, 'Skyfall', '192.168.178.12', -65),
(13, 1, '2023-04-19 19:11:33', 1, 'Skyfall', '192.168.178.12', -66);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `wifi_sta_hist`
--
ALTER TABLE `wifi_sta_hist`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `wifi_sta_hist`
--
ALTER TABLE `wifi_sta_hist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID des DS', AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
