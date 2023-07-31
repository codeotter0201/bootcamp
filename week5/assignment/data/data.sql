-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',10,'2023-07-31 20:51:57'),(2,'John Doe','johndoe','password1',10,'2023-07-31 18:51:57'),(3,'Jane Smith','janesmith','password2',5,'2023-07-31 20:51:57'),(4,'Alice Johnson','alicejohnson','password3',2,'2023-07-31 15:51:57'),(5,'Bob Williams','bobwilliams','password4',7,'2023-07-31 20:51:57');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'Message 210',85,'2023-08-03 16:55:16'),(2,2,'Message 733',272,'2023-08-01 01:55:16'),(3,3,'Message 985',447,'2023-08-01 12:55:16'),(4,4,'Message 54',432,'2023-07-31 09:55:16'),(5,5,'Message 709',543,'2023-08-02 19:55:16'),(8,1,'Message 307',775,'2023-08-04 08:55:17'),(9,2,'Message 444',359,'2023-08-02 07:55:17'),(10,3,'Message 248',844,'2023-08-02 08:55:17'),(11,4,'Message 852',830,'2023-08-02 20:55:17'),(12,5,'Message 491',668,'2023-08-03 23:55:17'),(15,1,'Message 326',32,'2023-08-01 03:55:18'),(16,2,'Message 828',584,'2023-08-02 04:55:18'),(17,3,'Message 445',905,'2023-08-01 04:55:18'),(18,4,'Message 239',626,'2023-08-02 02:55:18'),(19,5,'Message 178',656,'2023-08-03 11:55:18'),(22,1,'Message 764',584,'2023-08-02 23:55:19'),(23,2,'Message 383',35,'2023-07-31 11:55:19'),(24,3,'Message 19',22,'2023-07-31 14:55:19'),(25,4,'Message 211',888,'2023-08-03 17:55:19'),(26,5,'Message 374',448,'2023-07-31 20:55:19'),(29,1,'Message 243',863,'2023-08-02 19:55:21'),(30,2,'Message 349',983,'2023-08-03 23:55:21'),(31,3,'Message 398',381,'2023-08-03 08:55:21'),(32,4,'Message 410',921,'2023-08-01 22:55:21'),(33,5,'Message 120',470,'2023-08-04 12:55:21');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-31  8:58:23
