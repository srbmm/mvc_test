from PyQt5.QtWidgets import QApplication, QMainWindow
from model import Students
from view import MainWindow


# Test
test = Students()
test.add('Matin', '226')
test.add('Mamad', '77')
test.add('nima', '44')
test.add('Hamed', '7789')
stu_list = test.list()


app = QApplication([])
win = MainWindow(stu_list)
win.show()
app.exec()
