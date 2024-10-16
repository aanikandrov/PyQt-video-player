
import os
import sys
import cv2
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene,
                             QGraphicsPixmapItem, QVBoxLayout, QWidget,
                             QLabel, QPushButton, QButtonGroup)

from PyQt5.QtCore import QThreadPool

import cv2
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

import Video_Pool
import Video_QLabel
import Video_QGraphics
import Video_Thread




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 319)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.main_radioLightTheme = QtWidgets.QRadioButton(self.centralwidget)
        # self.main_radioLightTheme.setGeometry(QtCore.QRect(20, 260, 82, 17))
        # self.main_radioLightTheme.setObjectName("main_radioLightTheme")
        # self.main_radioDarkTheme = QtWidgets.QRadioButton(self.centralwidget)
        # self.main_radioDarkTheme.setGeometry(QtCore.QRect(20, 280, 82, 17))
        # self.main_radioDarkTheme.setObjectName("main_radioDarkTheme_2")

        self.main_pushFiles = QtWidgets.QPushButton(self.centralwidget)
        self.main_pushFiles.setGeometry(QtCore.QRect(320, 260, 75, 23))
        self.main_pushFiles.setStyleSheet("border-top: 1px solid rgb(0, 0, 0);\n"
                                          "border-left: 1px solid rgb(0, 0, 0);\n"
                                          "border-right: 1px solid rgb(0, 0, 0);\n"
                                          "border-bottom: 1px solid rgb(0, 0, 0);\n"
                                          "")
        self.main_pushFiles.setObjectName("main_pushFiles")
        self.tabVideo = QtWidgets.QTabWidget(self.centralwidget)
        self.tabVideo.setGeometry(QtCore.QRect(10, 10, 391, 241))
        self.tabVideo.setStyleSheet(" border: 2px solid #C4C4C3;")
        self.tabVideo.setObjectName("tabVideo")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tab1_push2 = QtWidgets.QPushButton(self.tab)
        self.tab1_push2.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.tab1_push2.setStyleSheet("border-top: 1px solid rgb(0, 0, 0);\n"
                                      "border-left: 1px solid rgb(0, 0, 0);\n"
                                      "border-right: 1px solid rgb(0, 0, 0);\n"
                                      "border-bottom: 1px solid rgb(0, 0, 0);")
        self.tab1_push2.setObjectName("tab1_push2")
        self.tab1_push1 = QtWidgets.QPushButton(self.tab)
        self.tab1_push1.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.tab1_push1.setStyleSheet("border-top: 1px solid rgb(0, 0, 0);\n"
                                      "border-left: 1px solid rgb(0, 0, 0);\n"
                                      "border-right: 1px solid rgb(0, 0, 0);\n"
                                      "border-bottom: 1px solid rgb(0, 0, 0);")
        self.tab1_push1.setObjectName("tab1_push1")
        self.tab1_dial = QtWidgets.QDial(self.tab)
        self.tab1_dial.setGeometry(QtCore.QRect(20, 80, 50, 64))
        self.tab1_dial.setStyleSheet("border-top: 3px solid rgb(0, 0, 0);\n"
                                     "border-left: 3px solid rgb(0, 0, 0);\n"
                                     "border-right: 3px solid rgb(0, 0, 0);\n"
                                     "border-bottom: 3px solid rgb(0, 0, 0);")
        self.tab1_dial.setObjectName("tab1_dial")
        self.tab1_frame = QtWidgets.QFrame(self.tab)
        self.tab1_frame.setGeometry(QtCore.QRect(80, 70, 120, 80))
        self.tab1_frame.setStyleSheet("border-top: 1px solid rgb(0, 0, 0);\n"
                                      "border-left: 1px solid rgb(0, 0, 0);\n"
                                      "border-right: 1px solid rgb(0, 0, 0);\n"
                                      "border-bottom: 1px solid rgb(0, 0, 0);")
        self.tab1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab1_frame.setObjectName("tab1_frame")
        self.tabVideo.addTab(self.tab, "")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab2_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.tab2_spinBox.setGeometry(QtCore.QRect(20, 20, 42, 31))
        self.tab2_spinBox.setObjectName("tab2_spinBox")
        self.tab2_textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.tab2_textEdit.setGeometry(QtCore.QRect(70, 20, 41, 31))
        self.tab2_textEdit.setObjectName("tab2_textEdit")
        self.tab2_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_lineEdit.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.tab2_lineEdit.setText("")
        self.tab2_lineEdit.setObjectName("tab2_lineEdit")
        self.tab2_horizontalSlider = QtWidgets.QSlider(self.tab_2)
        self.tab2_horizontalSlider.setGeometry(QtCore.QRect(20, 100, 111, 22))
        self.tab2_horizontalSlider.setStyleSheet(" border: 2px solid #C4C4C3;")
        self.tab2_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tab2_horizontalSlider.setObjectName("tab2_horizontalSlider")
        self.tabVideo.addTab(self.tab_2, "")


        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab3_label = QtWidgets.QLabel(self.tab_3)
        self.tab3_label.setGeometry(QtCore.QRect(20, 20, 270, 170))
        self.tab3_label.setFrameShape(QtWidgets.QFrame.Box)
        self.tab3_label.setLineWidth(8)
        self.tab3_label.setText("")
        self.tab3_label.setObjectName("tab3_label")
        self.tab3_pushPlay = QtWidgets.QPushButton(self.tab_3)
        self.tab3_pushPlay.setGeometry(QtCore.QRect(300, 30, 50, 25))
        self.tab3_pushPlay.setObjectName("tab3_pushPlay")
        self.tab3_pushRestart = QtWidgets.QPushButton(self.tab_3)
        self.tab3_pushRestart.setGeometry(QtCore.QRect(300, 60, 50, 25))
        self.tab3_pushRestart.setObjectName("tab3_pushPause")
        self.tabVideo.addTab(self.tab_3, "")


        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tab4_graphicsView = QtWidgets.QGraphicsView(self.tab_4)
        self.tab4_graphicsView.setGeometry(QtCore.QRect(20, 20, 270, 170))
        self.tab4_graphicsView.setAutoFillBackground(False)
        self.tab4_graphicsView.setObjectName("tab4_graphicsView")
        self.tab4_pushPlay = QtWidgets.QPushButton(self.tab_4)
        self.tab4_pushPlay.setGeometry(QtCore.QRect(300, 30, 50, 25))
        self.tab4_pushPlay.setObjectName("tab4_pushPlay")
        self.tab4_pushRestart = QtWidgets.QPushButton(self.tab_4)
        self.tab4_pushRestart.setGeometry(QtCore.QRect(300, 60, 50, 25))
        self.tab4_pushRestart.setObjectName("tab4_pushPause")
        self.tabVideo.addTab(self.tab_4, "")


        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tab5_label = QtWidgets.QLabel(self.tab_5)
        self.tab5_label.setGeometry(QtCore.QRect(20, 20, 270, 170))
        self.tab5_label.setText("")
        self.tab5_label.setObjectName("tab5_label")
        self.tab5_pushPlay = QtWidgets.QPushButton(self.tab_5)
        self.tab5_pushPlay.setGeometry(QtCore.QRect(300, 30, 50, 25))
        self.tab5_pushPlay.setObjectName("tab5_pushPlay")
        self.tab5_radioCamera = QtWidgets.QRadioButton(self.tab_5)
        self.tab5_radioCamera.setGeometry(QtCore.QRect(300, 60, 70, 25))
        self.tab5_radioCamera.setObjectName("tab5_radioCamera")
        self.tab5_radioFile = QtWidgets.QRadioButton(self.tab_5)
        self.tab5_radioFile.setGeometry(QtCore.QRect(300, 90, 70, 25))
        self.tab5_radioFile.setObjectName("tab5_radioFile")
        self.tabVideo.addTab(self.tab_5, "")

        # self.tab_6 = QtWidgets.QWidget()
        # self.tab_6.setObjectName("tab_6")
        # self.tab6_label = QtWidgets.QLabel(self.tab_6)
        # self.tab6_label.setGeometry(QtCore.QRect(20, 20, 270, 170))
        # self.tab6_label.setText("")
        # self.tab6_label.setObjectName("tab6_label")
        # self.tab6_pushPlay = QtWidgets.QPushButton(self.tab_6)
        # self.tab6_pushPlay.setGeometry(QtCore.QRect(300, 30, 50, 25))
        # self.tab6_pushPlay.setObjectName("tab6_pushPlay")
        # self.tab6_radioCamera = QtWidgets.QRadioButton(self.tab_6)
        # self.tab6_radioCamera.setGeometry(QtCore.QRect(300, 60, 70, 25))
        # self.tab6_radioCamera.setObjectName("tab6_radioCamera")
        # self.tab6_radioFile = QtWidgets.QRadioButton(self.tab_6)
        # self.tab6_radioFile.setGeometry(QtCore.QRect(300, 90, 70, 25))
        # self.tab6_radioFile.setObjectName("tab5_radioFile")
        # self.tabVideo.addTab(self.tab_6, "")


        self.tabVideo.raise_()
        # self.main_radioLightTheme.raise_()
        # self.main_radioDarkTheme.raise_()

        self.main_pushFiles.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabVideo.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.main_radioLightTheme.setText(_translate("MainWindow", "Light Theme"))
        # self.main_radioDarkTheme.setText(_translate("MainWindow", "Dark Theme"))
        self.main_pushFiles.setText(_translate("MainWindow", "FILES"))
        self.tab1_push2.setText(_translate("MainWindow", "Button 2"))
        self.tab1_push1.setText(_translate("MainWindow", "Button 1"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tab3_pushPlay.setText(_translate("MainWindow", "Play"))
        self.tab3_pushRestart.setText(_translate("MainWindow", "Restart"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_3), _translate("MainWindow", "Tab 3"))
        self.tab4_pushPlay.setText(_translate("MainWindow", "Play"))
        self.tab4_pushRestart.setText(_translate("MainWindow", "Restart"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_4), _translate("MainWindow", "Tab 4"))
        self.tab5_pushPlay.setText(_translate("MainWindow", "Play"))
        self.tab5_radioCamera.setText(_translate("MainWindow", "Camera"))
        self.tab5_radioFile.setText(_translate("MainWindow", "File"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_5), _translate("MainWindow", "Tab 5"))

        # self.tab6_pushPlay.setText(_translate("MainWindow", "Play"))
        # self.tab6_radioCamera.setText(_translate("MainWindow", "Camera"))
        # self.tab6_radioFile.setText(_translate("MainWindow", "File"))
        # self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_6), _translate("MainWindow", "Tab 6"))

    def functions(self, MainWindow):
        self.tab1_push1.setStyleSheet("background-color: white;")
        self.tab1_push1.clicked.connect(self.on_pushButton_clicked)
        self.tab1_push2.setStyleSheet("background-color: white;")
        self.tab1_push2.clicked.connect(self.on_pushButton_2_clicked)

        self.main_pushFiles.clicked.connect(self.open_files)

        # self.button_group = QButtonGroup(self)
        # self.button_group.addButton(self.main_radioLightTheme)
        # self.button_group.addButton(self.main_radioDarkTheme)
        # self.button_group.buttonClicked.connect(self.changeTheme)
        # self.main_radioLightTheme.setChecked(True)

        self.tab2_horizontalSlider.setRange(-10, 10)
        self.tab2_horizontalSlider.valueChanged.connect(self.update_line_edit)
        self.tab1_dial.setRange(0, 255)
        self.tab1_dial.valueChanged.connect(self.change_color)
        self.tab1_frame.setStyleSheet("background-color: white;")

        self.tab2_textEdit.setReadOnly(True)
        self.tab2_spinBox.valueChanged.connect(self.textEdit_change)
        self.tab2_lineEdit.setReadOnly(True)

        self.tab5_radioCamera.setChecked(True)
        self.tab5_radioCamera.toggled.connect(self.changeMode_tab5)
        self.tab5_radioFile.toggled.connect(self.changeMode_tab5)

        # self.tab6_radioCamera.toggled.connect(self.start_camera_capture)
        # self.tab6_radioFile.toggled.connect(self.start_file_capture)



    def video_tab3(self, MainWindow):
        video_path = "D:/Рабочий стол/vid4.mp4"
        self.video_label = Video_QLabel.Class_Video_QLabel(video_path, self.tab3_label, self)

        self.tab3_pushPlay.clicked.connect(self.video_label.play)
        self.tab3_pushRestart.clicked.connect(self.video_label.restart)

    # --- --- --- --- --- --- --- --- --- --- --- ---
    def video_tab4(self, MainWindow):
        video_path = "D:/Рабочий стол/vid4.mp4"
        self.tab4_graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tab4_graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.video_player = Video_QGraphics.Class_Video_QGraphics(video_path, self.tab4_graphicsView)
        self.tab4_pushPlay.clicked.connect(self.video_player.play)
        self.tab4_pushRestart.clicked.connect(self.video_player.restart)

    ## --- --- ---- -- - -- -- - - -  -


    def video_tab5(self, MainWindow):
        self.mode = True
        self.video_path_3 = "D:/Рабочий стол/vid4.mp4"

        self.video_thread = Video_Thread.start_video_stream(self.tab5_label,
                                               self.mode,
                                               self.video_path_3)

        #self.tab5_pushPlay.clicked.connect(self.play_tab5)
        self.tab5_pushPlay.clicked.connect(self.play_tab5)

    def changeMode_tab5(self):
        if self.tab5_radioCamera.isChecked():
            self.tab5_label.clear()
            self.mode = True
            self.video_thread.stop_capture()
            self.video_thread = Video_Thread.start_video_stream(self.tab5_label,
                                                   self.mode,
                                                   self.video_path_3)
        elif self.tab5_radioFile.isChecked():
            self.mode = False
            self.tab5_label.clear()
            self.video_thread.stop_capture()
            self.video_thread = Video_Thread.start_video_stream(self.tab5_label,
                                                   self.mode,
                                                   self.video_path_3)

    def play_tab5(self):
        #self.video_thread.start_capture()
        self.video_thread.pause_capture()

    def close_tab5(self, event):
        self.video_thread.stop_capture()
        event.accept()

    ## --- --- ---- -- - -- -- - - -  -

    # video_capture_runnable = None
    # thread_pool = QThreadPool()
    # video_capture_worker = None


    ## --- --- ---- -- - -- -- - - -  -

    def changeTheme(self):
        if self.main_radioLightTheme.isChecked():
            self.setStyleSheet("background-color: white;")
        elif self.main_radioDarkTheme.isChecked():
            self.setStyleSheet("background-color: darkgray;")


    def textEdit_change(self, a):
        self.tab2_textEdit.setPlainText(f'{a}')

    def change_color(self, value):
        red = value
        green = 255 - value
        blue = (value * 2) % 256
        self.tab1_frame.setStyleSheet(f"background-color: rgb({red},"
                                 f" {green}, {blue});")
    def open_files(self):
        project_directory = os.path.dirname(os.path.abspath(__file__))
        os.startfile(project_directory)

    def update_line_edit(self, value):
        self.tab2_lineEdit.setText(str(value))

    def on_pushButton_clicked(self):
        self.tab1_push1.setStyleSheet("background-color: white;")
        self.tab1_push2.setStyleSheet("background-color: red;")

    def on_pushButton_2_clicked(self):
        self.tab1_push1.setStyleSheet("background-color: blue;")
        self.tab1_push2.setStyleSheet("background-color: white;")