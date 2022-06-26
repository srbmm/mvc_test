from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self, stu_lis):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Student App')
        self.setMinimumSize(600, 400)
        widget = CenteralWidget(stu_lis)
        self.setCentralWidget(widget)


class CenteralWidget(QWidget):
    def __init__(self,stu_list):
        super(CenteralWidget, self).__init__()
        lay = QGridLayout()
        self.setLayout(lay)
        lay.addWidget(QLabel('name', self), 1, 1)
        lay.addWidget(QLabel('id', self), 1, 2)
        for i in range(len(stu_list)):
            lay.addWidget(QLabel(stu_list[i][0]),(i+2), 1)
            lay.addWidget(QLabel(stu_list[i][1]), (i+2), 2)
