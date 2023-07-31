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
INSERT INTO `member` VALUES (1,'test2','test','test',10,'2023-07-31 15:56:09'),(2,'John Doe','johndoe','password1',10,'2023-07-31 08:56:09'),(3,'Jane Smith','janesmith','password2',5,'2023-07-31 13:56:09'),(4,'Alice Johnson','alicejohnson','password3',2,'2023-07-31 08:56:09'),(5,'Bob Williams','bobwilliams','password4',7,'2023-07-31 08:56:09');
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
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'Message 637',194,'2023-07-31 14:20:41'),(2,2,'Message 712',384,'2023-08-03 15:20:41'),(3,3,'Message 768',488,'2023-07-31 22:20:41'),(4,4,'Message 226',716,'2023-08-04 03:20:41'),(5,5,'Message 365',119,'2023-08-02 10:20:41'),(8,1,'Message 135',182,'2023-08-02 11:20:42'),(9,2,'Message 989',423,'2023-08-01 00:20:42'),(10,3,'Message 486',977,'2023-08-02 03:20:42'),(11,4,'Message 212',775,'2023-08-01 08:20:42'),(12,5,'Message 866',619,'2023-08-02 10:20:42'),(15,1,'Message 615',594,'2023-07-31 21:20:43'),(16,2,'Message 845',849,'2023-08-03 07:20:43'),(17,3,'Message 0',875,'2023-08-01 22:20:43'),(18,4,'Message 242',92,'2023-08-03 10:20:43'),(19,5,'Message 397',783,'2023-08-03 09:20:43'),(22,1,'Message 267',168,'2023-07-31 13:20:43'),(23,2,'Message 698',367,'2023-08-03 11:20:43'),(24,3,'Message 613',837,'2023-08-01 19:20:43'),(25,4,'Message 228',97,'2023-08-03 17:20:43'),(26,5,'Message 722',200,'2023-08-03 20:20:43'),(29,1,'Message 588',428,'2023-08-01 22:20:44'),(30,2,'Message 598',861,'2023-08-02 12:20:44'),(31,3,'Message 985',385,'2023-08-04 10:20:44'),(32,4,'Message 703',602,'2023-08-04 03:20:44'),(33,5,'Message 697',785,'2023-08-03 20:20:44'),(36,1,'Message 807',540,'2023-08-01 12:20:44'),(37,2,'Message 772',28,'2023-08-03 19:20:44'),(38,3,'Message 33',694,'2023-08-01 22:20:44'),(39,4,'Message 775',764,'2023-08-02 10:20:44'),(40,5,'Message 183',432,'2023-08-02 22:20:44'),(43,1,'Message 755',946,'2023-08-02 07:20:45'),(44,2,'Message 496',81,'2023-08-04 04:20:45'),(45,3,'Message 331',913,'2023-08-02 18:20:45'),(46,4,'Message 119',880,'2023-07-31 13:20:45'),(47,5,'Message 584',788,'2023-08-01 03:20:45'),(50,1,'Message 567',279,'2023-08-03 06:20:45'),(51,2,'Message 640',112,'2023-08-03 01:20:45'),(52,3,'Message 878',462,'2023-08-03 04:20:45'),(53,4,'Message 988',918,'2023-08-02 23:20:45'),(54,5,'Message 378',13,'2023-08-04 06:20:45'),(57,1,'Message 619',302,'2023-08-03 02:20:46'),(58,2,'Message 355',821,'2023-07-31 12:20:46'),(59,3,'Message 734',553,'2023-08-02 17:20:46'),(60,4,'Message 158',102,'2023-07-31 12:20:46'),(61,5,'Message 873',256,'2023-08-03 03:20:46');
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

-- Dump completed on 2023-07-31  8:37:38
