from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loader = QUiLoader()
window = loader.load("test.ui")  # Path to your .ui file
window.show()
app.exec()