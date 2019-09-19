SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `tabel_coba`;
CREATE TABLE `tabel_coba` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kode` varchar(255) NOT NULL,
  `identitas_pelapor` varchar(255) NOT NULL,
  `alamat_lokasi_laporan` text,
  `isi_laporan` text,
  `kategori` varchar(255) DEFAULT NULL,
  `opd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `tabel_coba` (`id`, `kode`, `identitas_pelapor`, `alamat_lokasi_laporan`, `isi_laporan`, `kategori`, `opd`) VALUES
(667,	'#423',	'Fulanah binti Fulan',	'Jl. Raya Raya Raya',	'Ini adalah laporan, ini adalah laporan, ini adalah laporan',	'Lalu Lintas dan Angkutan Jalan',	'DISHUB');