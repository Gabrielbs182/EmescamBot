-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 15, 2018 at 07:55 PM
-- Server version: 5.7.24-0ubuntu0.16.04.1
-- PHP Version: 7.0.32-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `dados`
--

CREATE TABLE `dados` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `sobrenome` varchar(255) DEFAULT NULL,
  `cpf` varchar(20) DEFAULT NULL,
  `sangue` varchar(5) DEFAULT NULL,
  `pais` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `cep` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dados`
--

INSERT INTO `dados` (`id`, `nome`, `sobrenome`, `cpf`, `sangue`, `pais`, `estado`, `cep`) VALUES
(1, 'André ', 'Souza', '000.000.000-01', 'A+', 'Brasil', 'Espirito Santo', 29153000),
(2, 'Thiago ', 'Vieira', '000.000.000-02', 'B-', 'Brasil', 'Espirito Santo', 29153100),
(3, 'Matheus ', 'Oliveira', '000.000.000-03', 'B+', 'Brasil', 'Espirito Santo', 29153100),
(4, 'Gabriel ', 'Henrique', '000.000.000-04', 'AB-', 'Brasil', 'Espirito Santo', 29153100),
(5, 'Daniel ', 'Ferreira', '000.000.000-05', 'O-', 'Brasil', 'Espirito Santo', 29153100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dados`
--
ALTER TABLE `dados`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dados`
--
ALTER TABLE `dados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
