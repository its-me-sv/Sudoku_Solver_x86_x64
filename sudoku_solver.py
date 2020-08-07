from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import sys
from functools import partial
from os import path, makedirs
from time import perf_counter

buttons = [[0 for i in range(9)] for j in range(9)]
game_board = [[0 for i in range(9)] for j in range(9)]
user_locs = list()
ans = None
ttime = None

def Solve_The_Board(board):
    empty = Return_Empty(board)
    if not empty:
        return True
    else:
        r, c = empty
    for i in range(1, 10):
        if Check_Available(board, i, (r, c)):
            board[r][c] = i
            if Solve_The_Board(board):
                return True
            board[r][c] = 0
    return False

def Check_Available(board, no, rc):
    for i in range(len(board[0])):
        if board[rc[0]][i] == no and i != rc[1]:
            return False

    for i in range(len(board)):
        if board[i][rc[1]] == no and i != rc[0]:
            return False

    x = rc[0] // 3
    y = rc[1] // 3

    for i in range(x*3, x*3 + 3):
        for j in range(y*3, y*3 + 3):
            if (i,j) != rc and board[i][j] == no:
                return False

    return True

def Return_Empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

def Message(code):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle(" ")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/splash_screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if not code:
        msg.setText("Board Has Been Reset Successfully")
    elif code == 1:
        msg.setText("Board Has Been Solved Successfully\nTime Taken : {} Seconds".format(ttime))
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


