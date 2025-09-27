from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QLabel, QLineEdit

from DiceToolBar import DiceToolBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.setWindowTitle("DndQt")

        toolBar = DiceToolBar()
        self.addToolBar(toolBar)
