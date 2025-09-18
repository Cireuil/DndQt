from PySide6.QtWidgets import QApplication
import sys

from buttonHolder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()

app.exec()