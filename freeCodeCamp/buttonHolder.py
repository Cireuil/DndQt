from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("our first window")

        button = QPushButton("Press me")

        button.clicked.connect(self.buttonClicked)
        button.setCheckable(True)

        self.setCentralWidget(button)

    def buttonClicked(self, state):
        print("you clicked me didnt you !", state)
