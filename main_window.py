# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QWidget)
import camera_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 752)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(210, 80, 640, 480))
        self.input.setScaledContents(True)
        self.input.setAlignment(Qt.AlignCenter)
        self.buttton_image_select = QPushButton(self.centralwidget)
        self.buttton_image_select.setObjectName(u"buttton_image_select")
        self.buttton_image_select.setGeometry(QRect(110, 600, 70, 40))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(12)
        self.buttton_image_select.setFont(font)
        self.buttton_video_select = QPushButton(self.centralwidget)
        self.buttton_video_select.setObjectName(u"buttton_video_select")
        self.buttton_video_select.setGeometry(QRect(110, 670, 70, 40))
        self.buttton_video_select.setFont(font)
        self.button_weight_select = QPushButton(self.centralwidget)
        self.button_weight_select.setObjectName(u"button_weight_select")
        self.button_weight_select.setGeometry(QRect(70, 130, 130, 40))
        self.button_weight_select.setFont(font)
        self.button_weight_select.setStyleSheet(u"# rgb(0, 170, 255)")
        self.button_weight_init = QPushButton(self.centralwidget)
        self.button_weight_init.setObjectName(u"button_weight_init")
        self.button_weight_init.setGeometry(QRect(70, 200, 130, 40))
        self.button_weight_init.setFont(font)
        self.button_image_detect = QPushButton(self.centralwidget)
        self.button_image_detect.setObjectName(u"button_image_detect")
        self.button_image_detect.setGeometry(QRect(250, 600, 70, 40))
        self.button_image_detect.setFont(font)
        self.button_image_show = QPushButton(self.centralwidget)
        self.button_image_show.setObjectName(u"button_image_show")
        self.button_image_show.setGeometry(QRect(390, 600, 70, 40))
        self.button_image_show.setFont(font)
        self.button_video_detect = QPushButton(self.centralwidget)
        self.button_video_detect.setObjectName(u"button_video_detect")
        self.button_video_detect.setGeometry(QRect(250, 670, 70, 40))
        self.button_video_detect.setFont(font)
        self.button_video_suspend = QPushButton(self.centralwidget)
        self.button_video_suspend.setObjectName(u"button_video_suspend")
        self.button_video_suspend.setGeometry(QRect(390, 670, 70, 40))
        self.button_video_suspend.setFont(font)
        self.button_video_stop = QPushButton(self.centralwidget)
        self.button_video_stop.setObjectName(u"button_video_stop")
        self.button_video_stop.setGeometry(QRect(760, 670, 100, 40))
        self.button_video_stop.setFont(font)
        self.button_image_stop = QPushButton(self.centralwidget)
        self.button_image_stop.setObjectName(u"button_image_stop")
        self.button_image_stop.setGeometry(QRect(760, 600, 100, 40))
        self.button_image_stop.setFont(font)
        self.button_image_export = QPushButton(self.centralwidget)
        self.button_image_export.setObjectName(u"button_image_export")
        self.button_image_export.setGeometry(QRect(530, 600, 140, 40))
        self.button_image_export.setFont(font)
        self.button_video_export = QPushButton(self.centralwidget)
        self.button_video_export.setObjectName(u"button_video_export")
        self.button_video_export.setGeometry(QRect(530, 670, 140, 40))
        self.button_video_export.setFont(font)
        self.label_weight_select = QLabel(self.centralwidget)
        self.label_weight_select.setObjectName(u"label_weight_select")
        self.label_weight_select.setGeometry(QRect(10, 132, 34, 34))
        self.label_weight_select.setFont(font)
        self.label_weight_init = QLabel(self.centralwidget)
        self.label_weight_init.setObjectName(u"label_weight_init")
        self.label_weight_init.setGeometry(QRect(10, 202, 34, 34))
        self.label_weight_init.setFont(font)
        self.label_image_select = QLabel(self.centralwidget)
        self.label_image_select.setObjectName(u"label_image_select")
        self.label_image_select.setGeometry(QRect(60, 605, 30, 30))
        self.label_video_select = QLabel(self.centralwidget)
        self.label_video_select.setObjectName(u"label_video_select")
        self.label_video_select.setGeometry(QRect(60, 675, 30, 30))
        self.label_image_detect = QLabel(self.centralwidget)
        self.label_image_detect.setObjectName(u"label_image_detect")
        self.label_image_detect.setGeometry(QRect(200, 605, 30, 30))
        self.label_video_detect = QLabel(self.centralwidget)
        self.label_video_detect.setObjectName(u"label_video_detect")
        self.label_video_detect.setGeometry(QRect(200, 675, 30, 30))
        self.label_image_show = QLabel(self.centralwidget)
        self.label_image_show.setObjectName(u"label_image_show")
        self.label_image_show.setGeometry(QRect(340, 605, 30, 30))
        self.label_image_stop = QLabel(self.centralwidget)
        self.label_image_stop.setObjectName(u"label_image_stop")
        self.label_image_stop.setGeometry(QRect(700, 605, 30, 30))
        self.label_image_export = QLabel(self.centralwidget)
        self.label_image_export.setObjectName(u"label_image_export")
        self.label_image_export.setGeometry(QRect(470, 605, 30, 30))
        self.label_video_suspend = QLabel(self.centralwidget)
        self.label_video_suspend.setObjectName(u"label_video_suspend")
        self.label_video_suspend.setGeometry(QRect(340, 675, 30, 30))
        self.label_video_stop = QLabel(self.centralwidget)
        self.label_video_stop.setObjectName(u"label_video_stop")
        self.label_video_stop.setGeometry(QRect(700, 670, 30, 30))
        self.label_video_export = QLabel(self.centralwidget)
        self.label_video_export.setObjectName(u"label_video_export")
        self.label_video_export.setGeometry(QRect(470, 670, 30, 30))
        self.confidence = QLabel(self.centralwidget)
        self.confidence.setObjectName(u"confidence")
        self.confidence.setGeometry(QRect(20, 270, 80, 30))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.confidence.setFont(font1)
        self.confidence.setStyleSheet(u"QLabel#confidence{\n"
"	font-size:12pt;\n"
"}")
        self.con_slider = QSlider(self.centralwidget)
        self.con_slider.setObjectName(u"con_slider")
        self.con_slider.setGeometry(QRect(40, 330, 100, 30))
        self.con_slider.setStyleSheet(u"QSlider{\n"
"	border-color: #bcbcbc;\n"
"	color:#57a4ff;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 3px;\n"
"  	 margin: 0px 0;\n"
"     left: 5px;\n"
"	right: 5px;\n"
" }\n"
"QSlider::handle:horizontal {\n"
"     border: 0px ;\n"
"     border-image: url(:/img/img/icons/full-moon.png);\n"
"	 width:17px;\n"
"     margin: -7px -7px -7px -7px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #f9f9f9, stop:0.25 #f9f9f9, stop:0.5 #f9f9f9, stop:1 #f9f9f9);\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #57a4ff, stop:0.25 #57a4ff, stop:0.5 #57a4ff, stop:1 #57a4ff);\n"
"}")
        self.con_slider.setMaximum(100)
        self.con_slider.setValue(25)
        self.con_slider.setOrientation(Qt.Horizontal)
        self.con_number = QDoubleSpinBox(self.centralwidget)
        self.con_number.setObjectName(u"con_number")
        self.con_number.setGeometry(QRect(120, 270, 60, 30))
        self.con_number.setFrame(False)
        self.con_number.setKeyboardTracking(False)
        self.con_number.setMaximum(1.000000000000000)
        self.con_number.setSingleStep(0.010000000000000)
        self.con_number.setStepType(QAbstractSpinBox.DefaultStepType)
        self.con_number.setValue(0.250000000000000)
        self.confidence_2 = QLabel(self.centralwidget)
        self.confidence_2.setObjectName(u"confidence_2")
        self.confidence_2.setGeometry(QRect(30, 390, 60, 30))
        self.confidence_2.setFont(font1)
        self.confidence_2.setStyleSheet(u"QLabel#confidence{\n"
"	font-size:12pt;\n"
"}")
        self.iou_number = QDoubleSpinBox(self.centralwidget)
        self.iou_number.setObjectName(u"iou_number")
        self.iou_number.setGeometry(QRect(90, 390, 60, 30))
        self.iou_number.setFrame(False)
        self.iou_number.setMaximum(1.000000000000000)
        self.iou_number.setSingleStep(0.010000000000000)
        self.iou_number.setStepType(QAbstractSpinBox.DefaultStepType)
        self.iou_number.setValue(0.400000000000000)
        self.iou_slider = QSlider(self.centralwidget)
        self.iou_slider.setObjectName(u"iou_slider")
        self.iou_slider.setGeometry(QRect(40, 480, 100, 30))
        self.iou_slider.setStyleSheet(u"QSlider{\n"
"	border-color: #bcbcbc;\n"
"	color:#57a4ff;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 3px;\n"
"  	 margin: 0px 0;\n"
"     left: 5px;\n"
"	right: 5px;\n"
" }\n"
"QSlider::handle:horizontal {\n"
"     border: 0px ;\n"
"     border-image: url(:/img/img/icons/full-moon.png);\n"
"	 width:17px;\n"
"     margin: -7px -7px -7px -7px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #f9f9f9, stop:0.25 #f9f9f9, stop:0.5 #f9f9f9, stop:1 #f9f9f9);\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #57a4ff, stop:0.25 #57a4ff, stop:0.5 #57a4ff, stop:1 #57a4ff);\n"
"}")
        self.iou_slider.setMaximum(100)
        self.iou_slider.setValue(40)
        self.iou_slider.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 0, 951, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_detect_time = QLabel(self.centralwidget)
        self.label_detect_time.setObjectName(u"label_detect_time")
        self.label_detect_time.setGeometry(QRect(870, 130, 30, 30))
        self.lineEdit_detect_time = QLineEdit(self.centralwidget)
        self.lineEdit_detect_time.setObjectName(u"lineEdit_detect_time")
        self.lineEdit_detect_time.setGeometry(QRect(1010, 130, 50, 30))
        self.lineEdit_detect_time.setReadOnly(True)
        self.label_detect_object_nums = QLabel(self.centralwidget)
        self.label_detect_object_nums.setObjectName(u"label_detect_object_nums")
        self.label_detect_object_nums.setGeometry(QRect(870, 190, 30, 30))
        self.lineEdit_detect_object_nums = QLineEdit(self.centralwidget)
        self.lineEdit_detect_object_nums.setObjectName(u"lineEdit_detect_object_nums")
        self.lineEdit_detect_object_nums.setGeometry(QRect(1010, 190, 50, 32))
        self.lineEdit_detect_object_nums.setReadOnly(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(920, 130, 80, 40))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(920, 180, 70, 40))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_detect_object_pos = QLabel(self.centralwidget)
        self.label_detect_object_pos.setObjectName(u"label_detect_object_pos")
        self.label_detect_object_pos.setGeometry(QRect(870, 250, 30, 30))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(950, 240, 80, 40))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_detect_object_all = QLabel(self.centralwidget)
        self.label_detect_object_all.setObjectName(u"label_detect_object_all")
        self.label_detect_object_all.setGeometry(QRect(870, 310, 30, 30))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(930, 300, 120, 40))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(870, 370, 51, 31))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(870, 470, 51, 31))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_xmin = QLineEdit(self.centralwidget)
        self.lineEdit_xmin.setObjectName(u"lineEdit_xmin")
        self.lineEdit_xmin.setGeometry(QRect(950, 370, 80, 30))
        self.lineEdit_xmin.setReadOnly(True)
        self.lineEdit_xmax = QLineEdit(self.centralwidget)
        self.lineEdit_xmax.setObjectName(u"lineEdit_xmax")
        self.lineEdit_xmax.setGeometry(QRect(950, 470, 80, 30))
        self.lineEdit_xmax.setReadOnly(True)
        self.lineEdit_ymax = QLineEdit(self.centralwidget)
        self.lineEdit_ymax.setObjectName(u"lineEdit_ymax")
        self.lineEdit_ymax.setGeometry(QRect(950, 520, 80, 30))
        self.lineEdit_ymax.setReadOnly(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(870, 520, 51, 31))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_ymin = QLineEdit(self.centralwidget)
        self.lineEdit_ymin.setObjectName(u"lineEdit_ymin")
        self.lineEdit_ymin.setGeometry(QRect(950, 420, 80, 30))
        self.lineEdit_ymin.setReadOnly(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(870, 420, 51, 31))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(210, 50, 611, 31))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(16)
        font3.setItalic(True)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_camera_select = QLabel(self.centralwidget)
        self.label_camera_select.setObjectName(u"label_camera_select")
        self.label_camera_select.setGeometry(QRect(880, 585, 30, 30))
        self.label_camera_detect = QLabel(self.centralwidget)
        self.label_camera_detect.setObjectName(u"label_camera_detect")
        self.label_camera_detect.setGeometry(QRect(880, 635, 30, 30))
        self.button_camera_start = QPushButton(self.centralwidget)
        self.button_camera_start.setObjectName(u"button_camera_start")
        self.button_camera_start.setGeometry(QRect(920, 580, 90, 40))
        self.button_camera_start.setFont(font)
        self.button_camera_detect = QPushButton(self.centralwidget)
        self.button_camera_detect.setObjectName(u"button_camera_detect")
        self.button_camera_detect.setGeometry(QRect(920, 630, 90, 40))
        self.button_camera_detect.setFont(font)
        self.label_camera_stop = QLabel(self.centralwidget)
        self.label_camera_stop.setObjectName(u"label_camera_stop")
        self.label_camera_stop.setGeometry(QRect(880, 685, 30, 30))
        self.button_camera_stop = QPushButton(self.centralwidget)
        self.button_camera_stop.setObjectName(u"button_camera_stop")
        self.button_camera_stop.setGeometry(QRect(920, 680, 90, 40))
        self.button_camera_stop.setFont(font)
        self.label_main = QLabel(self.centralwidget)
        self.label_main.setObjectName(u"label_main")
        self.label_main.setGeometry(QRect(0, 0, 1071, 771))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(870, 580, 2, 150))
        self.lineEdit_4.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 670, 1000, 2))
        font4 = QFont()
        font4.setPointSize(9)
        self.line.setFont(font4)
        self.line.setCursor(QCursor(Qt.UpArrowCursor))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(100, 650, 750, 2))
        self.lineEdit_5.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(200, 100, 2, 450))
        self.lineEdit_6.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(850, 110, 2, 450))
        self.lineEdit_7.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 540, 650, 31))
        self.lineEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_main.raise_()
        self.input.raise_()
        self.buttton_image_select.raise_()
        self.buttton_video_select.raise_()
        self.button_weight_select.raise_()
        self.button_weight_init.raise_()
        self.button_image_detect.raise_()
        self.button_image_show.raise_()
        self.button_video_detect.raise_()
        self.button_video_suspend.raise_()
        self.button_video_stop.raise_()
        self.button_image_stop.raise_()
        self.button_image_export.raise_()
        self.button_video_export.raise_()
        self.label_weight_select.raise_()
        self.label_weight_init.raise_()
        self.label_image_select.raise_()
        self.label_video_select.raise_()
        self.label_image_detect.raise_()
        self.label_video_detect.raise_()
        self.label_image_show.raise_()
        self.label_image_stop.raise_()
        self.label_image_export.raise_()
        self.label_video_suspend.raise_()
        self.label_video_stop.raise_()
        self.label_video_export.raise_()
        self.confidence.raise_()
        self.con_slider.raise_()
        self.con_number.raise_()
        self.confidence_2.raise_()
        self.iou_number.raise_()
        self.iou_slider.raise_()
        self.label.raise_()
        self.label_detect_time.raise_()
        self.lineEdit_detect_time.raise_()
        self.label_detect_object_nums.raise_()
        self.lineEdit_detect_object_nums.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_detect_object_pos.raise_()
        self.label_4.raise_()
        self.label_detect_object_all.raise_()
        self.comboBox.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.lineEdit_xmin.raise_()
        self.lineEdit_xmax.raise_()
        self.lineEdit_ymax.raise_()
        self.label_7.raise_()
        self.lineEdit_ymin.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_camera_select.raise_()
        self.label_camera_detect.raise_()
        self.button_camera_start.raise_()
        self.button_camera_detect.raise_()
        self.label_camera_stop.raise_()
        self.button_camera_stop.raise_()
        self.lineEdit_4.raise_()
        self.line.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf\u5c55\u793a", None))
        self.buttton_image_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u50cf", None))
        self.buttton_video_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.button_weight_select.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6743\u91cd\u9009\u62e9", None))
        self.button_weight_init.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6743\u91cd\u521d\u59cb\u5316", None))
        self.button_image_detect.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u68c0\u6d4b", None))
        self.button_image_show.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u5c55\u793a", None))
        self.button_video_detect.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u68c0\u6d4b", None))
        self.button_video_suspend.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u68c0\u6d4b", None))
        self.button_video_stop.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u89c6\u9891\u68c0\u6d4b", None))
        self.button_image_stop.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u56fe\u50cf\u68c0\u6d4b", None))
        self.button_image_export.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u68c0\u6d4b\u7ed3\u679c\u5bfc\u51fa", None))
        self.button_video_export.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u68c0\u6d4b\u7ed3\u679c\u5bfc\u51fa", None))
        self.label_weight_select.setText(QCoreApplication.translate("MainWindow", u"\u6743\u91cd\u56fe", None))
        self.label_weight_init.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u56fe", None))
        self.label_image_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u56fe-\u56fe", None))
        self.label_video_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u89c6-\u56fe", None))
        self.label_image_detect.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u68c0-\u56fe", None))
        self.label_video_detect.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u68c0-\u56fe", None))
        self.label_image_show.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u5c55-\u56fe", None))
        self.label_image_stop.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7ed3-\u56fe", None))
        self.label_image_export.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u5bfc-\u56fe", None))
        self.label_video_suspend.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c-\u56fe", None))
        self.label_video_stop.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u7ed3-\u56fe", None))
        self.label_video_export.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u5bfc-\u56fe", None))
        self.confidence.setText(QCoreApplication.translate("MainWindow", u"Confidence:", None))
        self.confidence_2.setText(QCoreApplication.translate("MainWindow", u"IOU\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u673a\u5668\u5b66\u4e60\u7684\u9053\u8def\u7f3a\u9677\u68c0\u6d4b\u7cfb\u7edfV2.4", None))
        self.label_detect_time.setText(QCoreApplication.translate("MainWindow", u"\u7528\u65f6\u56fe", None))
        self.lineEdit_detect_time.setText("")
        self.lineEdit_detect_time.setPlaceholderText("")
        self.label_detect_object_nums.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807-\u56fe", None))
        self.lineEdit_detect_object_nums.setText("")
        self.lineEdit_detect_object_nums.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7528\u65f6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6570\u91cf\uff1a", None))
        self.label_detect_object_pos.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e\u56fe", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u4f4d\u7f6e\uff1a", None))
        self.label_detect_object_all.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6846", None))
        self.comboBox.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"xmin\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"xmax\uff1a", None))
        self.lineEdit_xmin.setText("")
        self.lineEdit_xmin.setPlaceholderText("")
        self.lineEdit_xmax.setText("")
        self.lineEdit_xmax.setPlaceholderText("")
        self.lineEdit_ymax.setText("")
        self.lineEdit_ymax.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ymax\uff1a", None))
        self.lineEdit_ymin.setText("")
        self.lineEdit_ymin.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ymin\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6167\u773c\u8bc6\u8def\u2014\u2014\u9053\u8def\u7f3a\u9677\u63a2\u6d4b\u5148\u950b", None))
        self.label_camera_select.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf-\u56fe", None))
        self.label_camera_detect.setText(QCoreApplication.translate("MainWindow", u"\u6444\u68c0-\u56fe", None))
        self.button_camera_start.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.button_camera_detect.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u68c0\u6d4b", None))
        self.label_camera_stop.setText(QCoreApplication.translate("MainWindow", u"\u6444\u7ed3-\u56fe", None))
        self.button_camera_stop.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u6444\u50cf\u5934", None))
        self.label_main.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u72b6\u6001\u76d1\u6d4b\u6846", None))
    # retranslateUi

