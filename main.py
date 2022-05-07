import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from ui.test import Ui_Form

# 静态载入1
class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 实例化一个 Ui_MainWindow对象
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.openImage)

    def openImage(self):
        print("dfadsf")



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec_())
