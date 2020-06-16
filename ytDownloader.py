from __future__ import unicode_literals
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(600, 300)
        mainWindow.setMaximumSize(QtCore.QSize(600, 300))
        mainWindow.setBaseSize(QtCore.QSize(300, 600))
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 541, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
       
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 541, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Campo de Entrada do "Output"
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")

        self.gridLayout.addWidget(self.textEdit_2, 2, 1, 1, 1)
        
        # Campo de Entrada do URL
        self.urlInput = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.urlInput.setObjectName("urlInput")

        self.gridLayout.addWidget(self.urlInput, 1, 1, 1, 1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 190, 541, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        # Barra de Progresso
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.verticalLayout_6.addWidget(self.progressBar)
        
        # Botão de Download
        self.downloadButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.downloadButton.setObjectName("downloadButton")
        self.downloadButton.clicked.connect(self.download)

        self.verticalLayout_6.addWidget(self.downloadButton)

        mainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")

        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        ## Message for Finished Download
        self.msgFinished = QtWidgets.QMessageBox()
        self.msgFinished.setIcon(QtWidgets.QMessageBox.Critical)
        self.msgFinished.setWindowTitle("Download Finished")
        self.msgFinished.setInformativeText('Your video has been downloaded')

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Youtube Downloader"))
        self.radioButton.setText(_translate("mainWindow", "Download MP4"))
        self.radioButton_2.setText(_translate("mainWindow", "Download MP3"))
        self.label.setText(_translate("mainWindow", "URL:"))
        self.label_2.setText(_translate("mainWindow", "Output:"))
        self.downloadButton.setText(_translate("mainWindow", "Download"))

    def download(self):
        Url = self.urlInput.toPlainText()
        Dir = self.textEdit_2.toPlainText()
        self.progressBar.setProperty("value", 0)

        def message(d):
            if d['status'] == 'finished':
                self.msgFinished.exec_()
                self.progressBar.setProperty("value", 100)

        if self.radioButton.isChecked():
            print('VIDEO SELECTED')
            options = {
                'format': 'best', # choice of quality
                'noplaylist' : True,        # only download single song, not playlist
                'progress_hooks': [message],
            }

        elif self.radioButton_2.isChecked():
            print('MP3 SELECTED')
            options = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],
                'noplaylist' : True,
                'progress_hooks': [message],
                'outtmpl': '{}/%(title)s.%(ext)s'.format(Dir)
            }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([Url])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
