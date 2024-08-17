from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import subprocess
from styles_main import StyleSheet

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Data-Plotter-App-2'
        width = 1000
        height = 800
        self.setFixedSize(width, height)
        self.setWindowTitle(self.title)

        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.AS = StyleSheet()

        self.setStyleSheet(self.AS.App_style)
        self.setStyleSheet(self.AS.App_style_2)
        self.setWindowTitle(self.title)

        self.GUI = GUI(self)

        self.setCentralWidget(self.GUI)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('')

        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)

        self.show()

    def closeEvent(self, event):
        print('**************************Closing Application****************************************')
        sys.exit(0)

class GUI(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.layout.addWidget(self.scrollArea)

        self.scrollWidget = QWidget()
        self.scrollArea.setWidget(self.scrollWidget)

        self.scrollLayout = QVBoxLayout(self.scrollWidget)

        self.TS = StyleSheet()
        self.make_Header()
        self.make_Footer()

    def make_Header(self):
        self.TITLE_LOGO = QFrame()
        self.scrollLayout.addWidget(self.TITLE_LOGO)

        self.H = QHBoxLayout(self.TITLE_LOGO)
        self.TITLE_LOGO.setFrameShape(QFrame.StyledPanel)
        self.TITLE_LOGO.setStyleSheet(self.TS.LOGO_frame_style)

        self.tim = QtGui.QPixmap("H:\\My_Application\\matplot_qt_01082024\\matplot_qt\\1\\final_1\\demo.png")
        self.tlogo_label = QLabel("")
        self.tlogo_label.resize(100, 100)
        self.tlogo_label.setStyleSheet("background-color: white; border-radius:15px;")
        self.tlogo_label.setMaximumSize(QtCore.QSize(125, 120))
        self.tlogo_label.setScaledContents(True)
        self.tlogo_label.setPixmap(self.tim)
        self.H.addWidget(self.tlogo_label)

        self.ttitle_label = QLabel("RANGE SYSTEM DIVISIONS - RSD")
        self.ttitle_label.setAlignment(Qt.AlignCenter)
        self.ttitle_label.setStyleSheet("font-size: 25px; background-color: #4375ac; color: white; border-radius: 10px;")
        self.ttitle_label.setMaximumSize(QtCore.QSize(1000, 120))
        self.H.addWidget(self.ttitle_label)

        self.tim = QtGui.QPixmap("H:\\My_Application\\matplot_qt_01082024\\matplot_qt\\1\\final_1\\demo.png")
        self.tlogo_label_2 = QLabel("")
        self.tlogo_label_2.resize(100, 100)
        self.tlogo_label_2.setStyleSheet("background-color: white; border-radius:15px;")
        self.tlogo_label_2.setMaximumSize(QtCore.QSize(125, 120))
        self.tlogo_label_2.setScaledContents(True)
        self.tlogo_label_2.setPixmap(self.tim)
        self.H.addWidget(self.tlogo_label_2)

        self.V = QVBoxLayout()
        self.scrollLayout.addLayout(self.V)

        self.V.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.title_label = QLabel("Data Plotter Application")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 40px; color: light green; border-radius: 10px;")
        self.title_label.setMaximumSize(QtCore.QSize(1000, 120))
        self.V.addWidget(self.title_label)

        self.button_layout = QHBoxLayout()
        self.scrollLayout.addLayout(self.button_layout)

        self.submit_button_1 = QPushButton("Two File Plot Compression App", self)
        self.submit_button_1.setStyleSheet(self.TS.buttonstyle)
        self.submit_button_1.clicked.connect(self.submit_clicked_1)
        self.button_layout.addWidget(self.submit_button_1)

        self.submit_button_2 = QPushButton("One file Plotting App", self)
        self.submit_button_2.setStyleSheet(self.TS.buttonstyle)
        self.submit_button_2.clicked.connect(self.submit_clicked_2)
        self.button_layout.addWidget(self.submit_button_2)

        self.submit_button_3 = QPushButton("Plot And Image to Pdf App", self)
        self.submit_button_3.setStyleSheet(self.TS.buttonstyle)
        self.submit_button_3.clicked.connect(self.submit_clicked_3)
        self.button_layout.addWidget(self.submit_button_3)

        self.V.addSpacerItem(QSpacerItem(80, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def make_Footer(self):
        self.footer = QFrame()
        self.footer.setStyleSheet(self.TS.footr)
        self.scrollLayout.addWidget(self.footer)
        self.footer_layout = QVBoxLayout(self.footer)
        self.footer_label = QLabel("© Developed by Sujit.")
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setStyleSheet("font-size: 16px;")
        self.footer_layout.addWidget(self.footer_label)

    def submit_clicked_1(self):
        print(">>>>>>> SUJIT---BUTTON-1 Clicked")
        subprocess.Popen(['python', 'H:\\My_Application\\matplot_qt_01082024\\matplot_qt\\1\\final_1\\PLOTTER_APP_1FIG_OFFSET.py'])

    def submit_clicked_2(self):
        print(">>>>>>> SUJIT---BUTTON-2 Clicked")
        subprocess.Popen(['python', 'H:\\My_Application\\matplot_qt_01082024\\matplot_qt\\1\\final_1\\PLOTTER_APP_D3.py'])

    def submit_clicked_3(self):
        print(">>>>>>> SUJIT---BUTTON-3 Clicked")
        subprocess.Popen(['python', 'H:\\My_Application\\matplot_qt_01082024\\matplot_qt\\1\\final_1\\PDF_GE_NEW.py'])

def MAIN():
    app = QtWidgets.QApplication(sys.argv)
    GUI_Obj = App()
    sys.exit(app.exec_())

if __name__ == "__main__":
    MAIN()
