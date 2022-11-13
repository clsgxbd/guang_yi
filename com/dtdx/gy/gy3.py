import sys
import requests, random, hashlib, json
import datetime
import time

from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QDesktopWidget, QComboBox,
                             QLineEdit, QTextEdit, QLabel, QMessageBox, )
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont


from pymysql import *
from pymysql.converters import escape_string

# 数据库连接配置
conn = connect(
    host='127.0.0.1',
    port=3305,
    user='root',
    password='root',
    database='guang_yi',
    charset='utf8'
)
# 定义对象
cursor = conn.cursor()


l = {
            '自动检测语言': 'AUTO',
            '中文': 'zh-CHS',
            '英文': 'en',
            '日语': 'ja',
            '韩语': 'ko',
            '法语': 'fr',
            '德语': 'de',
            '俄语': 'ru',
            '西班牙语': 'es',
            '葡萄牙语': 'pt',
            '意大利语': 'it',
            '越南语': 'vi',
            '印尼语': 'id',
            '阿拉伯语': 'ar',
            '荷兰语': 'nl',
            '泰语': 'th'
}


# QWidget 和 QMainWindow 的区别:
# QWidget运行后就只有一个“页面”,而QMainWindow运行后生成了一个“窗口”
# 光译  这个类里包含三个界面
class GuangYi(QWidget):

    def __init__(self,facenum=1): # 默认界面参数为 1 表示默认打开第一个界面
        super().__init__()
        self.facenum = facenum
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # 不删除_o的话在翻译部分文字会出错  比如 'bu'  但删除了 _o 又没办法正常切换语言
        # self.url = 'http://fanyi.youdao.com/translate'
        # 上面这行是网上的解决方案  把url设为 'http://fanyi.youdao.com/translate'  但我亲测 与 把之前的 '_o'去掉结果相同
        # 原文链接:  https: // blog.csdn.net / qq_44770178 / article / details / 112613422

        self.headers = {
            "Referer": "https://fanyi.youdao.com/",
            "Cookie": 'OUTFOX_SEARCH_USER_ID=-1124603977@10.108.162.139; JSESSIONID=aaamH0NjhkDAeAV9d28-x; OUTFOX_SEARCH_USER_ID_NCOO=1827884489.6445506; fanyi-ad-id=305426; fanyi-ad-closed=1; ___rl__test__cookies=1649216072438',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }
        self.data = {
            "i": '',
            "from": 'AUTO',
            "to": 'AUTO',
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": '',
            "sign": '',
            "lts": '',
            "bv": "a0d7903aeead729d96af5ac89c04d48e",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",
        }
        # 绘制界面
        if self.facenum == 1:
            self.initUI1()  # 绘制界面 1
            self.Button2.clicked.connect(lambda: self.Switchface2(1))  # 为主界面按钮 2 绑定事件
            self.Button3.clicked.connect(lambda: self.Switchface3(1))  # 为主界面按钮 3 绑定事件

            self.face2 = GuangYi(2)  # 创建子界面 2
            self.face2.Button1.clicked.connect(lambda: self.Switchface1(2))  # 为子界面 2 按钮 1 绑定事件
            self.face2.Button3.clicked.connect(lambda: self.Switchface3(2))  # 为子界面 2 按钮 3 绑定事件


            self.face3 = GuangYi(3)  # 创建子界面 3
            self.face3.Button1.clicked.connect(lambda: self.Switchface1(3))  # 为子界面 3 按钮 1 绑定事件
            self.face3.Button2.clicked.connect(lambda: self.Switchface2(3))  # 为子界面 3 按钮 2 绑定事件


        elif self.facenum == 2:
            self.initUI2()  # 绘制界面 2
        elif self.facenum == 3:
            self.initUI3()  # 绘制界面 3
        else:
            self.initUI1()  # 绘制界面 1


    # 绘制界面 1
    def initUI1(self):

        # self.setToolTip(' 光 译 ! ')    # 提示
        # 插入背景图片
        window_pale = QPalette()
        window_pale.setBrush(self.backgroundRole(), QBrush(QPixmap("img/beijing.png")))
        self.setPalette(window_pale)
        self.setVisible(True)
        # 新建水平布局
        hbox = QHBoxLayout()
        # 添加左边
        hbox.addLayout(self.left())
        hbox.addSpacing(20)

        # 添加右边
        hbox.addLayout(self.right1())    # 词典


        # hbox.addLayout(self.right2())   # 翻译
        # # 左边选项切切换到按钮2
        # self.Button1.setStyleSheet(self.noxuan)  # 按钮 2选中
        # self.Button2.setStyleSheet(self.xuan)   # 按钮 1补选中


        self.setLayout(hbox)

        # self.resize(820, 600)   # 可调整窗口大小
        self.setFixedSize(820, 600)   # 固定的窗口大小
        self.center()   # 窗口居中显示

        # 设置窗口句柄
        self.setWindowTitle('光译')
        # 设置图标
        self.setWindowIcon(QIcon('img/tubiao.png'))

        # self.setVisible(True)   # 设置界面可见性
        # self.show()

    # 绘制界面 2
    def initUI2(self):
        # self.face1 = GuangYi(1)
        # self.face3 = GuangYi(3)
        # self.setToolTip(' 光 译 ! ')    # 提示
        # 插入背景图片
        window_pale = QPalette()
        window_pale.setBrush(self.backgroundRole(), QBrush(QPixmap("img/beijing.png")))
        self.setPalette(window_pale)

        # 新建水平布局
        hbox = QHBoxLayout()
        # 添加左边
        hbox.addLayout(self.left())
        hbox.addSpacing(20)

        # 添加右边
        # hbox.addLayout(self.right1())    # 词典

        hbox.addLayout(self.right2())   # 翻译
        # 左边选项切切换到按钮2
        self.Button1.setStyleSheet(self.noxuan)  # 按钮 1补选中
        self.Button2.setStyleSheet(self.xuan)   # 按钮 2选中


        self.setLayout(hbox)

        # self.resize(820, 600)   # 可调整窗口大小
        self.setFixedSize(820, 600)   # 固定的窗口大小
        # 调整窗口位置
        # self.center()   # 窗口居中显示

        # 设置窗口句柄
        self.setWindowTitle('光译')
        # 设置图标
        self.setWindowIcon(QIcon('img/tubiao.png'))

        # self.setVisible(True)   # 设置界面可见性
        # self.show()


    # 绘制界面 3
    def initUI3(self):
        # self.setToolTip(' 光 译 ! ')    # 提示
        # 插入背景图片
        window_pale = QPalette()
        window_pale.setBrush(self.backgroundRole(), QBrush(QPixmap("img/beijing.png")))
        self.setPalette(window_pale)

        # 新建水平布局
        hbox = QHBoxLayout()
        # 添加左边
        hbox.addLayout(self.left())
        hbox.addSpacing(20)

        # 添加右边
        hbox.addLayout(self.right3())  # 翻译
        # 左边选项切切换到按钮2
        self.Button1.setStyleSheet(self.noxuan)  # 按钮 1补选中
        self.Button3.setStyleSheet(self.xuan)  # 按钮 3 选中

        self.setLayout(hbox)

        # self.resize(820, 600)   # 可调整窗口大小
        self.setFixedSize(820, 600)  # 固定的窗口大小
        # self.center()  # 窗口居中显示

        # 设置窗口句柄
        self.setWindowTitle('光译')
        # 设置图标
        self.setWindowIcon(QIcon('img/tubiao.png'))

        # self.setVisible(True)   # 设置界面可见性
        # self.show()


    # 左边
    def left(self):
        self.xuan = '''QPushButton{background:#f8d92a;}QPushButton:hover{background:#f8d92a;}'''
        self.noxuan = '''QPushButton{background:#bfbfbf;}QPushButton:hover{background:#f8d92a;}'''

        self.Button1 = QPushButton("")    # 创建按钮 1
        # self.Button1 = QPushButton("词典")
        # self.Button1.setFont(QFont("等线", 20))
        # self.Button1.setToolTip('词典')
        self.Button1.setIcon(QIcon('img/词典.png'))
        self.Button1.setIconSize(QSize(142, 81))
        self.Button1.setFixedSize(140, 80)
        self.Button1.setStyleSheet(self.xuan)
        # self.Button1.clicked.connect(self.Switchface1)   # 为按钮绑定事件


        self.Button2 = QPushButton("")    # 创建按钮 2
        # self.Button2.setToolTip('翻译')
        self.Button2.setIcon(QIcon('img/翻译.png'))
        self.Button2.setIconSize(QSize(156, 120))
        self.Button2.setFixedSize(140, 80)
        self.Button2.setStyleSheet(self.noxuan)
        # self.Button2.clicked.connect(self.Switchface2)   # 为按钮绑定事件

        label_x = QLabel("- - - - - - - - - - - -")     # 创建下划线

        self.Button3 = QPushButton("")    # 创建按钮 3
        # self.Button3.setToolTip('单词本')
        self.Button3.setIcon(QIcon('img/生词本.png'))
        self.Button3.setIconSize(QSize(145, 120))
        self.Button3.setFixedSize(140, 80)
        self.Button3.setStyleSheet(self.noxuan)
        # self.Button3.clicked.connect(self.Switchface3)   # 为按钮绑定事件

        lab1 = QLabel(self)        # 设置图片显示label
        lab1.setToolTip('设置')     #提示
        lab1.setFixedSize(30, 30)  # 设置图片大小
        # lab1.setStyleSheet("QLabel{background:#F2F2F2;}")  # 设置labe1底色
        showImage = QPixmap('img/设置.png').scaled(lab1.width(), lab1.height())  # 适应窗口大小
        lab1.setPixmap(showImage)  # 显示图片
        lab1.setStyleSheet('''QLabel{background:#bfbfbf;}QLabel:hover{background:#f8d92a;}''')

        vboxLeft = QVBoxLayout()
        vboxLeft.addSpacing(200)
        vboxLeft.addWidget(self.Button1)    # 添加词典按钮
        vboxLeft.addSpacing(0)
        vboxLeft.addWidget(self.Button2)    # 添加翻译按钮
        vboxLeft.addSpacing(15)
        vboxLeft.addWidget(label_x)    # 添加下划线标签
        vboxLeft.addSpacing(35)
        vboxLeft.addWidget(self.Button3)    # 添加单词本按钮
        vboxLeft.addSpacing(80)
        vboxLeft.addWidget(lab1)    # 添加单设置按钮

        return vboxLeft


    # 词典 右边
    def right1(self):

        vboxRight = QVBoxLayout()   # 创建垂直总布局

        vboxRight.addSpacing(7)     # 上边距

        # ---创建水平分布局 1
        hbox1 = self.select_language()  # 选择语言
        # 水平分布局 1 创建完毕 ---

        # ---创建水平分布局 2
        hbox2 =  QHBoxLayout()

        self.wordInput = QLineEdit()    # 创建单行文本输入框  查询框
        self.wordInput.setFont(QFont("黑体", 20))
        self.wordInput.setToolTip('输入要翻译的单词')  # 提示
        self.wordInput.setStyleSheet("QLineEdit{background:#f7f8fa;}")  # 设置文本框底色

        buttonLs = QPushButton("∨", self)  # 创建‘历史记录’按钮
        buttonLs.setFixedSize(30, 36)

        buttonCx = QPushButton("查询", self)  # 创建‘查询’按钮
        buttonCx.setFont(QFont("黑体", 15))
        buttonCx.setFixedSize(80, 36)
        buttonCx.setStyleSheet('''QPushButton{background:#fffb2b;}QPushButton:hover{background:#f0f02b;}''')

        hbox2.addWidget(self.wordInput)  # 水平分布局 添加 文本输入框
        hbox2.addWidget(buttonLs)  # 水平分布局 添加 ‘历史记录’’按钮
        hbox2.addWidget(buttonCx)  # 水平分布局 添加 ‘查询’按钮
        hbox2.addSpacing(200)  # 边距
        # 水平分布局 2 创建完毕---

        # 创建文本输入框  结果框
        self.wordMean = QTextEdit()
        # self.wordMean.setStyleSheet("QTextEdit{background:#ffffff;}")  # 设置文本框底色
        self.wordMean.setStyleSheet("border:none;")     # 隐藏边框
        self.wordMean.setFont(QFont("楷体", 15))
        witticisms_id = random.randrange(1, 52)  # 随机生成 1-51 之间的数字  因为数据库里只有51条名言
        cursor.execute("select w_En,w_Ch from gy_witticisms where id=%d;" % witticisms_id)
        witticism = cursor.fetchall()
        i = datetime.datetime.now()  # 获取当前的日期
        gy_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        # 每日一句
        self.wordMean.append("\n\n\n\n\n ")
        self.wordMean.append(" <font size=80 face='Maiandra GD'> %s</font><font face='Maiandra GD'>%s</font>  每日一句! "
                             % (str(i.day), gy_month[i.month]))  # 日期
        self.wordMean.append(" <font size=4 face=楷体>%s</font>" % witticism[0][0])  # 名句
        self.wordMean.append(" <font size=3 face=华文楷体>%s</font> 。" % witticism[0][1])  # 名句


        # ---创建水平分布局 3
        hbox3 = QHBoxLayout()

        buttonTsc = QPushButton("+", self)  # 创建‘添加到生词本’按钮
        buttonTsc.setToolTip('添加到生词本')    # 提示
        buttonTsc.setFont(QFont("黑体", 30))
        buttonTsc.setFixedSize(40, 40)

        self.de_num = QLineEdit()    # 创建单行文本输入框 删除索引框
        self.de_num.setToolTip('输入要删除的序号')  # 提示
        self.de_num.setFont(QFont("黑体",12 ))

        buttonDe = QPushButton("删除一条记录", self)  # 创建‘删除’按钮
        buttonDe.setToolTip('删除一条记录')    # 提示
        # buttonDe.setFont(QFont("黑体", 15))
        buttonDe.setFixedSize(90, 20)

        buttonQk = QPushButton("清空记录", self)  # 创建‘清空’按钮
        buttonQk.setToolTip('清空搜索记录')    # 提示
        # buttonQk.setFont(QFont("黑体", 15))
        buttonQk.setFixedSize(60, 20)

        buttonFh = QPushButton("返回", self)  # 创建‘返回’按钮
        buttonFh.setToolTip('返回主界面')    # 提示
        buttonFh.setFont(QFont("黑体", 10))
        buttonFh.setFixedSize(82, 39)

        hbox3.addWidget(buttonTsc)  # 水平分布局 添加 ‘添加到生词本’按钮
        hbox3.addSpacing(30)        # 间距
        hbox3.addWidget(self.de_num)  # 水平分布局 添加 删除索引框
        hbox3.addWidget(buttonDe)  # 水平分布局 添加 删除按钮
        hbox3.addWidget(buttonQk)  # 水平分布局 添加 清空按钮
        hbox3.addSpacing(250)  # 间距
        hbox3.addWidget(buttonFh)  # 水平分布局 添加 ‘返回’按钮
        hbox3.addSpacing(20)        # 间距
        # ---水平分布局 3 创建完成

        vboxRight.addLayout(hbox1)  # 垂直总布局 添加 水平分布局 1
        vboxRight.addSpacing(20)        # 间距
        vboxRight.addLayout(hbox2)  # 垂直总布局 添加 水平分布局 2
        vboxRight.addSpacing(15)        # 间距
        vboxRight.addWidget(self.wordMean)  # 垂直总布局 添加 文本框
        vboxRight.addSpacing(5)        # 间距
        vboxRight.addLayout(hbox3)  # 垂直总布局 添加 水平分布局 3
        vboxRight.addSpacing(10)        # 下边距 10


        # 返回按钮事件
        def buttonFhClicked():
            self.wordInput.clear()  # 清空搜索框
            self.wordMean.clear()  # 清空结果框
            witticisms_id = random.randrange(1, 52)  # 随机生成 1-51 之间的数字  因为数据库里只有51条名言
            cursor.execute("select w_En,w_Ch from gy_witticisms where id=%d;" % witticisms_id)

            witticism = cursor.fetchall()
            i = datetime.datetime.now()  # 获取当前的日期
            gy_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

            self.wordMean.append("\n\n\n\n\n ")

            self.wordMean.append(" <font size=80 face='Maiandra GD'> %s</font><font face='Maiandra GD'>%s</font>  每日一句! "
                                 % (str(i.day), gy_month[i.month]))  # 日期
            self.wordMean.append(" <font size=4 face=楷体>%s</font>" % witticism[0][0])  # 名句
            self.wordMean.append(" <font size=3 face=华文楷体>%s</font> 。" % witticism[0][1])  # 名句




        buttonFh.clicked.connect(buttonFhClicked)  # 给查询按钮绑定事件



        # 查询按钮单击事件
        def buttonCxClicked():

            self.wordMean.clear()  # 清空结果框
            i1 = self.wordInput.text()
            if i1 !='':     # 文本框里有内容才开始翻译


                # 解决输入回车后,回车后面的不翻译
                # 输入 。.!！；; 后面的也不翻译

                stST = [['\n', '。', '.', '!', '！', '；', ';'],
                        ['@ # % ^ &', '% @ % ^ &', '# # @ ^ &', '& # % ^ %', '^ # % ^ @', '* # % # &', '^ # # ^ &'],
                        ['@', '%', '#', '&', '^', '*', '+']]

                i2 = ''
                for n in range(len(i1)):
                    if i1[n] in stST[0]:
                        i2 += (' ' + stST[1][(stST[0].index(i1[n]))] + ' ')
                    else:
                        i2 += i1[n]

                self.data['i'] = i2
                self.data['lts'] = str(int(time.time() * 1000))
                self.data['salt'] = self.data['lts'] + str(random.randint(0, 9))
                self.sign_str = 'fanyideskweb' + self.data['i'] + self.data['salt'] + 'Ygy_4c=r#e#4EX^NUGUc5'
                self.m = hashlib.md5()
                self.m.update(self.sign_str.encode())
                self.data['sign'] = self.m.hexdigest()

                res = requests.post(self.url, headers=self.headers, data=self.data)
                # 发送
                response = json.loads(res.text)

                # 接收网页返回的数据 进行数据清洗
                # 因为有部分字符串无法翻译, 比如 翻译'bu' 返回结果为 {'errorCode': 40}
                # 所以这里判断一下有没有出错

                if response['errorCode'] != 0:
                    value = i1
                else:
                    value = response['translateResult'][0][0]['tgt']

                # 解决输入回车后,回车后面的不翻译
                # 输入 。.!！；; 后面的也不翻译

                value2 = ''
                n = 0
                while (n < len(value)):
                    if value[n] in stST[2] and value[n:n + 9] in stST[1]:
                        value2 += stST[0][(stST[2].index(value[n]))]
                        n += 9
                        if n >= len(value):
                            break
                        elif value[n] == ' ':
                            n += 1
                        continue
                    else:
                        value2 += value[n]
                    n += 1

                # 输出数据
                self.wordMean.append("  <b><font face=黑体 size=10>%s</font></b>" % i1)
                self.wordMean.append(" ")
                self.wordMean.append("  <u><font face=宋体 size=3><b>%s</b>%s</font></u>"
                                     % ('简明', '      新汉英      现代汉语      例句      百科'))
                self.wordMean.append(" ")
                self.wordMean.append(" <b><font face=黑体 size=3 color=#2b77c5>%s</font></b>" % value2)
                self.wordMean.append("\n\n ")
                self.wordMean.append("  <font face=宋体  size=3><b><u>%s</u></b></font>%s"
                                     % (' 网络释义', '______________________________________________'))
                self.wordMean.append("<font face=等线 size=2>>***</font>")
                self.wordMean.append("<font face=等线 size=2>>***</font>")
                self.wordMean.append(" ")
                self.wordMean.append("<font face=等线 size=2>%s</font>" % ' 短语')
                self.wordMean.append("<font face=等线 size=2>1.**********</font>")
                self.wordMean.append("<font face=等线 size=2>2.**********</font>")
                self.wordMean.append("<font face=等线 size=2>3.**********</font>")
                # escape_str(i)
                # 自动添加到数据库,历史记录表
                # 先查一下历史记录表有没有该单词 没有则添加  有则删除原来的然后添加
                isins = cursor.execute("select word,mean from gy_history where word='%s' and mean='%s'"
                                       % (escape_string(i1), escape_string(value2)))
                if isins != 0:
                    print('历史记录中有该数据！')
                    cursor.execute("delete from gy_history where word='%s' and mean='%s'"
                                        % (escape_string(i1), escape_string(value2)))
                    conn.commit()
                    print("已经删除它!")
                cursor.execute("insert into gy_history values(default, '%s', '%s');" %
                               (escape_string(i1), escape_string(value2)))
                conn.commit()   # 提交
                print("重新加入历史记录！")


        buttonCx.clicked.connect(buttonCxClicked)   # 给查询按钮绑定事件


        # “添加到生词本” 按钮单击事件
        def buttonTscClicked():
            if self.wordInput.text() != '':
                cursor.execute("select word,mean from gy_history where id=(select max(id) from gy_history);")
                wm = cursor.fetchall()
                word = wm[0][0]
                mean = wm[0][1]
                # 先查一下生词表有没有该单词 没有则可以添加
                isins = cursor.execute("select word,mean from gy_newwords where word='%s' and mean='%s';"
                                       % (escape_string(word), escape_string(mean)))
                if isins == 0:
                    # cursor.execute("insert into gy_newwords(word,mean) values('%s','%s')" % (word, mean))
                    cursor.execute("insert into gy_newwords values(default, '%s', '%s');" %
                                   (escape_string(word), escape_string(mean)))
                    conn.commit()
                    print('成功添加到生词本！')

                    # # 重置页码显示:
                    if self.face3.numOfNewWords != 0 and self.face3.numOfNewWords % 14 == 0:  # 当前数量刚好能被整除
                        self.face3.totalP += 1
                    self.face3.this_total_Edit.clear()
                    self.face3.this_total_Edit.setText("%d/%d" % (self.face3.thisP, self.face3.totalP))  # 显示当前页码/共有几页  默认为显示第一页
                    self.face3.numOfNewWords += 1  # 生词数量+1
                    self.face3.numberOfWordsEdit.clear()
                    self.face3.numberOfWordsEdit.append(
                        "<font color=#68696a>共有 %d 个生词</font>" % self.face3.numOfNewWords)  # 显示生词数量
                    self.face3.showNewWords()  # 显示 生词本中的数据在界面上
                else:
                    print('该单词已存在！')

        buttonTsc.clicked.connect(buttonTscClicked)   # 给'添加到生词本'按钮绑定事件


        # 历史记录 “∨” 按钮单击事件
        def buttonLsClicked():
            self.wordMean.clear()  # 清空结果框
            ls_num = cursor.execute("select word,mean from gy_history ;")
            ls = cursor.fetchall()
            if ls_num == 0:
                self.wordMean.append(" <span><pre>                 <font size=2> 当前无历史记录 !!! </font></pre></span>")
            else:
                for i in range(ls_num):
                    self.wordMean.append(" <pre>                 <font size=2 color=#adadad>%-2d.</font><font size=2><b>%s</b><font size=2>  \t<font size=2 color=#68696a>%s</font></pre>"
                                         % (i + 1, ls[i][0], ls[i][1]))
        buttonLs.clicked.connect(buttonLsClicked)  # 给'历史记录 “∨” 按钮绑定事件


        # 删除按钮buttonDe单击事件
        def buttonDeClicked():
            if self.de_num.text() != '':
                num = int(self.de_num.text()) - 1
                cursor.execute("select id from gy_history ;")
                ids = cursor.fetchall()
                id = ids[num][0]
                cursor.execute("delete from gy_history where id=%d ;" % id)
                conn.commit()
                buttonLsClicked()   # 调用历史记录 “∨” 按钮单击事件
        buttonDe.clicked.connect(buttonDeClicked)  # 给删除按钮buttonDe绑定事件

        # 清空按钮buttonQk单击事件
        def buttonQkClicked():
            # 创建 询问清空 对象
            messageBox = QMessageBox(QMessageBox.Question, "清空历史记录", "确定要清空历史记录吗 ?")
            messageBox.setWindowIcon(QtGui.QIcon('img/tubiao.png'))
            messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            messageBox.button(QMessageBox.Yes).setText('确定')  # 修改 'Yes' 按钮为 '确定'
            messageBox.button(QMessageBox.No).setText('取消')  # 修改 'No' 按钮为 '取消'
            messageBox.exec_()
            if messageBox.clickedButton() == messageBox.button(QMessageBox.Yes):
                print('确定清空历史记录')
                cursor.execute("delete from gy_history;")  # 清空数据库中的 历史记录表
                conn.commit()  # 提交
                buttonLsClicked()  # 调用历史记录 “∨” 按钮单击事件
            else:
                print('取消清空历史记录')
        buttonQk.clicked.connect(buttonQkClicked)  # 给清空按钮buttonQk绑定事件

        return vboxRight


    # 翻译 右边
    def right2(self):

        vboxRight = QVBoxLayout()   # 创建垂直总布局

        vboxRight.addSpacing(7)     # 上边距

        # ---创建水平分布局
        hbox1 = self.select_language()  # 选择语言
        # 水平分布局 1 创建完毕 ---

        # 创建标签 1
        label1 = QLabel(" 翻译内容")  # 标签 1
        label1.setFont(QFont("黑体", 12))

        # 创建文本输入框 1
        self.txtInput1 = QTextEdit()
        self.txtInput1.setToolTip('输入要翻译的内容')    # 提示
        self.txtInput1.setFont(QFont("黑体", 15))
        self.txtInput1.setStyleSheet("QTextEdit{background:#f7f8fa;}")  # 设置文本框底色
        # ---创建水平分布局 2
        hbox2 = QHBoxLayout()

        label2 = QLabel(" 翻译结果")    # 创建标签2
        label2.setFont(QFont("黑体", 12))

        buttonf = QPushButton("翻译", self)    # 创建‘翻译’按钮
        buttonf.setFixedSize(100, 25)
        buttonf.setStyleSheet('''QPushButton{background:#fffb2b;}QPushButton:hover{background:#f0f02b;}''')

        hbox2.addWidget(label2)         # 水平分布局 添加 标签 2
        hbox2.addSpacing(400)           # 间距 400
        hbox2.addWidget(buttonf)        # 水平分布局 添加 标签 2
        hbox2.addSpacing(12)            # 间距 12
        # 水平分布局 2 创建完毕---

        # 创建文本输入框 2
        self.textEdit2 = QTextEdit()
        self.textEdit2.setToolTip('翻译结果')    # 提示
        self.textEdit2.setFont(QFont("黑体", 15))
        self.textEdit2.setStyleSheet("QTextEdit{background:#f7f8fa;}")  # 设置文本框底色

        vboxRight.addLayout(hbox1)      # 垂直总布局 添加 水平分布局 1
        vboxRight.addSpacing(15)        # 间距 15
        vboxRight.addWidget(label1)     # 垂直总布局 添加 标签 1
        # vboxRight.addSpacing(0)        # 间距 0
        vboxRight.addWidget(self.txtInput1)  # 垂直总布局 添加 文本输入框 1
        # vboxRight.addSpacing(0)

        vboxRight.addLayout(hbox2)      # 垂直总布局 添加 水平分布局 2
        vboxRight.addWidget(self.textEdit2)  # 垂直总布局 添加 文本输入框 2
        vboxRight.addSpacing(10)        # 下边距 10


        # 翻译按钮单击事件
        def buttonfClicked():

            self.textEdit2.clear()  # 清空结果框
            i1 = self.txtInput1.toPlainText()
            if i1 != '':
                # 解决输入回车后,回车后面的不翻译
                # 输入 。.!！；; 后面的也不翻译

                stST = [['\n', '。', '.', '!', '！', '；', ';'],
                        ['@ # % ^ &', '% @ % ^ &', '# # @ ^ &', '& # % ^ %', '^ # % ^ @', '* # % # &', '^ # # ^ &'],
                        ['@', '%', '#', '&', '^', '*', '+' ]]


                i2 = ''
                for n in range(len(i1)):
                    if i1[n] in stST[0]:
                        i2 += (' ' + stST[1][(stST[0].index(i1[n]))] + ' ')
                    else:
                        i2 += i1[n]

                self.data['i'] = i2
                self.data['lts'] = str(int(time.time() * 1000))
                self.data['salt'] = self.data['lts'] + str(random.randint(0, 9))
                self.sign_str = 'fanyideskweb' + self.data['i'] + self.data['salt'] + 'Ygy_4c=r#e#4EX^NUGUc5'
                self.m = hashlib.md5()
                self.m.update(self.sign_str.encode())
                self.data['sign'] = self.m.hexdigest()

                res = requests.post(self.url, headers=self.headers, data=self.data)
                # 发送
                response = json.loads(res.text)

                # 接收网页返回的数据 进行数据清洗
                # 因为有部分字符串无法翻译, 比如 翻译'bu' 返回结果为 {'errorCode': 40}
                # 所以这里判断一下有没有出错
                if response['errorCode'] != 0:
                    value = i1
                else:
                    value = response['translateResult'][0][0]['tgt']

                # 解决输入回车后,回车后面的不翻译
                # 输入 。.!！；; 后面的也不翻译
                value2 = ''
                n = 0
                while(n<len(value)):
                    if value[n] in stST[2] and value[n:n+9] in stST[1]:
                        value2 += stST[0][(stST[2].index(value[n]))]
                        n += 9
                        if n >= len(value):
                            break
                        elif value[n] == ' ':
                            n += 1
                        continue
                    else:
                        value2 += value[n]
                    n += 1
                # 输出数据
                self.textEdit2.append(value2)
        buttonf.clicked.connect(buttonfClicked)

        return vboxRight

    #单词本 右边
    def right3(self):
        vboxRight = QVBoxLayout()  # 创建垂直总布局

        vboxRight.addSpacing(7)  # 上边距


        # ---创建水平分布局 1
        hbox1 = QHBoxLayout()
        hbox1.addSpacing(20)  # 左距
        self.newwordInput = QLineEdit()  # 创建单行文本输入框  查新单词是否存在
        self.newwordInput.setFont(QFont("黑体", 15))
        self.newwordInput.setToolTip('输入要查找的单词')  # 提示
        self.newwordInput.setStyleSheet("QLineEdit{background:#f7f8fa;}")  # 设置文本框底色

        buttonNcx = QPushButton("🔍", self)  # 创建‘查新单词’按钮
        buttonNcx.setToolTip('查找生词表中的单词')  # 提示
        buttonNcx.setFixedSize(25, 25)

        buttonS = QPushButton("<", self)  # 创建‘上一页’按钮
        buttonS.setToolTip('上一页')  # 提示
        buttonS.setFixedSize(25, 25)


        self.this_total_Edit = QLineEdit()  # "当前页码/共有几页" 文本框
        self.this_total_Edit.setFont(QFont("黑体", 10))
        self.this_total_Edit.setFixedSize(25, 25)
        self.this_total_Edit.setStyleSheet("border:none;")  # 隐藏边框
        self.thisP = 1  # 当前页码 1
        self.numOfNewWords = cursor.execute("select * from gy_newwords ;")  # 查看数据库中有几条数据
        if self.numOfNewWords == 0:
            self.totalP = 1
        elif self.numOfNewWords % 14 == 0:
            self.totalP = int(self.numOfNewWords / 14) # 计算共有几页  是否被14整除 每一页14条记录
        else:
            self.totalP = int(self.numOfNewWords / 14) + 1
        self.this_total_Edit.setText("1/%d" % self.totalP)  # 显示当前页码/共有几页  默认为显示第一页
        buttonX = QPushButton(">", self)  # 创建‘下一页’按钮
        buttonX.setToolTip('下一页')  # 提示
        buttonX.setFixedSize(25, 25)
        buttonZl = QPushButton("👣整理", self)  # 创建‘整理’按钮
        buttonZl.setToolTip('整理生词表')  # 提示
        buttonZl.setFixedSize(60, 25)
        buttonFx = QPushButton("ლ复习", self)  # 创建‘复习生词表’按钮
        buttonFx.setToolTip('复习生词')  # 提示
        buttonFx.setFixedSize(60, 25)
        buttonQkNew = QPushButton("清空生词表", self)  # 创建‘清空’按钮
        buttonQkNew.setToolTip('清空生词表')    # 提示
        # buttonQk.setFont(QFont("黑体", 15))
        buttonQkNew.setFixedSize(80, 25)
        hbox1.addWidget(self.newwordInput)  # 水平分布局 添加 单行文本输入框
        # hbox1.addSpacing(0)  # 间距
        hbox1.addWidget(buttonNcx)  # 水平分布局 添加 ‘查新单词’按钮
        hbox1.addSpacing(50)  #边距
        hbox1.addWidget(buttonS)  # 水平分布局 添加 ‘上一页’按钮
        hbox1.addWidget(self.this_total_Edit)  # 水平分布局 添加 ‘当前页/总页数’文本框
        hbox1.addWidget(buttonX)  # 水平分布局 添加 ‘下一页’按钮
        hbox1.addSpacing(50)  #边距
        hbox1.addWidget(buttonZl)  # 水平分布局 添加 ‘整理’按钮
        hbox1.addWidget(buttonFx)  # 水平分布局 添加 ‘复习’按钮
        hbox1.addWidget(buttonQkNew)  # 水平分布局 添加 ‘清空生词本’按钮

        hbox1.addSpacing(20)  # 边距
        # 水平分布局 1 创建完毕---


        # ---创建垂直分布局 2
        newWordShows = QVBoxLayout()  # 创建垂直总布局
        newWordShows.addSpacing(10)  # 上边距

        # 生词布局
        words = {'1': '','2': '','3': '','4': '','5': '','6': '','7': '',
               '8': '','9': '','10': '','11': '','12': '','13': '','14': ''}
        # 生词
        self.showWords = {'1': '','2': '','3': '','4': '','5': '','6': '','7': '',
               '8': '','9': '','10': '','11': '','12': '','13': '','14': ''}
        # 释义
        self.showMeans = {'1': '','2': '','3': '','4': '','5': '','6': '','7': '',
               '8': '','9': '','10': '','11': '','12': '','13': '','14': ''}
        # 删除按钮 ✕
        de_shows = {'1': '','2': '','3': '','4': '','5': '','6': '','7': '',
               '8': '','9': '','10': '','11': '','12': '','13': '','14': ''}

        de_showsClickeds = {'1': '','2': '','3': '','4': '','5': '','6': '','7': '',
               '8': '','9': '','10': '','11': '','12': '','13': '','14': ''}


        self.idShowMean = True


        # 索引 按钮的事件
        def buttonNcxClickeds():
            thisWord = self.newwordInput.text()
            if thisWord != '' and self.numOfNewWords > 0:
                cursor.execute("select * from gy_newwords;")

                allWords = cursor.fetchall()
                for i in range(self.numOfNewWords):
                    if allWords[i][1] == thisWord:
                        if (i+1) % 14 == 0:
                            self.thisP = int((i+1)/14)
                        else:
                            self.thisP = int((i+1)/14 + 1)
                        self.this_total_Edit.setText("%d/%d" % (self.thisP, self.totalP))  # 显示 当前页码/共有几页
                        self.showNewWords()
                        break
        buttonNcx.clicked.connect(buttonNcxClickeds)  # 给'索引” 按钮绑定事件


        # 上一页按钮 绑定的事件
        def buttonSClickeds():
            if self.thisP > 1 and self.thisP <= self.totalP:
                self.thisP -= 1
                self.showNewWords()  # 显示 生词本中的数据在界面上
                self.this_total_Edit.clear()
                self.this_total_Edit.setText("%d/%d" % (self.thisP, self.totalP))  # # 重置页码显示

        buttonS.clicked.connect(buttonSClickeds)  # 给'上一页按钮” 按钮绑定事件


        # 下一页按钮 绑定的事件
        def buttonXClickeds():
            if self.thisP >= 1 and self.thisP < self.totalP:
                self.thisP += 1
                self.this_total_Edit.clear()
                self.this_total_Edit.setText("%d/%d" % (self.thisP, self.totalP))  # # 重置页码显示
                self.showNewWords()  # 显示 生词本中的数据在界面上
        buttonX.clicked.connect(buttonXClickeds)  # 给'上一页按钮” 按钮绑定事件

        def buttonFxClickeds():
            self.idShowMean = not self.idShowMean
            self.showNewWords()  # 显示 生词本中的数据在界面上
        buttonFx.clicked.connect(buttonFxClickeds)  # 给'复习” 按钮绑定事件

        # 清空生词表绑定的事件
        def buttonQkNewClickeds():
            # 创建 询问清空 对象
            messageBox = QMessageBox(QMessageBox.Question, "清空生词本", "确定要清空生词本吗 ?")
            messageBox.setWindowIcon(QtGui.QIcon('img/tubiao.png'))
            messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            messageBox.button(QMessageBox.Yes).setText('确定')  # 修改 'Yes' 按钮为 '确定'
            messageBox.button(QMessageBox.No).setText('取消')  # 修改 'No' 按钮为 '取消'
            messageBox.exec_()
            if messageBox.clickedButton() == messageBox.button(QMessageBox.Yes):
                cursor.execute("delete from gy_newwords;")
                conn.commit()
                self.showNewWords()        # 显示 生词本中的数据在界面上
                self.thisP = 1  # 当前页码改为 1
                self.totalP = 1 # 总页码改为 1
                self.numOfNewWords = 0  # 生词数量改为0
                self.this_total_Edit.clear()
                self.this_total_Edit.setText("1/1")  # 重新显示当前页码/共有几页 1/1
                self.numberOfWordsEdit.clear()
                self.numberOfWordsEdit.append("<font color=#68696a>共有 0 个生词</font>")  # 重新显示生词数量
            else:
                print('取消清空生词本')
        buttonQkNew.clicked.connect(buttonQkNewClickeds)  # 给'清空生词表” 按钮绑定事件

        # 删除生词按钮绑定的事件  num 为当前页面显示的序号
        def delete(num):
            de_num = (self.thisP - 1) * 14 + num  # 计算在生词表中第几条
            if de_num <= self.numOfNewWords:
                cursor.execute("select id from gy_newwords ;")
                de_id = cursor.fetchall()[de_num-1][0]    #得到 真实 id
                cursor.execute("delete from gy_newwords where id=%d;" % de_id)
                conn.commit()
                self.numOfNewWords -= 1 # 生词数量-1
                # # 重置页码显示:
                if self.numOfNewWords % 14 == 0:    # 删了一条刚好能被整除
                    if self.thisP == self.totalP:   #如果刚好在最后一页
                        self.thisP -= 1
                    self.totalP -= 1
                self.this_total_Edit.clear()
                self.this_total_Edit.setText("%d/%d" % (self.thisP, self.totalP))  # 显示当前页码/共有几页  默认为显示第一页
                self.numberOfWordsEdit.clear()
                self.numberOfWordsEdit.append("<font color=#68696a>共有 %d 个生词</font>" % self.numOfNewWords)  # 显示生词数量
                self.showNewWords()        # 显示 生词本中的数据在界面上

        def delete1():
            delete(1)
        def delete2():
            delete(2)
        def delete3():
            delete(3)
        def delete4():
            delete(4)
        def delete5():
            delete(5)
        def delete6():
            delete(6)
        def delete7():
            delete(7)
        def delete8():
            delete(8)
        def delete9():
            delete(9)
        def delete10():
            delete(10)
        def delete11():
            delete(11)
        def delete12():
            delete(12)
        def delete13():
            delete(13)
        def delete14():
            delete(14)
        de_showsClickeds['1'] = delete1
        de_showsClickeds['2'] = delete2
        de_showsClickeds['3'] = delete3
        de_showsClickeds['4'] = delete4
        de_showsClickeds['5'] = delete5
        de_showsClickeds['6'] = delete6
        de_showsClickeds['7'] = delete7
        de_showsClickeds['8'] = delete8
        de_showsClickeds['9'] = delete9
        de_showsClickeds['10'] = delete10
        de_showsClickeds['11'] = delete11
        de_showsClickeds['12'] = delete12
        de_showsClickeds['13'] = delete13
        de_showsClickeds['14'] = delete14

        for i in range(14):
            words[str(i + 1)] = QHBoxLayout()
            self.showWords[str(i+1)] = QLineEdit()  # 生词
            self.showWords[str(i+1)].setFont(QFont("黑体", 15))
            self.showWords[str(i+1)].setFixedSize(200, 25)
            self.showWords[str(i+1)].setStyleSheet("QLineEdit{background:#fbfcff;}")  # 设置文本框底色
            self.showMeans[str(i+1)] = QLineEdit()  # 生词
            self.showMeans[str(i+1)].setFont(QFont("黑体", 15))
            # self.showWord14.setFixedSize(200, 25)
            self.showMeans[str(i + 1)].setStyleSheet("QLineEdit{background:#fbfcff;}")  # 设置文本框底色
            de_shows[str(i+1)] = QPushButton("✕", self)  # 删除 生词14
            de_shows[str(i+1)].setToolTip('删除')  # 提示
            de_shows[str(i+1)].setFixedSize(25, 25)
            de_shows[str(i+1)].clicked.connect(de_showsClickeds[str(i + 1)])  # 给'历史记录 “✕” 按钮绑定事件
            words[str(i + 1)].addWidget(self.showWords[str(i+1)])  # 垂直分布局  添加 生词
            words[str(i + 1)].addWidget(self.showMeans[str(i+1)])  # 垂直分布局  添加 释义
            words[str(i + 1)].addWidget(de_shows[str(i+1)])  # 垂直分布局  添加 删除
            words[str(i + 1)].addSpacing(20)  # 右边距
            newWordShows.addLayout(words[str(i + 1)])  # 垂直分布局  添加 生词
        self.showNewWords()  # 显示 生词本中的数据在界面上
        # 垂直分布局 2 创建完毕---


        # ---创建水平分布局 3
        hbox3 = QHBoxLayout()
        self.numberOfWordsEdit = QTextEdit()  # 创建单行文本输入框  显示生词数量
        self.numberOfWordsEdit.setFixedSize(100, 23)
        self.numberOfWordsEdit.setStyleSheet("border:none;")    # 隐藏边框
        self.numberOfWordsEdit.append("<font color=#68696a>共有 %d 个生词</font>" % self.numOfNewWords)  #显示生词数量

        buttonLb = QPushButton("列表", self)  # 创建‘列表’按钮
        buttonLb.setFixedSize(40, 30)
        buttonKp = QPushButton("卡片", self)  # 创建‘卡片’按钮
        buttonKp.setFixedSize(40, 30)
        hbox3.addWidget(self.numberOfWordsEdit)  # 水平分布局 添加 单行文本输入框
        hbox3.addSpacing(500)  # 间距
        hbox3.addWidget(buttonLb)  # 水平分布局 添加 ‘列表’按钮
        hbox3.addWidget(buttonKp)  # 水平分布局 添加 ‘卡片’按钮
        hbox3.addSpacing(20)  # 右距
        # 水平分布局 3 创建完毕---

        vboxRight.addLayout(hbox1)  # 垂直总布局 添加 水平分布局 1
        vboxRight.addSpacing(15)  # 间距 15
        vboxRight.addLayout(newWordShows)  # 垂直总布局 添加 垂直分布局 2
        vboxRight.addSpacing(0)  # 间距 15
        vboxRight.addLayout(hbox3)  # 垂直总布局 添加 水平分布局 3

        return vboxRight


    # 显示 生词本中的数据在界面上
    def showNewWords(self):
        for i in range(14):
            self.showWords[str(i + 1)].clear()
            self.showMeans[str(i + 1)].clear()
        self.numOfNewWords = cursor.execute("select word,mean from gy_newwords ;")
        newWords = cursor.fetchall()
        if self.numOfNewWords != 0:
            # 给14行文本框 显示14条数据
            for i in range(14):
                if (self.thisP - 1) * 14 + i + 1 <= self.numOfNewWords:  # 数据存在 则输出
                    self.showWords[str(i + 1)].setText(
                        "%2d. %s" % ((self.thisP - 1) * 14 + i + 1, newWords[i + (self.thisP - 1) * 14][0]))
                    if self.idShowMean == False:  # 复习模式下不显示释义
                        self.showMeans[str(i + 1)].setText('')
                    else:  # 正常模式显示释义
                        self.showMeans[str(i + 1)].setText("%s" % newWords[i + (self.thisP - 1) * 14][1])
                else:  # 数据不存在 则补空格
                    self.showWords[str(i + 1)].setText("%2d. " % ((self.thisP - 1) * 4 + i + 1))
                    self.showMeans[str(i + 1)].setText('')


    # 共用模块 语言选择下拉列表 返回布局
    def select_language(self):
        # ---创建水平分布局 1
        hbox1 = QHBoxLayout()

        combo1 = QComboBox(self)  # 下拉菜单 1
        combo1.setToolTip('源语言')  # 提示 源语言
        combo1.addItem("自动检测语言")  # 自动    AUTO
        combo1.addItem("中文")  # 中文    zh-CHS
        combo1.addItem("英文")  # 英文    en
        combo1.addItem("日语")  # 日语    ja
        combo1.addItem("韩语")  # 日语    ja
        combo1.addItem("法语")  # 法语    fr
        combo1.addItem("德语")  # 德语    de
        combo1.addItem("俄语")  # 俄语    ru
        combo1.addItem("西班牙语")  # 西班牙语  es
        combo1.addItem("葡萄牙语")  # 葡萄牙语  pt
        combo1.addItem("意大利语")  # 意大利语  it
        combo1.addItem("越南语")  # 越南语   vi
        combo1.addItem("印尼语")  # 印尼语   id
        combo1.addItem("阿拉伯语")  # 阿拉伯语  ar
        combo1.addItem("荷兰语")  # 荷兰语   nl
        combo1.addItem("泰语")  # 泰语    th
        combo1.activated[str].connect(self.onActivated1)
        label_jt = QLabel("→")  # 标签 2
        label_jt.setFont(QFont("黑体", 16))

        combo2 = QComboBox(self)  # 下拉菜单 2
        combo2.setToolTip('目标语言')  # 提示 目标语言
        combo2.addItem("自动检测语言")  # 自动    AUTO
        combo2.addItem("中文")  # 中文    zh-CHS
        combo2.addItem("英文")  # 英文    en
        combo2.addItem("日语")  # 日语    ja
        combo2.addItem("韩语")  # 日语    ja
        combo2.addItem("法语")  # 法语    fr
        combo2.addItem("德语")  # 德语    de
        combo2.addItem("俄语")  # 俄语    ru
        combo2.addItem("西班牙语")  # 西班牙语  es
        combo2.addItem("葡萄牙语")  # 葡萄牙语  pt
        combo2.addItem("意大利语")  # 意大利语  it
        combo2.addItem("越南语")  # 越南语   vi
        combo2.addItem("印尼语")  # 印尼语   id
        combo2.addItem("阿拉伯语")  # 阿拉伯语  ar
        combo2.addItem("荷兰语")  # 荷兰语   nl
        combo2.addItem("泰语")  # 泰语    th
        combo2.activated[str].connect(self.onActivated2)

        hbox1.addWidget(combo1)  # 水平分布局 1 添加 下拉菜单 1
        # hbox1.addSpacing(0)       # 间距 0
        hbox1.addWidget(label_jt)  # 水平分布局 1 添加 箭头
        # hbox1.addSpacing(0)       # 间距 0
        hbox1.addWidget(combo2)  # 水平分布局 1 添加 下拉菜单 2
        hbox1.addSpacing(400)  # 右边距 400
        # 水平分布局 1 创建完毕 ---
        return hbox1

    # 下拉列表 1 事件
    def onActivated1(self, text):
        self.data['from'] = l[text]    # 改变源语言
    # 下拉列表 2 事件
    def onActivated2(self, text):
        self.data['to'] = l[text]      # 改变目标语言

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    # 左边按钮 1  '词典' 按钮绑定的事件
    def Switchface1(self, num):
        # if self.facenum != 1:
        #     self.setVisible(False)
        #     face1 = GuangYi(1)
        #     face1.setVisible(True)
        # 同步窗口位置
        if num == 2:
            self.move(self.face2.x(), self.face2.y())
        if num == 3:
            self.move(self.face3.x(), self.face3.y())
        self.setVisible(True)
        time.sleep(0.02)
        self.face2.setVisible(False)
        self.face3.setVisible(False)


    # 左边按钮 2  '翻译' 按钮绑定的事件
    def Switchface2(self, num):
        # if self.facenum != 2:
            # self.setVisible(False)
            # face2 = GuangYi(2)
            # face2.setVisible(True)
        # 同步窗口位置
        if num == 1:
            self.face2.move(self.x(), self.y())
        if num == 3:
            self.face2.move(self.face3.x(), self.face3.y())
        self.face2.setVisible(True)
        time.sleep(0.02)
        self.setVisible(False)
        self.face3.setVisible(False)


    # 左边按钮 3  '生词本' 按钮绑定的事件
    def Switchface3(self,num):
        # 同步窗口位置
        if num == 1:
            self.face3.move(self.x(), self.y())
        if num == 2:
            self.face3.move(self.face2.x(), self.face2.y())
        self.face3.setVisible(True)
        time.sleep(0.02)
        self.setVisible(False)
        self.face2.setVisible(False)


    # 右上角 退出叉号❌ 按钮绑定事件
    def closeEvent(self, event):
        # 创建 询问退出 对象
        messageBox = QMessageBox(QMessageBox.Question, "退出", "确定要退出吗 ?")
        messageBox.setWindowIcon(QtGui.QIcon('img/tubiao.png'))
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        messageBox.button(QMessageBox.Yes).setText('确定')  # 修改 'Yes' 按钮为 '确定'
        messageBox.button(QMessageBox.No).setText('取消')  # 修改 'No' 按钮为 '取消'
        messageBox.exec_()
        if messageBox.clickedButton() == messageBox.button(QMessageBox.Yes):
            print('确定退出')
            event.accept()
        else:
            print('取消退出')
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    guangyi = GuangYi()
    sys.exit(app.exec_())
    cursor.close()  #关闭数据库链接
    conn.close()
