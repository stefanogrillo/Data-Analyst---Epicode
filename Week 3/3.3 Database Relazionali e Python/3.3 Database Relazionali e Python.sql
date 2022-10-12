CREATE DATABASE `discografia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- discografia.disco definition

CREATE TABLE `disco` (
  `NroSerie` varchar(100) NOT NULL,
  `TitoloAlbum` varchar(100) DEFAULT NULL,
  `Anno` year NOT NULL,
  `Prezzo` float(4,2) NOT NULL,
  PRIMARY KEY (`NroSerie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.esecuzione definition

CREATE TABLE `esecuzione` (
  `CodiceReg` varchar(100) NOT NULL,
  `TitoloCanzone` varchar(100) NOT NULL,
  `Anno` year NOT NULL,
  PRIMARY KEY (`CodiceReg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.autore definition

CREATE TABLE `autore` (
  `nome` varchar(100) NOT NULL,
  `TitoloCanzone` varchar(100) NOT NULL,
  PRIMARY KEY (`nome`,`TitoloCanzone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.contiene definition

CREATE TABLE `contiene` (
  `NroSerieDisco` varchar(100) NOT NULL,
  `CodiceReg` varchar(100) NOT NULL,
  `NroProg` varchar(100) NOT NULL,
  PRIMARY KEY (`NroSerieDisco`,`CodiceReg`),
  KEY `contiene_FK_1` (`CodiceReg`),
  CONSTRAINT `contiene_FK` FOREIGN KEY (`NroSerieDisco`) REFERENCES `disco` (`NroSerie`),
  CONSTRAINT `contiene_FK_1` FOREIGN KEY (`CodiceReg`) REFERENCES `esecuzione` (`CodiceReg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.canzone definition

CREATE TABLE `canzone` (
  `NomeCantante` varchar(100) NOT NULL,
  `CodiceReg` varchar(100) NOT NULL,
  PRIMARY KEY (`NomeCantante`,`CodiceReg`),
  KEY `canzone_FK` (`CodiceReg`),
  CONSTRAINT `canzone_FK` FOREIGN KEY (`CodiceReg`) REFERENCES `esecuzione` (`CodiceReg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
