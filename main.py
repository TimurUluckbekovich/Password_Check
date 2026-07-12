import sys
from PyQt6.QtWidgets import QApplication
from models import Window

class PasswordCheck:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Window()

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    PasswordCheck().run()


