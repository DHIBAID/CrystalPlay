import sys
from Window.functions import Functions
from Window.ui import UI
from Advanced.ui import UI as AdvancedUI
from Advanced.functions import Functions as AdvancedFunctions
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QLabel
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class Window(UI, Functions, QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crystal Play")
        self.setWindowIcon(QIcon("assets/icon.ico"))
        self.setGeometry(300, 300, 700, 500)
        p = self.palette()
        p.setColor(QPalette.Window, QColor(48, 48, 48))
        self.setPalette(p)
        self.w = None
        self.create_player()

        self.closeEvent = self.close_event

    def advanced_menu(self):
        if self.w == None:
            self.w = Advanced_Menu(mediaplayer=self.mediaPlayer)
            self.w.show()
            


class Advanced_Menu(QWidget, AdvancedUI, AdvancedFunctions):
    def __init__(self, mediaplayer):
        super().__init__()
        self.setWindowTitle("Advanced Menu")
        self.setWindowIcon(QIcon("assets/icon.ico"))
        self.setGeometry(300, 300, 700, 500)
        p = self.palette()
        p.setColor(QPalette.Window, QColor(48, 48, 48))
        self.setPalette(p)
        self.create_ui()
        self.mediaPlayer = mediaplayer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())