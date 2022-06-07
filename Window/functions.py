import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class Functions():
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Video Files (*.mp4 *.avi *.mkv)")
        if filename != "":
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.skip5Back.setEnabled(True)
            self.skip5Ahead.setEnabled(True)
            self.nextFrame.setEnabled(True)
            self.prevFrame.setEnabled(True)
            self.mediaPlayer.play()


    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.playBtn.setText("Pause")
        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.playBtn.setText("Play")

    def position_changed(self, position):
        self.slider.setValue(position)
        self.timer.setText("{:02d}:{:02d}".format(position // 60000, position % 60000 // 1000))
    
    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def skip_5_back(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 5000)

    def skip_5_ahead(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 5000)

    def set_speed(self, speed):
        self.mediaPlayer.setPlaybackRate(speed / 100)
    
    def next_frame(self):
        framerate = self.mediaPlayer.metaData("VideoFrameRate")
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + round(1000 / framerate))
    
    def prev_frame(self):
        framerate = self.mediaPlayer.metaData("VideoFrameRate")
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - round(1000 / framerate))
    
    def close_event(self, event):
        if self.w != None:
            self.w.close()
        self.close()