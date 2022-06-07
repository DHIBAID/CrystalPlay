from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QMenu, QLabel
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class UI():
    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        videowidget = QVideoWidget()

        self.openBtn = QPushButton(" Open Video")
        self.openBtn.setIcon(QIcon("assets/videoFile.png"))
        self.openBtn.setToolTip("Open a Video file from your computer.")
        self.openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton("Play")
        self.playBtn.setEnabled(False)
        self.playBtn.clicked.connect(self.play_video)
        self.playBtn.setToolTip("Click to play a selected video.")
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.skip5Back = QPushButton("Seek 5 Back")
        self.skip5Back.setToolTip("Skip 5 seconds back in the video.")
        self.skip5Back.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.skip5Back.clicked.connect(self.skip_5_back)
        self.skip5Back.setEnabled(False)

        self.skip5Ahead = QPushButton("Seek 5 Ahead")
        self.skip5Ahead.setToolTip("Skip 5 seconds ahead in the video.")
        self.skip5Ahead.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.skip5Ahead.clicked.connect(self.skip_5_ahead)
        self.skip5Ahead.setEnabled(False)


        self.nextFrame = QPushButton("Next frame")
        self.nextFrame.setToolTip("Skip to the next frame in the video.")
        self.nextFrame.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.nextFrame.clicked.connect(self.next_frame)
        self.nextFrame.setEnabled(False)

        self.prevFrame = QPushButton("Previous Frame")
        self.prevFrame.setToolTip("Skip to the previous frame in the video.")
        self.prevFrame.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.prevFrame.clicked.connect(self.prev_frame)
        self.prevFrame.setEnabled(False)

        self.advancedMenu = QPushButton("Advanced Menu")
        self.advancedMenu.setToolTip("Open the advanced menu for more features.")
        self.advancedMenu.setIcon(self.style().standardIcon(QStyle.SP_VistaShield))
        self.advancedMenu.clicked.connect(self.advanced_menu)

        self.timer = QLabel("00:00")
        self.timer.setFixedWidth(100)
        self.timer.setAlignment(Qt.AlignCenter)
        timer_palette = self.timer.palette()
        timer_palette.setColor(QPalette.WindowText, Qt.white)
        self.timer.setToolTip("Current time in the video.")
        self.timer.setPalette(timer_palette)



        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self.openBtn)
        hbox2.addWidget(self.skip5Back)
        hbox2.addWidget(self.playBtn)
        hbox2.addWidget(self.skip5Ahead)
        hbox2.addWidget(self.prevFrame)
        hbox2.addWidget(self.nextFrame)
        hbox2.addWidget(self.advancedMenu)

        timeline = QHBoxLayout()
        timeline.setContentsMargins(0,0,0,0)
        timeline.addWidget(self.timer)
        timeline.addWidget(self.slider)

        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(videowidget)
        vbox.addLayout(timeline)
        vbox.addLayout(hbox2)

        self.mediaPlayer.setVideoOutput(videowidget)

        self.setLayout(vbox)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
