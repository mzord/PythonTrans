from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel
import sys

from Translator import Translator


Stylesheet = """
#Custom_Widget {
    background: #733fa1;
    border-radius: 20px;
    opacity: 100;
    border: 2px solid #ff2025;                   
}
#closeButton {
    min-width: 36px;
    min-height: 36px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: #ccc;
    background: red;
}
"""

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traduire")
        self.resize(400, 40)
        self.UI()
        self.setObjectName("Custom_Widget")
        self.setStyleSheet(Stylesheet)

        self.tr = Translator("fr")

    def UI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        # Label Field
        self.label = QLabel(self)
        layout.addWidget(self.label)

        # Form Field
        self.form = QLineEdit(self)
        self.form.setPlaceholderText("Traduire")
        layout.addWidget(self.form)

        self.show()

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        if event.key() == QtCore.Qt.Key_Return:
            self.label.setText(self.tr.translate(self.form.text()))



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

