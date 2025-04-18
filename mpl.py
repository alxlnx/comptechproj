import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matplotlib in Qt")
        self.setup_ui()

    def setup_ui(self):
        # Create a Matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Add data to the plot
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.ax.plot(x, y, 'r-', label='sin(x)')
        self.ax.set_title("Matplotlib Plot in Qt")
        self.ax.legend()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

# Run the application
matplotlib.use('qtagg')
app = QApplication(sys.argv)
window = MatplotlibWidget()
window.show()
sys.exit(app.exec())