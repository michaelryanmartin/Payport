-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 30, 2021 at 06:52 AM
-- Server version: 10.5.5-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `payport`
--

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `IDAnggota` int(11) NOT NULL,
  `NamaAnggota` varchar(50) NOT NULL,
  `TipeAnggota` varchar(10) NOT NULL,
  `Username` varchar(10) NOT NULL,
  `Password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`IDAnggota`, `NamaAnggota`, `TipeAnggota`, `Username`, `Password`) VALUES
(7, 'John', 'Staff', 'chef_john', 'john'),
(10, 'admin', 'Owner', 'admin', 'admin'),
(49, 'Staff', 'Staff', 'staff', 'staff'),
(50, 'Owner', 'Owner', 'owner', 'owner');

-- --------------------------------------------------------

--
-- Table structure for table `pesanan`
--

CREATE TABLE `pesanan` (
  `IDTransaksi` int(11) NOT NULL,
  `NomorPesanan` int(11) NOT NULL,
  `IDProduk` int(11) NOT NULL,
  `Kuantitas` int(11) NOT NULL,
  `Harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pesanan`
--

INSERT INTO `pesanan` (`IDTransaksi`, `NomorPesanan`, `IDProduk`, `Kuantitas`, `Harga`) VALUES
(86, 82, 3, 1, 10000),
(87, 83, 2, 1, 25000),
(88, 84, 3, 1, 10000),
(90, 86, 1, 1, 20000),
(91, 87, 3, 1, 10000),
(94, 90, 1, 3, 60000),
(94, 91, 2, 1, 25000),
(94, 92, 3, 4, 40000),
(95, 93, 1, 5, 100000),
(95, 94, 2, 2, 50000),
(95, 95, 3, 2, 20000),
(116, 116, 1, 1, 20000),
(116, 117, 2, 1, 25000),
(116, 118, 3, 2, 20000),
(117, 119, 1, 1, 20000),
(117, 120, 3, 2, 20000),
(118, 121, 3, 1, 10000),
(121, 124, 2, 1, 25000);

-- --------------------------------------------------------

--
-- Table structure for table `produk`
--

CREATE TABLE `produk` (
  `IDProduk` int(11) NOT NULL,
  `NamaProduk` varchar(50) NOT NULL,
  `Deskripsi` varchar(100) DEFAULT NULL,
  `HargaProduk` int(11) NOT NULL,
  `Stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `produk`
--

INSERT INTO `produk` (`IDProduk`, `NamaProduk`, `Deskripsi`, `HargaProduk`, `Stok`) VALUES
(1, 'Original Chicken', 'Ayam Goreng rasa Original', 20000, 100),
(2, 'Onion Chicken', 'Ayam Goreng rasa Bawang', 25000, 100),
(3, 'Teh Manis', 'Minuman Teh (Hot/Ice)', 10000, 200);

-- --------------------------------------------------------

--
-- Table structure for table `promosi`
--

CREATE TABLE `promosi` (
  `IDPromosi` int(11) NOT NULL,
  `NamaPromosi` varchar(50) NOT NULL,
  `JumlahPromosi` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `promosi`
--

INSERT INTO `promosi` (`IDPromosi`, `NamaPromosi`, `JumlahPromosi`) VALUES
(1, 'Don\'t Use Discount', 0),
(3, '12.12', 0.2);

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `IDTransaksi` int(11) NOT NULL,
  `IDAnggota` int(11) NOT NULL,
  `IDPromosi` int(11) DEFAULT NULL,
  `Tanggal` date DEFAULT current_timestamp(),
  `TotalHarga` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`IDTransaksi`, `IDAnggota`, `IDPromosi`, `Tanggal`, `TotalHarga`) VALUES
(86, 7, 1, '2021-11-29', 11000),
(87, 7, 1, '2021-11-29', 27500),
(88, 7, 3, '2021-11-29', 8800),
(90, 7, 1, '2021-11-29', 22000),
(91, 7, 1, '2021-11-29', 11000),
(94, 7, 3, '2021-11-29', 110000),
(95, 7, 3, '2021-11-29', 149600),
(116, 7, 3, '2021-11-30', 57200),
(117, 7, 3, '2021-11-30', 35200),
(118, 7, 1, '2021-11-30', 11000),
(121, 49, 1, '2021-11-30', 27500);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`IDAnggota`);

--
-- Indexes for table `pesanan`
--
ALTER TABLE `pesanan`
  ADD PRIMARY KEY (`NomorPesanan`),
  ADD KEY `IDTransaksi` (`IDTransaksi`);

--
-- Indexes for table `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`IDProduk`);

--
-- Indexes for table `promosi`
--
ALTER TABLE `promosi`
  ADD PRIMARY KEY (`IDPromosi`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`IDTransaksi`),
  ADD KEY `IDAnggota` (`IDAnggota`),
  ADD KEY `IDPromosi` (`IDPromosi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anggota`
--
ALTER TABLE `anggota`
  MODIFY `IDAnggota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `pesanan`
--
ALTER TABLE `pesanan`
  MODIFY `NomorPesanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=125;

--
-- AUTO_INCREMENT for table `produk`
--
ALTER TABLE `produk`
  MODIFY `IDProduk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `promosi`
--
ALTER TABLE `promosi`
  MODIFY `IDPromosi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `IDTransaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pesanan`
--
ALTER TABLE `pesanan`
  ADD CONSTRAINT `pesanan_ibfk_1` FOREIGN KEY (`IDTransaksi`) REFERENCES `transaksi` (`IDTransaksi`) ON DELETE CASCADE;

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`IDAnggota`) REFERENCES `anggota` (`IDAnggota`),
  ADD CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`IDPromosi`) REFERENCES `promosi` (`IDPromosi`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
