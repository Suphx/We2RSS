/*
 Navicat Premium Data Transfer

 Source Server         : 本地MongoDB
 Source Server Type    : MongoDB
 Source Server Version : 40208
 Source Host           : localhost:27017
 Source Schema         : we2rss

 Target Server Type    : MongoDB
 Target Server Version : 40208
 File Encoding         : 65001

 Date: 04/05/2021 09:57:39
*/


// ----------------------------
// Collection structure for passage_collections
// ----------------------------
db.getCollection("passage_collections").drop();
db.createCollection("passage_collections");

// ----------------------------
// Documents of passage_collections
// ----------------------------
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f3be6fe4538792c292e"),
    "passage_title": "星球英语彩蛋大盘点——水星、金星和地球",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-05-01T20:07:04Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247496075&idx=1&sn=d4ce5eb8b2c91eb0f861143517c25352&chksm=e9f47b6ade83f27ca406e3990a017166a8356d40ff1814a8388c1269741fce5309b945808c95#rd",
    "passage_update_time": ISODate("2021-05-01T20:07:04Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f3be6fe4538792c2932"),
    "passage_title": "外刊词汇 | ​单日新增35万！印度疫情何时到头？",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-04-27T19:11:17Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495966&idx=1&sn=7eed7b2a0638b343e890503bde2ec8ec&chksm=e9f47bffde83f2e9fbfa38c11aa2acddde6a9e4c87052e96f92527412efe11450df0199768f4#rd",
    "passage_update_time": ISODate("2021-04-27T19:11:17Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f3be6fe4538792c2936"),
    "passage_title": "如何有效提高阅读和写作？杂货社外刊读写训练营5月班来啦！",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-04-25T20:32:42Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495892&idx=1&sn=58aa9b6fd727f9c55562d9ebfbfdc366&chksm=e9f47a35de83f32343494185d1014dde96c1383cc30742a744b43bb5c61908d047b258b5dcee#rd",
    "passage_update_time": ISODate("2021-04-25T20:32:41Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f3be6fe4538792c293a"),
    "passage_title": "外刊写作 | 统一延迟退休合理吗？",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-04-21T18:27:05Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495754&idx=1&sn=a2976ed342782d4afa92442d79143600&chksm=e9f47aabde83f3bd64a3a17cf5981616a41211e5042de0f5bdb9e72b816174a7a0fa1b9addc9#rd",
    "passage_update_time": ISODate("2021-04-21T18:27:05Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f3be6fe4538792c293e"),
    "passage_title": "外刊精读视频 | 丑鞋当道？疫情下的鞋履新时尚",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-04-18T20:28:06Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495611&idx=1&sn=1dc56637684d282bedbb8fc08b9e487c&chksm=e9f4655ade83ec4cb7bedb1da511ebf77fee0d709d0a34bbb0e406de339909b022e65a526676#rd",
    "passage_update_time": ISODate("2021-04-18T20:28:06Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f4be6fe4538792c2946"),
    "passage_title": "外刊词汇 | ​日本宣布将福岛核污水排放入海",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-04-14T00:39:45Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495450&idx=1&sn=4ef3632b61a2dbb7b0f42a87ac68b52e&chksm=e9f465fbde83ecedaadf41e5700757daebf1fe01aa84c46cbcce0502eaf6ad2d81b2ea604f46#rd",
    "passage_update_time": ISODate("2021-04-14T08:00:00Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f4be6fe4538792c294a"),
    "passage_title": "外刊词汇 | 清明小长假，国内旅游大复苏",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-04-09T17:40:06Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495388&idx=1&sn=46430e669bf0e902df39bbbc8655f8b2&chksm=e9f4643dde83ed2b7428490d552afac4067194b79b0cf6c5ddd9104fa8277592e91ec34326c7#rd",
    "passage_update_time": ISODate("2021-04-09T17:40:06Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f4be6fe4538792c294e"),
    "passage_title": "外刊写作 | 小米造车？为什么科技公司适合造智能汽车？",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-04-01T20:23:57Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247495183&idx=1&sn=865c8e221f513e89234d0e0d767997ec&chksm=e9f464eede83edf88172e917a2e2740a14154ea2479bed7650a6e2036a746787e91a43b73e1f#rd",
    "passage_update_time": ISODate("2021-04-01T20:23:57Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f4be6fe4538792c2952"),
    "passage_title": "外刊词汇 | 一夜蒸发40亿的苏伊士运河通了！",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-03-30T21:03:00Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494958&idx=1&sn=2cf3b4025c465f96dd14710e17516f62&chksm=e9f467cfde83eed9f7a4f0de3b371099d5fb45322769837c8b075c7a77ccbbc9800230e5a9d7#rd",
    "passage_update_time": ISODate("2021-03-30T21:03:00Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f4be6fe4538792c2956"),
    "passage_title": "外刊精读视频 | 全球电商大乱斗，谁能雄踞一方？",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-03-27T20:12:37Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494869&idx=1&sn=e483285d09d9735f4880a66d9f728957&chksm=e9f46634de83ef22f8686af2545c64aef066b2fc8861c7b8583fa8b445ba950cfba676ffee71#rd",
    "passage_update_time": ISODate("2021-03-27T20:12:37Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f5ae6fe4538792c295f"),
    "passage_title": "外刊写作 | 如何描述H&M新疆棉花事件的前因后果？",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-03-25T21:40:30Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494764&idx=1&sn=30eac115c7e764dee97811c7459c925f&chksm=e9f4668dde83ef9bfd26172f13dc9e6a2fe735521596dda73528a766448aa291aad0bf098586#rd",
    "passage_update_time": ISODate("2021-03-25T21:40:30Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f5ae6fe4538792c2963"),
    "passage_title": "全新单元！外刊读写训练营第2期来啦",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-03-24T20:03:33Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494694&idx=1&sn=6781adb5c798e4f8471e81deb8b0c8b3&chksm=e9f466c7de83efd17b7fa5903afa91d6f57f9ebb33f3f94a0e1f4bea1a8e762504a5923c7d9a#rd",
    "passage_update_time": ISODate("2021-03-24T20:03:33Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f5ae6fe4538792c2967"),
    "passage_title": "外刊词汇 | 扎导版《正义联盟》上线，DC能力挽狂澜吗？",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-03-23T18:12:51Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494283&idx=1&sn=fe9b06f2e74927d8095e524e9ccabba8&chksm=e9f4606ade83e97cfe742f2e5fcf5c5f68901dbbcf497b76a2e260a643f35a94a8822b40aa8b#rd",
    "passage_update_time": ISODate("2021-03-23T18:12:51Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f5ae6fe4538792c296b"),
    "passage_title": "外刊精读视频 | 6900万美元买张“JPG图”值不值？",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-03-21T20:43:41Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494215&idx=1&sn=6e17ff28a843d1b90e71a46479d11875&chksm=e9f460a6de83e9b05e2a0e76d5c9fcead43329b0b60c45136edb722c5ca25983e9584af70ac9#rd",
    "passage_update_time": ISODate("2021-03-21T20:43:41Z")
} ]);
db.getCollection("passage_collections").insert([ {
    _id: ObjectId("60900f5ae6fe4538792c296f"),
    "passage_title": "外刊写作 | 应届生就业难？试试绿色就业吧",
    "official_account_id": NumberInt("2"),
    "passage_create_time": ISODate("2021-03-18T21:03:59Z"),
    "passage_link": "http://mp.weixin.qq.com/s?__biz=MzI1MTE5MTE4Mg==&mid=2247494194&idx=1&sn=2d46a22e4680d330aead479b02266397&chksm=e9f460d3de83e9c52cb523174b5ce2a6c5bef1913c03c23c32dc5dc04775fa853c9f9c7c8d7e#rd",
    "passage_update_time": ISODate("2021-03-18T21:03:59Z")
} ]);
