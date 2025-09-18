from PySide6.QtCore import QSize

from PySide6.QtGui import QAction, QIcon, QIntValidator

from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QLabel, QLineEdit

from requestRoll import rollDice

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.setWindowTitle("DndQt")

        toolBar = QToolBar("diceToolBar")
        toolBar.setIconSize(QSize(40, 40))
        self.addToolBar(toolBar)
        self.initToolBar(toolBar)

    
    def initToolBar(self, toolBar : QToolBar):
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
            toolBar.addAction(action)
        toolBar.addSeparator()

        bonus = QLabel("Bonus :")
        toolBar.addWidget(bonus)

        
        onlyIntRange = QIntValidator()
        onlyIntRange.setRange(-32, 32)

        self.bonusInput = QLineEdit()
        self.bonusInput.setValidator(onlyIntRange)

        toolBar.addWidget(self.bonusInput)

        toolBar.addSeparator()

        button = QPushButton("Roll")
        button.clicked.connect(self.buttonClicked)
        toolBar.addWidget(button)

        

    def buttonClicked(self, state):
        inputText = self.bonusInput.text()

        bonus = 0
        if inputText != "":
            bonus = int(inputText)

        res = rollDice("Carian", 1, 20, bonus, "dexterite")

        print("you rolled a", res)