from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QMenu, QLabel
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class Functions():
    def set_speed(self, value):
        self.mediaPlayer.setPlaybackRate(value/100)
        self.speedLabel.setText("Speed: " + str(value) + "%")

    def set_volume(self, value):
        self.mediaPlayer.setVolume(value)
        self.volumeLabel.setText("Volume: " + str(value) + "%")
    
    def reset_speed(self):
        self.mediaPlayer.setPlaybackRate(1)
        self.speed.setValue(100)
        self.speedLabel.setText("Speed: 100%")
    
    def reset_volume(self):
        self.mediaPlayer.setVolume(100)
        self.volume.setValue(100)
        self.volumeLabel.setText("Volume: 100%")

    