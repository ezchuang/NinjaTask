-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
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
  PRIMARY KEY (`id`),
  KEY `name_index` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',100,'2023-08-02 02:25:41'),(2,'Frank','FAQzzz','9999',1000,'2023-08-02 02:25:46'),(3,'Zack','Zaaaaaak_the_king','kill Buzz',100000,'2023-08-02 02:25:53'),(4,'Sakura_Miko','business_tete','suisei',1820000,'2023-08-02 02:25:59'),(5,'Hoshimachi_suisei','Aqua_kawaii','aqua',1930000,'2023-08-02 02:26:04'),(9,'123','test1','1234',0,'2023-08-09 01:40:22'),(10,'123','12345','123',0,'2023-08-09 01:49:04'),(11,'123','99999','88888',0,'2023-08-09 01:49:21'),(12,'9999','8888','7777',0,'2023-08-10 12:25:23'),(13,'我是中文帳號名稱','我想用中文','5j/ jp6s062l41j4vu/6a87',0,'2023-08-10 18:17:07');
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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'test speak',1000,'2023-08-02 02:39:22'),(2,3,'kill Buzz Lightyear!!',1000000,'2023-08-02 02:41:53'),(3,3,'Buzz Lightyear!!',1000,'2023-08-02 02:42:17'),(4,3,'憎しみBuzz Lightyear!!',1000,'2023-08-02 02:42:24'),(5,2,'Call me Grate Frank',1,'2023-08-02 02:43:14'),(6,4,'ね',10000000,'2023-08-02 02:43:44'),(7,2,'Don\'t say no to me',1,'2023-08-02 02:44:15'),(8,5,'私の Stellar Stellar はすごいですよね!',10000000,'2023-08-02 02:50:37'),(9,1,'test want to say something...',10,'2023-08-02 02:51:17'),(10,1,'Can you spell Chinese? C-H-I-N-E-S-E',200000000,'2023-08-02 02:53:50'),(11,2,'I want to add something to this table, but I have no idea.',2,'2023-08-02 02:55:06'),(12,1,'測試',10,'2023-08-07 19:13:55'),(17,1,'留言系統測試',20000000,'2023-08-10 02:56:29'),(18,12,'留言系統測試2',30000,'2023-08-10 12:26:29'),(21,4,'留言系統測試2',10000,'2023-08-10 18:16:13'),(22,13,'全部都是中文，我來嘗試爆破資料庫的',2999,'2023-08-10 18:17:53'),(24,1,'別鬧啦!!! 自己程式碼參數傳遞沒做好，還跑去問助教啊!',0,'2023-08-12 23:33:14'),(25,4,'別鬧啦!!! 自己程式碼參數傳遞沒做好，還跑去問助教啊!',0,'2023-08-12 23:33:28'),(26,5,'別鬧啦!!! 自己程式碼參數傳遞沒做好，還跑去問助教啊!',0,'2023-08-12 23:34:21');
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

-- Dump completed on 2023-08-12 23:37:51
