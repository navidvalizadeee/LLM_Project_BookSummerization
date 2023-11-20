from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('UI/main.ui', self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_layout = QtWidgets.QVBoxLayout()
        self.plotWidget.setLayout(self.plot_layout)
        self.plot_layout.addWidget(self.canvas)
        self.plot()

    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])  # Example data
        self.canvas.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainWin = MyWindow()
    mainWin.show()
    app.exec_()
