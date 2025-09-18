from PySide6.QtWidgets import QMainWindow, QPushButton

from requestRoll import rollDice

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("our first window")

        button = QPushButton("Roll")

        button.clicked.connect(self.buttonClicked)
        # button.setCheckable(True)

        self.setCentralWidget(button)

    def buttonClicked(self, state):
        res = rollDice("Carian", 1, 20, 3, "dexterite")

        print("you rolled a", res)
