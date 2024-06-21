-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydbsj
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `idAdmin` int NOT NULL,
  `korisnickoImeAdmin` varchar(45) NOT NULL,
  `lozinkaAdmin` varchar(45) NOT NULL,
  `imeAdmin` varchar(45) NOT NULL,
  `prezimeAdmin` varchar(45) NOT NULL,
  `gmailAdmin` varchar(45) NOT NULL,
  PRIMARY KEY (`idAdmin`),
  UNIQUE KEY `lozinkaAdmin_UNIQUE` (`lozinkaAdmin`),
  UNIQUE KEY `korisnickoImeAdmin_UNIQUE` (`korisnickoImeAdmin`),
  UNIQUE KEY `gmailAdmin_UNIQUE` (`gmailAdmin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin1','lozinka1','Sanja','Sobot','ssanja99@gmail.com'),(2,'admin2','lozinka2','Nina','Ostojic','onina99@gmail.com');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infonakit`
--

DROP TABLE IF EXISTS `infonakit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `infonakit` (
  `idInfoNakit` int NOT NULL,
  `cenaNakita` int NOT NULL,
  `kolicinaNakita` int NOT NULL,
  `Nakit_idNakit` int NOT NULL,
  PRIMARY KEY (`idInfoNakit`),
  KEY `fk_InfoNakit_Nakit1_idx` (`Nakit_idNakit`),
  CONSTRAINT `fk_InfoNakit_Nakit1` FOREIGN KEY (`Nakit_idNakit`) REFERENCES `nakit` (`idNakit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infonakit`
--

LOCK TABLES `infonakit` WRITE;
/*!40000 ALTER TABLE `infonakit` DISABLE KEYS */;
INSERT INTO `infonakit` VALUES (1,5000,37,1),(2,1500,62,2),(3,19999,14,3),(4,7899,12,4),(5,5540,7,5),(6,1300,94,6);
/*!40000 ALTER TABLE `infonakit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infosat`
--

DROP TABLE IF EXISTS `infosat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `infosat` (
  `idInfoSat` int NOT NULL,
  `cenaSat` int NOT NULL,
  `kolicinaSat` int NOT NULL,
  `Sat_idSat` int NOT NULL,
  PRIMARY KEY (`idInfoSat`),
  KEY `fk_InfoSat_Sat1_idx` (`Sat_idSat`),
  CONSTRAINT `fk_InfoSat_Sat1` FOREIGN KEY (`Sat_idSat`) REFERENCES `sat` (`idSat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infosat`
--

LOCK TABLES `infosat` WRITE;
/*!40000 ALTER TABLE `infosat` DISABLE KEYS */;
INSERT INTO `infosat` VALUES (1,26000,21,1),(2,12800,9,2),(3,8550,32,3),(4,34000,15,4),(5,56099,4,5),(6,32100,13,6);
/*!40000 ALTER TABLE `infosat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik` (
  `idKorisnik` int NOT NULL,
  `imeKorisnika` varchar(45) NOT NULL,
  `prezimeKorisnika` varchar(45) NOT NULL,
  `korisnickoImeKorisnika` varchar(45) NOT NULL,
  `lozinkaKorisnika` varchar(45) NOT NULL,
  `adresa` varchar(45) NOT NULL,
  `gmailKorisnik` varchar(45) NOT NULL,
  PRIMARY KEY (`idKorisnik`),
  UNIQUE KEY `korisnickoImeKorisnika_UNIQUE` (`korisnickoImeKorisnika`),
  UNIQUE KEY `lozinkaKorisnika_UNIQUE` (`lozinkaKorisnika`),
  UNIQUE KEY `gmail_UNIQUE` (`gmailKorisnik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES (1,'Jelena','Radisic','korisnik1','lozinka1','Mosorinska 108 Zrenjanin','jelena@gmail.com'),(2,'Mirjana','Pavlovic','korisnik2','lozinka2','Bulevar Oslobodjenja 78 Novi Sad','mirjana@gmail.com'),(3,'Vladimir','Adamov','korisnik3','lozinka3','Cara Dusana 81 Beograd','vladimir@gmail.com'),(4,'Milena','Knezevic','korisnik4','lozinka4','Ive Lole Ribara 12 Elemir','milena@gmail.com');
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nakit`
--

DROP TABLE IF EXISTS `nakit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nakit` (
  `idNakit` int NOT NULL,
  `nazivNakita` varchar(45) NOT NULL,
  `Admin_idAdmin` int NOT NULL,
  PRIMARY KEY (`idNakit`),
  KEY `fk_Nakit_Admin1_idx` (`Admin_idAdmin`),
  CONSTRAINT `fk_Nakit_Admin1` FOREIGN KEY (`Admin_idAdmin`) REFERENCES `admin` (`idAdmin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nakit`
--

LOCK TABLES `nakit` WRITE;
/*!40000 ALTER TABLE `nakit` DISABLE KEYS */;
INSERT INTO `nakit` VALUES (1,'Zlatne mindjuse',2),(2,'Srebrne mindjuse',2),(3,'Zlatni lancic',2),(4,'Srebrni lancic',2),(5,'Zlatna narukvica',2),(6,'Srebrna narukvica',2);
/*!40000 ALTER TABLE `nakit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prikaznakit`
--

DROP TABLE IF EXISTS `prikaznakit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prikaznakit` (
  `idPrikazNakit` int NOT NULL,
  `Korisnik_idKorisnik` int NOT NULL,
  `Nakit_idNakit` int NOT NULL,
  PRIMARY KEY (`idPrikazNakit`),
  KEY `fk_PrikazNakit_Korisnik1_idx` (`Korisnik_idKorisnik`),
  KEY `fk_PrikazNakit_Nakit1_idx` (`Nakit_idNakit`),
  CONSTRAINT `fk_PrikazNakit_Korisnik1` FOREIGN KEY (`Korisnik_idKorisnik`) REFERENCES `korisnik` (`idKorisnik`),
  CONSTRAINT `fk_PrikazNakit_Nakit1` FOREIGN KEY (`Nakit_idNakit`) REFERENCES `nakit` (`idNakit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prikaznakit`
--

LOCK TABLES `prikaznakit` WRITE;
/*!40000 ALTER TABLE `prikaznakit` DISABLE KEYS */;
INSERT INTO `prikaznakit` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,2,1),(8,2,2),(9,2,3),(10,2,4),(11,2,5),(12,2,6),(13,3,1),(14,3,2),(15,3,3),(16,3,4),(17,3,5),(18,3,6),(19,4,1),(20,4,2),(21,4,3),(22,4,4),(23,4,5),(24,4,6);
/*!40000 ALTER TABLE `prikaznakit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prikazsat`
--

DROP TABLE IF EXISTS `prikazsat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prikazsat` (
  `idPrikazSat` int NOT NULL,
  `Korisnik_idKorisnik` int NOT NULL,
  `Sat_idSat` int NOT NULL,
  PRIMARY KEY (`idPrikazSat`),
  KEY `fk_PrikazSat_Korisnik_idx` (`Korisnik_idKorisnik`),
  KEY `fk_PrikazSat_Sat1_idx` (`Sat_idSat`),
  CONSTRAINT `fk_PrikazSat_Korisnik` FOREIGN KEY (`Korisnik_idKorisnik`) REFERENCES `korisnik` (`idKorisnik`),
  CONSTRAINT `fk_PrikazSat_Sat1` FOREIGN KEY (`Sat_idSat`) REFERENCES `sat` (`idSat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prikazsat`
--

LOCK TABLES `prikazsat` WRITE;
/*!40000 ALTER TABLE `prikazsat` DISABLE KEYS */;
INSERT INTO `prikazsat` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,2,1),(8,2,2),(9,2,3),(10,2,4),(11,2,5),(12,2,6),(13,3,1),(14,3,2),(15,3,3),(16,3,4),(17,3,5),(18,3,6),(19,4,1),(20,4,2),(21,4,3),(22,4,4),(23,4,5),(24,4,6);
/*!40000 ALTER TABLE `prikazsat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `racunnakit`
--

DROP TABLE IF EXISTS `racunnakit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `racunnakit` (
  `idRacunNakit` int NOT NULL,
  `ukupnaCenaNakit` int NOT NULL,
  `porudzbinaNakit` varchar(45) NOT NULL,
  `Korisnik_idKorisnik` int NOT NULL,
  `Nakit_idNakit` int NOT NULL,
  `Admin_idAdmin` int NOT NULL,
  `datumPorudzbineNakit` varchar(45) NOT NULL,
  PRIMARY KEY (`idRacunNakit`),
  KEY `fk_RacunNakit_Korisnik1_idx` (`Korisnik_idKorisnik`),
  KEY `fk_RacunNakit_Nakit1_idx` (`Nakit_idNakit`),
  KEY `fk_RacunNakit_Admin1_idx` (`Admin_idAdmin`),
  CONSTRAINT `fk_RacunNakit_Admin1` FOREIGN KEY (`Admin_idAdmin`) REFERENCES `admin` (`idAdmin`),
  CONSTRAINT `fk_RacunNakit_Korisnik1` FOREIGN KEY (`Korisnik_idKorisnik`) REFERENCES `korisnik` (`idKorisnik`),
  CONSTRAINT `fk_RacunNakit_Nakit1` FOREIGN KEY (`Nakit_idNakit`) REFERENCES `nakit` (`idNakit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `racunnakit`
--

LOCK TABLES `racunnakit` WRITE;
/*!40000 ALTER TABLE `racunnakit` DISABLE KEYS */;
INSERT INTO `racunnakit` VALUES (1,1500,'Srebrne mindjuse',4,2,2,'11.12.2022.'),(2,1300,'Srebrna narukvica',1,6,2,'11.12.2022.'),(3,19999,'Zlatan lancic',3,3,2,'11.01.2023.');
/*!40000 ALTER TABLE `racunnakit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `racunsat`
--

DROP TABLE IF EXISTS `racunsat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `racunsat` (
  `idRacunSat` int NOT NULL,
  `ukupnaCenaSat` int NOT NULL,
  `porudzbinaSat` varchar(45) NOT NULL,
  `Korisnik_idKorisnik` int NOT NULL,
  `Sat_idSat` int NOT NULL,
  `Admin_idAdmin` int NOT NULL,
  `datumPorudzbineSat` varchar(45) NOT NULL,
  PRIMARY KEY (`idRacunSat`),
  KEY `fk_Racun_Korisnik1_idx` (`Korisnik_idKorisnik`),
  KEY `fk_Racun_Sat1_idx` (`Sat_idSat`),
  KEY `fk_RacunSat_Admin1_idx` (`Admin_idAdmin`),
  CONSTRAINT `fk_Racun_Korisnik1` FOREIGN KEY (`Korisnik_idKorisnik`) REFERENCES `korisnik` (`idKorisnik`),
  CONSTRAINT `fk_Racun_Sat1` FOREIGN KEY (`Sat_idSat`) REFERENCES `sat` (`idSat`),
  CONSTRAINT `fk_RacunSat_Admin1` FOREIGN KEY (`Admin_idAdmin`) REFERENCES `admin` (`idAdmin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `racunsat`
--

LOCK TABLES `racunsat` WRITE;
/*!40000 ALTER TABLE `racunsat` DISABLE KEYS */;
INSERT INTO `racunsat` VALUES (1,56099,'Jaguar',2,5,1,'23.12.2022.'),(2,34000,'Guess',1,4,1,'10.01.2023.'),(3,26000,'Armani',4,1,1,'13.01.2023.');
/*!40000 ALTER TABLE `racunsat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sat`
--

DROP TABLE IF EXISTS `sat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sat` (
  `idSat` int NOT NULL,
  `nazivSata` varchar(45) NOT NULL,
  `Admin_idAdmin` int NOT NULL,
  PRIMARY KEY (`idSat`),
  KEY `fk_Sat_Admin1_idx` (`Admin_idAdmin`),
  CONSTRAINT `fk_Sat_Admin1` FOREIGN KEY (`Admin_idAdmin`) REFERENCES `admin` (`idAdmin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sat`
--

LOCK TABLES `sat` WRITE;
/*!40000 ALTER TABLE `sat` DISABLE KEYS */;
INSERT INTO `sat` VALUES (1,'Armani',1),(2,'Diesel',1),(3,'DKNY',1),(4,'Guess',1),(5,'Jaguar',1),(6,'Tommy Hilfiger',1);
/*!40000 ALTER TABLE `sat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'mydbsj'
--

--
-- Dumping routines for database 'mydbsj'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-14 19:10:44