class Ui_Option(object):
    def setupUi(self, Option, sen):
        Option.setObjectName("Option")
        Option.resize(300, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/splash_screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Option.setWindowIcon(icon)
        Option.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(Option)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/bl1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/bl2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 50, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/bl3.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 51, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/bl4.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 140, 51, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/bl5.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 140, 51, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/bl6.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/bl7.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 230, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/bl8.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 230, 51, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/bl9.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.b1 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(20, 50, 51, 51))
        self.b1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b1.setIcon(icon1)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(120, 50, 51, 51))
        self.b2.setText("")
        self.b2.setIcon(icon1)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(220, 50, 51, 51))
        self.b3.setText("")
        self.b3.setIcon(icon1)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(20, 140, 51, 51))
        self.b4.setText("")
        self.b4.setIcon(icon1)
        self.b4.setObjectName("b4")
        self.b5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(120, 140, 51, 51))
        self.b5.setText("")
        self.b5.setIcon(icon1)
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(220, 140, 51, 51))
        self.b6.setText("")
        self.b6.setIcon(icon1)
        self.b6.setObjectName("b6")
        self.b7 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(20, 230, 51, 51))
        self.b7.setText("")
        self.b7.setIcon(icon1)
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(120, 230, 51, 51))
        self.b8.setText("")
        self.b8.setIcon(icon1)
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(220, 230, 51, 51))
        self.b9.setText("")
        self.b9.setIcon(icon1)
        self.b9.setObjectName("b9")
        Option.setCentralWidget(self.centralwidget)

        self.retranslateUi(Option)
        QtCore.QMetaObject.connectSlotsByName(Option)
        self.b1.clicked.connect(partial(self.a1,sen))
        self.b2.clicked.connect(partial(self.a2,sen))
        self.b3.clicked.connect(partial(self.a3,sen))
        self.b4.clicked.connect(partial(self.a4,sen))
        self.b5.clicked.connect(partial(self.a5,sen))
        self.b6.clicked.connect(partial(self.a6,sen))
        self.b7.clicked.connect(partial(self.a7,sen))
        self.b8.clicked.connect(partial(self.a8,sen))
        self.b9.clicked.connect(partial(self.a9,sen))

    def a1(self,bjo):
        global ans, game_board, user_locs
        ans = 1
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a2(self,bjo):
        global ans, game_board, user_locs
        ans = 2
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a3(self,bjo):
        global ans, game_board, user_locs
        ans = 3
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a4(self,bjo):
        global ans, game_board, user_locs
        ans = 4
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a5(self,bjo):
        global ans, game_board, user_locs
        ans = 5
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a6(self,bjo):
        global ans, game_board, user_locs
        ans = 6
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a7(self,bjo):
        global ans, game_board, user_locs
        ans = 7
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a8(self,bjo):
        global ans, game_board, user_locs
        ans = 8
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def a9(self,bjo):
        global ans, game_board, user_locs
        ans = 9
        i,j = [int(k) for k in list(bjo.objectName())[1:]]
        user_locs.append((i,j))
        game_board[i][j] = ans
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(ans)))
        bjo.setIcon(icon1)
        Option.hide()

    def retranslateUi(self, Option):
        _translate = QtCore.QCoreApplication.translate
        Option.setWindowTitle(_translate("Option", "Option"))
        self.label_10.setText(_translate("Option", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Choose Number To Place</span></p></body></html>"))


class Ui_Board(object):
    def setupUi(self, Board):
        global buttons
        Board.setObjectName("Board")
        Board.resize(600, 600)
        Board.setMinimumSize(QtCore.QSize(600, 600))
        Board.setMaximumSize(QtCore.QSize(600, 600))
        Board.setBaseSize(QtCore.QSize(600, 600))
        Board.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/splash_screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Board.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Board)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Home_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Home_Button.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.Home_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Home_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_Button.setIcon(icon1)
        self.Home_Button.setObjectName("Home_Button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(180, 80, 21, 481))
        self.line.setStyleSheet("color: rgb(255, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(7)
        self.line.setMidLineWidth(7)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(390, 80, 21, 481))
        self.line_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(7)
        self.line_2.setMidLineWidth(7)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 210, 601, 31))
        self.line_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(7)
        self.line_3.setMidLineWidth(7)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 370, 601, 31))
        self.line_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(7)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 70, 551, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        for i in range(9):
            for j in range(9):
                self.button = QtWidgets.QCommandLinkButton()
                self.button.setGeometry(QtCore.QRect(i, j, 51, 51))
                self.button.setFocusPolicy(QtCore.Qt.NoFocus)
                self.button.setObjectName("B"+str(i)+str(j))
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/newPrefix/square.png"))
                self.button.setIcon(icon1)
                buttons[i][j] = self.button
                self.gridLayout.addWidget(self.button,i,j)

        self.Reset_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_Button.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.Reset_Button.setFont(font)
        self.Reset_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Reset_Button.setObjectName("Reset_Button")
        self.Solve_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Solve_Button.setGeometry(QtCore.QRect(420, 560, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.Solve_Button.setFont(font)
        self.Solve_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Solve_Button.setObjectName("Solve_Button")
        Board.setCentralWidget(self.centralwidget)
        self.retranslateUi(Board)
        QtCore.QMetaObject.connectSlotsByName(Board)
        self.Home_Button.clicked.connect(self.Take_To_Home)
        for i in range(9):
            for j in range(9):
                buttons[i][j].clicked.connect(partial(self.Work,buttons[i][j]))
        self.Solve_Button.clicked.connect(self.Show_Board)
        self.Reset_Button.clicked.connect(self.Reset_Board)

    def Reset_Board(self):
        global game_board, user_locs
        game_board = [[0 for i in range(9)] for j in range(9)]
        user_locs = list()
        self.setupUi(Board)
        Board.show()
        Message(0)

    def Show_Board(self):
        global game_board, user_locs, buttons, ttime
        start = perf_counter()
        final = Solve_The_Board(game_board)
        end = perf_counter()
        ttime = round(end-start, 3)
        for i in range(9):
            for j in range(9):
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/newPrefix/bl{}.png".format(game_board[i][j])))
                if (i,j) in user_locs:
                    icon1.addPixmap(QtGui.QPixmap(":/newPrefix/{}.png".format(game_board[i][j])))
                buttons[i][j].setIcon(icon1)
        Message(1)

    def Work(self, bjo):
        global ui2, ans
        ui2.setupUi(Option, bjo)
        Option.show()

    def Take_To_Home(self):
        Splash_Screen.show()
        Board.hide()

    def retranslateUi(self, Board):
        _translate = QtCore.QCoreApplication.translate
        Board.setWindowTitle(_translate("Board", "Board"))
        self.Home_Button.setToolTip(_translate("Board", "<html><head/><body><p><span style=\" font-weight:600;\">Go To Home</span></p></body></html>"))
        self.Reset_Button.setToolTip(_translate("Board", "<html><head/><body><p><span style=\" font-weight:600;\">Removes All The Digits In The Board</span></p></body></html>"))
        self.Reset_Button.setText(_translate("Board", "Reset Board"))
        self.Solve_Button.setToolTip(_translate("Board", "<html><head/><body><p><span style=\" font-weight:600;\">Solve The Sudoku Board</span></p></body></html>"))
        self.Solve_Button.setText(_translate("Board", "Solve The Board"))


class Ui_Splash_Screen(object):
    def setupUi(self, Splash_Screen):
        Splash_Screen.setObjectName("Splash_Screen")
        Splash_Screen.resize(600, 600)
        Splash_Screen.setMinimumSize(QtCore.QSize(600, 600))
        Splash_Screen.setMaximumSize(QtCore.QSize(600, 600))
        Splash_Screen.setBaseSize(QtCore.QSize(600, 600))
        Splash_Screen.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/splash_screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Splash_Screen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Splash_Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/splash_screen.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.Main_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Main_Button.setGeometry(QtCore.QRect(80, 200, 421, 171))
        self.Main_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Main_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Main_Button.setIcon(icon1)
        self.Main_Button.setObjectName("Main_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Exit_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.Exit_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Exit_Button.setText("")
        self.Exit_Button.setIcon(icon1)
        self.Exit_Button.setObjectName("Exit_Button")
        Splash_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash_Screen)
        QtCore.QMetaObject.connectSlotsByName(Splash_Screen)

        self.Exit_Button.clicked.connect(self.Exit_Application)
        self.Main_Button.clicked.connect(self.Take_To_Main_Page)

    def Take_To_Main_Page(self):
        global ui1
        ui1.setupUi(Board)
        Board.show()
        Splash_Screen.hide()

    def Exit_Application(self):
        app.quit()

    def retranslateUi(self, Splash_Screen):
        _translate = QtCore.QCoreApplication.translate
        Splash_Screen.setWindowTitle(_translate("Splash_Screen", "Sudoku Project"))
        self.Main_Button.setToolTip(_translate("Splash_Screen", "<html><head/><body><p><span style=\" font-weight:600;\">Get In</span></p></body></html>"))
        self.Exit_Button.setToolTip(_translate("Splash_Screen", "<html><head/><body><p><span style=\" font-weight:600;\">Exit Application</span></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    Option = QtWidgets.QMainWindow()
    ui2 = Ui_Option()

    Board = QtWidgets.QMainWindow()
    ui1 = Ui_Board()

    Splash_Screen = QtWidgets.QMainWindow()
    ui = Ui_Splash_Screen()
    ui.setupUi(Splash_Screen)
    
    Splash_Screen.show()
    sys.exit(app.exec_())

#