/*
 Navicat Premium Data Transfer

 Source Server         : 本地MySQL
 Source Server Type    : MySQL
 Source Server Version : 50710
 Source Host           : localhost:3306
 Source Schema         : wechat_official_account_passage_rss

 Target Server Type    : MySQL
 Target Server Version : 50710
 File Encoding         : 65001

 Date: 04/05/2021 09:57:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for passage_link_list
-- ----------------------------
DROP TABLE IF EXISTS `passage_link_list`;
CREATE TABLE `passage_link_list`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信公众号文章名称',
  `passage_link` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '文章链接',
  `official_account_id` int(11) NOT NULL COMMENT '发布文章的公众号id',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 225 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of passage_link_list
-- ----------------------------
INSERT INTO `passage_link_list` VALUES (194, '星球英语彩蛋大盘点——水星、金星和地球', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247496075&idx=1&sn=d4ce5eb8b2c91eb0f861143517c25352&chksm=e9f47b6ade83f27ca406e3990a017166a8356d40ff1814a8388c1269741fce5309b945808c95#rd', 2, '2021-05-03 16:09:13');
INSERT INTO `passage_link_list` VALUES (195, '外刊词汇 | ​单日新增35万！印度疫情何时到头？', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495966&idx=1&sn=7eed7b2a0638b343e890503bde2ec8ec&chksm=e9f47bffde83f2e9fbfa38c11aa2acddde6a9e4c87052e96f92527412efe11450df0199768f4#rd', 2, '2021-05-03 16:09:13');
INSERT INTO `passage_link_list` VALUES (196, '如何有效提高阅读和写作？杂货社外刊读写训练营5月班来啦！', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495892&idx=1&sn=58aa9b6fd727f9c55562d9ebfbfdc366&chksm=e9f47a35de83f32343494185d1014dde96c1383cc30742a744b43bb5c61908d047b258b5dcee#rd', 2, '2021-05-03 16:09:13');
INSERT INTO `passage_link_list` VALUES (197, '外刊写作 | 统一延迟退休合理吗？', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495754&idx=1&sn=a2976ed342782d4afa92442d79143600&chksm=e9f47aabde83f3bd64a3a17cf5981616a41211e5042de0f5bdb9e72b816174a7a0fa1b9addc9#rd', 2, '2021-05-03 16:09:13');
INSERT INTO `passage_link_list` VALUES (198, '外刊精读视频 | 丑鞋当道？疫情下的鞋履新时尚', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495611&idx=1&sn=1dc56637684d282bedbb8fc08b9e487c&chksm=e9f4655ade83ec4cb7bedb1da511ebf77fee0d709d0a34bbb0e406de339909b022e65a526676#rd', 2, '2021-05-03 16:09:13');
INSERT INTO `passage_link_list` VALUES (199, '外刊词汇 | ​日本宣布将福岛核污水排放入海', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495450&idx=1&sn=4ef3632b61a2dbb7b0f42a87ac68b52e&chksm=e9f465fbde83ecedaadf41e5700757daebf1fe01aa84c46cbcce0502eaf6ad2d81b2ea604f46#rd', 2, '2021-05-03 16:09:29');
INSERT INTO `passage_link_list` VALUES (200, '外刊词汇 | 清明小长假，国内旅游大复苏', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495388&idx=1&sn=46430e669bf0e902df39bbbc8655f8b2&chksm=e9f4643dde83ed2b7428490d552afac4067194b79b0cf6c5ddd9104fa8277592e91ec34326c7#rd', 2, '2021-05-03 16:09:29');
INSERT INTO `passage_link_list` VALUES (201, '外刊写作 | 小米造车？为什么科技公司适合造智能汽车？', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495183&idx=1&sn=865c8e221f513e89234d0e0d767997ec&chksm=e9f464eede83edf88172e917a2e2740a14154ea2479bed7650a6e2036a746787e91a43b73e1f#rd', 2, '2021-05-03 16:09:29');
INSERT INTO `passage_link_list` VALUES (202, '外刊词汇 | 一夜蒸发40亿的苏伊士运河通了！', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494958&idx=1&sn=2cf3b4025c465f96dd14710e17516f62&chksm=e9f467cfde83eed9f7a4f0de3b371099d5fb45322769837c8b075c7a77ccbbc9800230e5a9d7#rd', 2, '2021-05-03 16:09:29');
INSERT INTO `passage_link_list` VALUES (203, '外刊精读视频 | 全球电商大乱斗，谁能雄踞一方？', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494869&idx=1&sn=e483285d09d9735f4880a66d9f728957&chksm=e9f46634de83ef22f8686af2545c64aef066b2fc8861c7b8583fa8b445ba950cfba676ffee71#rd', 2, '2021-05-03 16:09:29');
INSERT INTO `passage_link_list` VALUES (204, '外刊写作 | 如何描述H&M新疆棉花事件的前因后果？', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494764&idx=1&sn=30eac115c7e764dee97811c7459c925f&chksm=e9f4668dde83ef9bfd26172f13dc9e6a2fe735521596dda73528a766448aa291aad0bf098586#rd', 2, '2021-05-03 16:09:44');
INSERT INTO `passage_link_list` VALUES (205, '全新单元！外刊读写训练营第2期来啦', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494694&idx=1&sn=6781adb5c798e4f8471e81deb8b0c8b3&chksm=e9f466c7de83efd17b7fa5903afa91d6f57f9ebb33f3f94a0e1f4bea1a8e762504a5923c7d9a#rd', 2, '2021-05-03 16:09:44');
INSERT INTO `passage_link_list` VALUES (206, '外刊词汇 | 扎导版《正义联盟》上线，DC能力挽狂澜吗？', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494283&idx=1&sn=fe9b06f2e74927d8095e524e9ccabba8&chksm=e9f4606ade83e97cfe742f2e5fcf5c5f68901dbbcf497b76a2e260a643f35a94a8822b40aa8b#rd', 2, '2021-05-03 16:09:44');
INSERT INTO `passage_link_list` VALUES (207, '外刊精读视频 | 6900万美元买张“JPG图”值不值？', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494215&idx=1&sn=6e17ff28a843d1b90e71a46479d11875&chksm=e9f460a6de83e9b05e2a0e76d5c9fcead43329b0b60c45136edb722c5ca25983e9584af70ac9#rd', 2, '2021-05-03 16:09:44');
INSERT INTO `passage_link_list` VALUES (208, '外刊写作 | 应届生就业难？试试绿色就业吧', 'http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494194&idx=1&sn=2d46a22e4680d330aead479b02266397&chksm=e9f460d3de83e9c52cb523174b5ce2a6c5bef1913c03c23c32dc5dc04775fa853c9f9c7c8d7e#rd', 2, '2021-05-03 16:09:44');

-- ----------------------------
-- Table structure for wechat_account_list
-- ----------------------------
DROP TABLE IF EXISTS `wechat_account_list`;
CREATE TABLE `wechat_account_list`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `official_account_name` varchar(35) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信公众号名称',
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of wechat_account_list
-- ----------------------------
INSERT INTO `wechat_account_list` VALUES (1, '一捧涵养泉', '2021-01-29 22:58:51');
INSERT INTO `wechat_account_list` VALUES (2, '三言两语杂货社', '2021-01-30 10:38:58');
INSERT INTO `wechat_account_list` VALUES (3, '我是程序汪', '2021-01-30 13:12:47');
INSERT INTO `wechat_account_list` VALUES (4, '环球时报', '2021-01-30 13:29:41');
INSERT INTO `wechat_account_list` VALUES (5, '共青团中央', '2021-05-03 14:57:44');

SET FOREIGN_KEY_CHECKS = 1;
