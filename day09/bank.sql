/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.5.43 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `abc` */

DROP TABLE IF EXISTS `abc`;

CREATE TABLE `abc` (
  `uid` varchar(20) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `passwd` varchar(30) DEFAULT NULL,
  `money` varchar(60) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `bank_deposit` varchar(20) NOT NULL,
  `card` int(1) DEFAULT '0',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `abc` */

insert  into `abc`(`uid`,`username`,`passwd`,`money`,`address`,`bank_deposit`,`card`) values ('958764715','刘磊举','123456','50000','中国河北朝阳街3巷四号','中国农业银行',1);

/*Table structure for table `icbc` */

DROP TABLE IF EXISTS `icbc`;

CREATE TABLE `icbc` (
  `uid` varchar(20) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `passwd` varchar(30) DEFAULT NULL,
  `money` varchar(60) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `bank_deposit` varchar(20) NOT NULL,
  `card` int(1) DEFAULT '0',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `icbc` */

insert  into `icbc`(`uid`,`username`,`passwd`,`money`,`address`,`bank_deposit`,`card`) values ('713277933','刘磊举','123456','40000','中国河北朝阳街3巷四号','中国工商银行',0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
