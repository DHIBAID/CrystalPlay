
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QMenu, QLabel, QGridLayout
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class UI():
    def create_ui(self):

        self.speedLabel = QLabel("Speed: 100%")
        self.speedLabel.setAlignment(Qt.AlignCenter)
        speedPalette = self.speedLabel.palette()
        speedPalette.setColor(QPalette.WindowText, Qt.white)
        self.speedLabel.setPalette(speedPalette)

        
        self.speed = QSlider(Qt.Vertical)
        self.speed.setRange(1, 200)
        self.speed.setValue(100)
        self.speed.setToolTip("Speed of the video")
        self.speed.valueChanged.connect(self.set_speed)

        self.speedReset = QPushButton("Reset Speed")
        self.speedReset.clicked.connect(self.reset_speed)


        
        QSS = """
            QSlider::handle:vertical:hover {
                background-color: rgb(255, 255, 255);
                border-radius: 3px;
            }
            """
        self.speed.setStyleSheet(QSS)      

        self.volumeLabel = QLabel("Volume: 100%")
        self.volumeLabel.setAlignment(Qt.AlignCenter)
        volumePalette = self.volumeLabel.palette()
        volumePalette.setColor(QPalette.WindowText, Qt.white)
        self.volumeLabel.setPalette(volumePalette)

        self.volume = QSlider(Qt.Vertical)
        self.volume.setRange(0, 150)
        self.volume.setValue(100)
        self.volume.setToolTip("Volume of the video")
        self.volume.valueChanged.connect(self.set_volume)

        self.volumeReset = QPushButton("Reset Volume")
        self.volumeReset.clicked.connect(self.reset_volume)


        layout = QGridLayout()
        layout.addWidget(self.speedLabel, 0, 0)
        layout.addWidget(self.speed, 0, 1)
        layout.addWidget(self.speedReset, 0, 2)
        layout.addWidget(self.volumeLabel, 1, 0)
        layout.addWidget(self.volume, 1, 1)
        layout.addWidget(self.volumeReset, 1, 2)

        self.setLayout(layout)