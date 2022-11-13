DROP DATABASE IF EXISTS `guang_yi`;
CREATE DATABASE guang_yi;
USE guang_yi;
/*
 Navicat Premium Data Transfer

 Source Server         : MySQL5
 Source Server Type    : MySQL
 Source Server Version : 50520
 Source Host           : localhost:3305
 Source Schema         : guang_yi

 Target Server Type    : MySQL
 Target Server Version : 50520
 File Encoding         : 65001

 Date: 13/11/2022 13:12:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for gy_history
-- ----------------------------
DROP TABLE IF EXISTS `gy_history`;
CREATE TABLE `gy_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mean` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 478 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of gy_history
-- ----------------------------
INSERT INTO `gy_history` VALUES (376, 'nih ', '国家卫生研究院');
INSERT INTO `gy_history` VALUES (377, 'compromise', '妥协');
INSERT INTO `gy_history` VALUES (378, 'breakfast', '早餐');
INSERT INTO `gy_history` VALUES (379, 'seaman', '水手');
INSERT INTO `gy_history` VALUES (380, 'appointment', '任命');
INSERT INTO `gy_history` VALUES (382, 'basketball', '篮球');
INSERT INTO `gy_history` VALUES (383, 'unite', 'unite');
INSERT INTO `gy_history` VALUES (384, 'dance', '跳舞');
INSERT INTO `gy_history` VALUES (385, 'carrier', '航空公司');
INSERT INTO `gy_history` VALUES (386, 'employment', '就业');
INSERT INTO `gy_history` VALUES (387, 'ad', '的');
INSERT INTO `gy_history` VALUES (388, 'expect', '预计');
INSERT INTO `gy_history` VALUES (389, 'tour', '之旅');
INSERT INTO `gy_history` VALUES (390, 'manual', '手册');
INSERT INTO `gy_history` VALUES (391, 'alcohol', '酒精');
INSERT INTO `gy_history` VALUES (392, 'world-wide', '全球范围内');
INSERT INTO `gy_history` VALUES (393, 'convenience', '方便');
INSERT INTO `gy_history` VALUES (394, 'settlement', '结算');
INSERT INTO `gy_history` VALUES (395, 'concept', '概念');
INSERT INTO `gy_history` VALUES (396, 'sometimes', '有时');
INSERT INTO `gy_history` VALUES (397, 'coin', '硬币');
INSERT INTO `gy_history` VALUES (398, 'squirrel', '松鼠');
INSERT INTO `gy_history` VALUES (399, 'past', '过去的');
INSERT INTO `gy_history` VALUES (400, 'recognize', '识别');
INSERT INTO `gy_history` VALUES (402, 'cave', '洞穴');
INSERT INTO `gy_history` VALUES (403, 'pinch', '捏');
INSERT INTO `gy_history` VALUES (404, 'moderate', '温和的');
INSERT INTO `gy_history` VALUES (405, 'concentration', '浓度');
INSERT INTO `gy_history` VALUES (406, 'reign', '统治');
INSERT INTO `gy_history` VALUES (407, 'correction', '修正');
INSERT INTO `gy_history` VALUES (408, '你的', 'your');
INSERT INTO `gy_history` VALUES (418, '你好', 'Hallo.');
INSERT INTO `gy_history` VALUES (420, '我', 'I');
INSERT INTO `gy_history` VALUES (421, 'am', '我');
INSERT INTO `gy_history` VALUES (422, 'i am', '我是');
INSERT INTO `gy_history` VALUES (423, 'see', '看到');
INSERT INTO `gy_history` VALUES (424, '苹果', 'りんご');
INSERT INTO `gy_history` VALUES (429, '但是', 'but');
INSERT INTO `gy_history` VALUES (430, '的', 'the');
INSERT INTO `gy_history` VALUES (431, 'when', '当');
INSERT INTO `gy_history` VALUES (436, '笨蛋', 'ばか');
INSERT INTO `gy_history` VALUES (437, '笨蛋', 'болва');
INSERT INTO `gy_history` VALUES (438, 'apple', 'В яблоко от яблони');
INSERT INTO `gy_history` VALUES (439, 'apple', 'apple');
INSERT INTO `gy_history` VALUES (442, 'apple', '苹果');
INSERT INTO `gy_history` VALUES (443, 'banana', '香蕉');
INSERT INTO `gy_history` VALUES (446, '你好', 'hola');
INSERT INTO `gy_history` VALUES (455, '和', 'and');
INSERT INTO `gy_history` VALUES (456, '和and', 'And the and');
INSERT INTO `gy_history` VALUES (457, '12', '12');
INSERT INTO `gy_history` VALUES (461, '你好', 'こんにちは');
INSERT INTO `gy_history` VALUES (462, '????.', 'いいですね.');
INSERT INTO `gy_history` VALUES (463, '好吧', 'いいだろう');
INSERT INTO `gy_history` VALUES (464, '你好', '?????');
INSERT INTO `gy_history` VALUES (466, '????.', '???? .');
INSERT INTO `gy_history` VALUES (467, 'peer', '??');
INSERT INTO `gy_history` VALUES (469, 'peer', 'peer');
INSERT INTO `gy_history` VALUES (471, 'peer', '同行');
INSERT INTO `gy_history` VALUES (472, 'book', '书');
INSERT INTO `gy_history` VALUES (473, 'book', '本');
INSERT INTO `gy_history` VALUES (474, 'book', '?');
INSERT INTO `gy_history` VALUES (475, '可恶', '畜生');
INSERT INTO `gy_history` VALUES (476, '好的', 'はい');
INSERT INTO `gy_history` VALUES (477, '你好', 'hello');

-- ----------------------------
-- Table structure for gy_newwords
-- ----------------------------
DROP TABLE IF EXISTS `gy_newwords`;
CREATE TABLE `gy_newwords`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '生词',
  `mean` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '释义',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 220 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of gy_newwords
-- ----------------------------
INSERT INTO `gy_newwords` VALUES (184, 'seaman', '水手');
INSERT INTO `gy_newwords` VALUES (185, 'appointment', '任命');
INSERT INTO `gy_newwords` VALUES (186, 'basketball', '篮球');
INSERT INTO `gy_newwords` VALUES (187, 'unite', 'unite');
INSERT INTO `gy_newwords` VALUES (188, 'dance', '跳舞');
INSERT INTO `gy_newwords` VALUES (189, 'carrier', '航空公司');
INSERT INTO `gy_newwords` VALUES (190, 'employment', '就业');
INSERT INTO `gy_newwords` VALUES (191, 'ad', '的');
INSERT INTO `gy_newwords` VALUES (193, 'tour', '之旅');
INSERT INTO `gy_newwords` VALUES (194, 'manual', '手册');
INSERT INTO `gy_newwords` VALUES (196, 'world-wide', '全球范围内');
INSERT INTO `gy_newwords` VALUES (197, 'convenience', '方便');
INSERT INTO `gy_newwords` VALUES (198, 'settlement', '结算');
INSERT INTO `gy_newwords` VALUES (199, 'concept', '概念');
INSERT INTO `gy_newwords` VALUES (201, 'coin', '硬币');
INSERT INTO `gy_newwords` VALUES (202, 'squirrel', '松鼠');
INSERT INTO `gy_newwords` VALUES (203, 'past', '过去的');
INSERT INTO `gy_newwords` VALUES (204, 'recognize', '识别');
INSERT INTO `gy_newwords` VALUES (205, 'so', '所以');
INSERT INTO `gy_newwords` VALUES (206, 'cave', '洞穴');
INSERT INTO `gy_newwords` VALUES (207, 'pinch', '捏');
INSERT INTO `gy_newwords` VALUES (208, 'moderate', '温和的');
INSERT INTO `gy_newwords` VALUES (209, 'concentration', '浓度');
INSERT INTO `gy_newwords` VALUES (210, 'reign', '统治');
INSERT INTO `gy_newwords` VALUES (213, 'when', '当');
INSERT INTO `gy_newwords` VALUES (214, 'apple', '苹果');
INSERT INTO `gy_newwords` VALUES (216, 'banana', '香蕉');
INSERT INTO `gy_newwords` VALUES (219, 'peer', '同行');

-- ----------------------------
-- Table structure for gy_witticisms
-- ----------------------------
DROP TABLE IF EXISTS `gy_witticisms`;
CREATE TABLE `gy_witticisms`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `times` int(11) NULL DEFAULT NULL COMMENT '展示次数',
  `w_En` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名言_英文',
  `w_Ch` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名言_汉语',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 52 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of gy_witticisms
-- ----------------------------
INSERT INTO `gy_witticisms` VALUES (1, 0, 'Life is short and you deserve to be happy.', '生命苦短，你应该过得开心些');
INSERT INTO `gy_witticisms` VALUES (2, 0, 'You cannot change what you refuse to confront.', '你不去面对又怎么能去改变呢');
INSERT INTO `gy_witticisms` VALUES (3, 0, 'If you are passionate about something, pursue it, no matter what anyone else thinks. That\'s how dreams are achieved.', '如果你想要什么，那就勇敢地去追求，不要管别人是怎么想的，因为这就是实现梦想的方式');
INSERT INTO `gy_witticisms` VALUES (4, 0, 'Life isn\'t about waiting for the storm to pass, it\'s about learning to dance in the rain.', '生活不是等待暴风雨过去，而是要学会在雨中跳舞');
INSERT INTO `gy_witticisms` VALUES (5, 0, 'The world is such small,it\'s like when you turn around,you don\'t know who you will see. The world is so big,as if when you turn around,you never know who will disappear.', '世界真的很小，好像一转身，就不知道会遇见谁;世界真的很大，好像一转身，就不知道谁会消失');
INSERT INTO `gy_witticisms` VALUES (6, 0, 'Never abandon an old friend. You will never find one who can take his place. Friendship is like wine, it gets better as it grows older.', '不要轻易放弃旧朋友, 因你不能找别人代替他, 友情就像酒，越旧越好');
INSERT INTO `gy_witticisms` VALUES (7, 0, 'Give up worrying about what others think of you. What they think isn\'t important. What is important is how you feel about yourself.', '不要为别人怎么看你而烦恼, 别人的看法并不重要，重要的\'是你怎么看待你自己');
INSERT INTO `gy_witticisms` VALUES (8, 0, 'You never know how strong you really are until being strong is the only choice you have.', '不到没有退路之时，你永远不会知道自己有多强大');
INSERT INTO `gy_witticisms` VALUES (9, 0, 'Some good friends become distant insensibly,even you do not know why.', '有些好朋友，真的是不知不觉就疏远了，你连原因都不知道是什么');
INSERT INTO `gy_witticisms` VALUES (10, 0, 'I\'m proud of my heart. It\'s been played, burned, and broken, but it still works.', '我为自己的心感到骄傲, 它曾受戏弄，曾经心焦，曾遭破碎，却依然鲜活跳动');
INSERT INTO `gy_witticisms` VALUES (11, 0, 'No matter how long the rain lasts, there will be a rainbow in the end. No matter how sad you may be, believe, that happiness is waiting.', '不管雨下多久，最终彩虹总会出现, 不管你有多难过，始终要相信，幸福就在不远处');
INSERT INTO `gy_witticisms` VALUES (12, 0, 'If we fell in love again I swear I\'d love you right.', '如果可以再相爱一次，我发誓一定用合适的方式来爱你');
INSERT INTO `gy_witticisms` VALUES (13, 0, 'Not pretend to be silent but have no strength to complain.', '不是假装沉默，只是无力诉说');
INSERT INTO `gy_witticisms` VALUES (14, 0, 'Any one thing, as long as be most willing to, always simple.', '任何一件事情，只要心甘情愿，总是能够变得简单');
INSERT INTO `gy_witticisms` VALUES (15, 0, 'I just miss once, but forget that we have not had their own.', '我只是怀念曾经，却忘记了我们都已不是曾经的自己');
INSERT INTO `gy_witticisms` VALUES (16, 0, 'Everyone has someone in their life that keeps them looking forward to the next day.', '每个人生命里都会有那么一个人，让自己期待新一天的到来');
INSERT INTO `gy_witticisms` VALUES (17, 0, 'The most qmainful distance, you are not with me but in my heart.', '最痛的距离，是你不在我身边却在我心里');
INSERT INTO `gy_witticisms` VALUES (18, 0, 'what a loveiy world it well be with you away.', '没有了你, 这个世界多么寂寞');
INSERT INTO `gy_witticisms` VALUES (19, 0, 'Because when young, with a total want of good in the future.', '只因那时年少，总把未来想的太好');
INSERT INTO `gy_witticisms` VALUES (20, 0, 'Disappear a memory. And leaving is unforgettable memories.', '消失的是记忆, 而留下的才是刻骨铭心的回忆');
INSERT INTO `gy_witticisms` VALUES (21, 0, 'If just like why inflated into love.', '如若只是喜欢何必夸大成爱');
INSERT INTO `gy_witticisms` VALUES (22, 0, 'When it has is lost, brave to give up.', '当拥有已经是失去，就勇敢的放弃');
INSERT INTO `gy_witticisms` VALUES (23, 0, 'Love makes all hard hearts gentle.', '爱情把一切冷酷之心变成温柔');
INSERT INTO `gy_witticisms` VALUES (24, 0, 'On one second still in love, the next moment we will accept separation.', '上一秒还在相爱的我们，下一秒却要接受分离');
INSERT INTO `gy_witticisms` VALUES (25, 0, 'It was raining heavily, whether or not we should choose to hide in the refuge.', '雨下的很大，我们是否该要选择躲在避风港里');
INSERT INTO `gy_witticisms` VALUES (26, 0, 'Love is a light that never dims.', '爱是一盏永不昏暗的明灯');
INSERT INTO `gy_witticisms` VALUES (27, 0, 'Time is not cruelty. Just for it we are too fragile.', '时光并不残忍, 只是对于它来说我们太脆弱');
INSERT INTO `gy_witticisms` VALUES (28, 0, 'Friendship often ends in love, but love, in friendship never.', '友谊常以爱情而结束;而爱情从不能以友谊而告终');
INSERT INTO `gy_witticisms` VALUES (29, 0, 'If I say leave me alone,actually I need you more than at any time.', '如果我说我想一个人静一静，其实我比任何时候都需要你');
INSERT INTO `gy_witticisms` VALUES (30, 0, 'I love you not for who you are, but for who I am before you.', '我爱你不是因为你是谁，而是我在你面前可以是谁');
INSERT INTO `gy_witticisms` VALUES (31, 0, 'I always love to see the traces of time squat down, like the line by line through my memory.', '我总是爱蹲下来看地上时光的痕迹，像一行一行蚂蚁穿越我的记忆 ');
INSERT INTO `gy_witticisms` VALUES (32, 0, ' Ants the worst way to miss someone is to be sitting right beside them knowing you can\'t have them.', '失去某人，最糟糕的莫过于，他近在身旁，却犹如远在天边');
INSERT INTO `gy_witticisms` VALUES (33, 0, 'I looked over to you in heaven, as you stare me with sorrow.', '我站在天堂向你俯身凝望，就像你凝望我一样略带忧伤');
INSERT INTO `gy_witticisms` VALUES (34, 0, 'Eternity is not a distance but a decision.', '永远不是一种距离，而是一种决定');
INSERT INTO `gy_witticisms` VALUES (35, 0, 'I\'m just a sunflower ,waiting for my only sunshine.', '我只是一朵向日葵，等待着属于我的唯一的阳光');
INSERT INTO `gy_witticisms` VALUES (36, 0, 'You can\'t change the past, but you can ruin the present by worrying about the future.', '你改变不了昨天，但如果你过于忧虑明天，将会毁了今天');
INSERT INTO `gy_witticisms` VALUES (37, 0, 'The worst feeling isn\'t being lonely; it\'s knowing you\'ll never be remembered by the person you\'ll never forget.', '最糟糕的感觉并不是孤独，而是你难以忘怀的那个人，彻底把你忘记了');
INSERT INTO `gy_witticisms` VALUES (38, 0, 'To be unknown but loved by just one is better than being known by many but loved by none.', '默默无闻，但被一人深爱，要好过声名显赫却没人去爱');
INSERT INTO `gy_witticisms` VALUES (39, 0, 'He misses her, but he missed her.', '错过只在一瞬，思念却是一世');
INSERT INTO `gy_witticisms` VALUES (40, 0, 'The art of being wise is the art of knowing what to overlook.', '智慧就是懂得该忽略什么的艺术');
INSERT INTO `gy_witticisms` VALUES (41, 0, 'Love is like an hourglass, with the heart filling up as the brain empties.', '爱情就像沙漏，心满了，脑子就空了');
INSERT INTO `gy_witticisms` VALUES (42, 0, 'Sometimes words cannot express the burden of our heart.', '有时候，心中所承受之重是无法用言语来表达的');
INSERT INTO `gy_witticisms` VALUES (43, 0, 'Happiness is when the desolated soul meets love.', '幸福是孤寂的灵魂遭遇爱的邂逅');
INSERT INTO `gy_witticisms` VALUES (44, 0, 'There\'s always that one song that brings back old memories.', '总有那么一首歌，让你陷入深深的回忆');
INSERT INTO `gy_witticisms` VALUES (45, 0, 'Love may fade with the season.But some friendships are year-round.', '爱情可能随着季节的变迁而消退，但友情会为你全年守候');
INSERT INTO `gy_witticisms` VALUES (46, 0, 'Don\'t cry because it is over, smile because it happened.', '不要因为结束而哭泣，微笑吧，为你的曾经拥有');
INSERT INTO `gy_witticisms` VALUES (47, 0, 'I have nothing but you.', '我除了你什么都没有');
INSERT INTO `gy_witticisms` VALUES (48, 0, 'One thorn of experience is worth a whole wilderness of warning.', '一次痛苦的经验抵得上千百次的告诫');
INSERT INTO `gy_witticisms` VALUES (49, 0, 'Throughout life, we rely on small groups of people for love, admiration, respect, moral support and help.', '整个一生， 我们都有赖于从一些人群中获得友爱、赏识、尊重、道义支持和帮助');
INSERT INTO `gy_witticisms` VALUES (50, 0, 'He that will not allow his friend to share the prize must not expect him to share the danger.', '不肯让朋友共享果实的人，不要指望朋友与他共患难');
INSERT INTO `gy_witticisms` VALUES (51, 0, 'A young idler, an old beggar.', '少壮不努力，老大徒伤悲');

-- ---------


SET FOREIGN_KEY_CHECKS = 1;
