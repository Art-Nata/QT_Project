import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window_Code(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cod_decod.ui', self)
        self.cod_button.clicked.connect(self.cod_mess)
        self.decod_button.clicked.connect(self.decod_mess)
        self.code_table = {}

    def cod_mess(self):
        message_new = self.lineEdit.text()
        message_cod = ''
        for i in message_new:
            message_cod += self.code_table[i]
        self.lineEdit_2.setText(message_cod)

    def decod_mess(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window_Code()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
