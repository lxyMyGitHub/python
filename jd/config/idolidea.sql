/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50527
Source Host           : localhost:3306
Source Database       : idolidea

Target Server Type    : MYSQL
Target Server Version : 50527
File Encoding         : 65001

Date: 2020-07-06 08:49:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dictionary
-- ----------------------------
DROP TABLE IF EXISTS `dictionary`;
CREATE TABLE `dictionary` (
  `id` varchar(100) NOT NULL,
  `name` varchar(400) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for jdcontents
-- ----------------------------
DROP TABLE IF EXISTS `jdcontents`;
CREATE TABLE `jdcontents` (
  `id` varchar(100) NOT NULL,
  `sku` varchar(100) DEFAULT NULL,
  `dictType` varchar(100) DEFAULT NULL,
  `content` varchar(6000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for skudata
-- ----------------------------
DROP TABLE IF EXISTS `skudata`;
CREATE TABLE `skudata` (
  `id` varchar(100) NOT NULL,
  `content` varchar(4000) DEFAULT NULL,
  `sku` varchar(300) DEFAULT NULL,
  `dictType` varchar(100) DEFAULT NULL,
  `status` int(2) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
