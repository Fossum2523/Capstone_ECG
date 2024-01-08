import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton,QLabel,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon,QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer,Qt
import numpy as np
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = '具身份辨識之血壓計'
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.m = PlotCanvas(self)
        self.m.move(0, 0)
        self.label = QLabel(self)
        self.label.move(970,330)
        self.label.resize(900,100)
        self.label.setText("請點選註冊身分")
        self.label.setStyleSheet("font: bold 25px ;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_state = QLabel(self)
        self.label_state.move(450,30)
        self.label_state.resize(500,100)
        self.label_state.setText("請點選按鈕")
        self.label_state.setStyleSheet("font: bold 24px ;color: #FF0000;")
        self.label_state.setVisible(True)
        self.button = QPushButton('Click me', self)
        self.button.setToolTip('This s an example button')
        self.button.move(440, 130)
        self.button.setStyleSheet("background-color: #2B5DD1; color: #FFFFFF ; border-style: outset; padding: 2px ; font: bold 20px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8;")
        self.button.resize(150, 100)
        self.button.clicked.connect(self.button_change)
        self.button1 = QPushButton('Enable', self)
        self.button1.setToolTip('This s an example button')
        self.button1.move(440, 240)
        self.button1.setStyleSheet("background-color: #2B5DD1; color: #FFFFFF ; border-style: outset; padding: 2px ; font: bold 20px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8;")
        self.button1.resize(150, 100)
        self.button1.clicked.connect(self.button_disable)
        self.button_plot = QPushButton('plot', self)
        self.button_plot.setToolTip('This s an example button')
        self.button_plot.move(440, 350)
        self.button_plot.setStyleSheet("background-color: #2B5DD1; color: #FFFFFF ; border-style: outset; padding: 2px ; font: bold 20px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8;")
        self.button_plot.resize(150, 100)
        self.button_plot.clicked.connect(self.button_plot_f)
        self.show()
    def button_change(self):
        self.button.setStyleSheet("background-color: #1749BD; color: #FFFFFF ; border-style: outset; padding: 2px ; font: bold 45px ; border-width: 6px ; border-radius: 10px ; border-color: #2252B8;")
        self.label_state.setVisible(False)
        self.show()
        self.timer = QTimer(self)       
        self.timer.timeout.connect(self.button_change1)
        self.timer.start(200)
    def button_change1(self):
        self.button.setStyleSheet("background-color: #2B5DD1; color: #FFFFFF ; border-style: outset; padding: 2px ; font: bold 20px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8;")
        self.label_state.setVisible(True)
        self.timer.stop()
        self.show()
    def button_disable(self):
        self.button1.setStyleSheet("background-color:#2752B8 ; color: #FFFFFF ;  padding: 2px ; font: bold 20px  ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8;")
        self.button1.setEnabled(False)
        self.show()
    def button_plot_f(self):
        in_array = np.linspace(-np.pi, np.pi, 100) 
        x1=np.sin(in_array)
        x2=np.cos(in_array)
        self.m.plot_sin(x1,x2)
        self.show()
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=6, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.subplots_adjust(0.1, 0.1, 0.9, 0.9)
        #fig.patch.set_facecolor((0.1, 0.2, 0.5,0.3))
        self.axes = fig.add_subplot(211)
        #self.axes.patch.set_facecolor((0.1, 0.2, 0.5,0.05))
        self.axes1 = fig.add_subplot(212)
        #self.axes1.patch.set_facecolor((0.1, 0.2, 0.5,0.05))
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.init_plot()


    def init_plot(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        self.axes.plot(x, y,'r')
        self.axes1.plot(x, y,'r')
    def plot_sin(self,x1,x2):
        self.axes.cla()
        self.axes.plot(x1,'r')
        self.axes1.cla()
        self.axes1.plot(x2,'r')
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

