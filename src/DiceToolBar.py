from PySide6.QtGui import QAction, QIcon, QIntValidator
from PySide6.QtWidgets import QToolBar, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QSize

from requestRoll import rollDice

class DiceToolBar(QToolBar):
    def __init__(self):
        super().__init__("diceToolBar")

        self.setIconSize(QSize(40, 40))

        dice = [
            ("D20", "img/D20.png", "Add a D20"),
            ("D12", "img/D12.png", "Add a D12"),
            ("D10", "img/D10.png", "Add a D10"),
            ("D8",  "img/D8.png",  "Add a D8"),
            ("D6",  "img/D6.png",  "Add a D6"),
            ("D4",  "img/D4.png",  "Add a D4"),
        ]

        for name, icon, tip in dice:
            action = QAction(QIcon(icon), name, self)
            action.setToolTip(tip)
            self.addAction(action)
        self.addSeparator()

        self.addSeparator()

        bonus = QLabel("Bonus :")
        self.addWidget(bonus)
        
        onlyIntRange = QIntValidator()
        onlyIntRange.setRange(-32, 32)

        self.bonusInput = QLineEdit()
        self.bonusInput.setValidator(onlyIntRange)

        self.addWidget(self.bonusInput)

        self.addSeparator()

        button = QPushButton("Roll")
        button.clicked.connect(self.__buttonClicked__)
        self.addWidget(button)

    def __buttonClicked__(self):
        inputText = self.bonusInput.text()

        bonus = 0
        if inputText != "":
            bonus = int(inputText)

        res = rollDice("Carian", 1, 20, bonus, "dexterite")

        print("you rolled a", res)