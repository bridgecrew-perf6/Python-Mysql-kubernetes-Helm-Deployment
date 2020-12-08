GRANT ALL PRIVILEGES ON appdb.* TO 'appuser'@'%';
create database appdb;
use appdb;
CREATE TABLE `data` (`title` varchar(255) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `data` VALUES ('Hello World');
UNLOCK TABLES;
