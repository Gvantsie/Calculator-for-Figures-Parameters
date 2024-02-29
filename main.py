import sys

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from design import Ui_MainWindow
import math



class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # loadUi('calculator.ui', self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main))

    def select_shape(self):
        shape_name = self.shape_group.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main)
        )

        self.calculate.clicked.connect(self.calculate_area)

    def calculate_area(self):
        shape_name = self.shape_group.checkedButton().objectName()

        if shape_name == 'kvadrati':
            side_length = float(self.k1.value())

            perimeter = float(4 * side_length)
            self.lcd_k_perimeter.display(perimeter)
            area = float(side_length ** 2)
            self.lcd_k_area.display(area)

        elif shape_name == 'samkutxedi':
            side1 = float(self.s1.value())
            side2 = float(self.s2.value())
            side3 = float(self.s3.value())

            perimeter = float(side1 + side2 + side3)
            self.lcd_s_perimeter.display(perimeter)
            p = (side1 + side2 + side3) / 2
            area = float((p * (p - side1) * (p - side2) * (p - side3)) ** 0.5)
            self.lcd_s_area.display(area)

        elif shape_name == 'trapecia':
            side1 = float(self.t1.value())
            side2 = float(self.t2.value())
            side3 = float(self.t3.value())
            side4 = float(self.t4.value())
            height = float(self.th.value())

            perimeter = float(side1 + side2 + side3 + side4)
            self.lcd_t_perimeter.display(perimeter)
            area = float(0.5 * height * (side1 + side2))
            self.lcd_t_area.display(area)

        elif shape_name == 'wre':
            radius = float(self.r1.value())

            # realurad xom arasdros vwert pis mnishvnelobas da ase
            # chavwere, magram gamaxsenda rom lcd box gvakvs :)
            # perimeter = float(2 * radius)
            # self.lcd_r_perimeter.display(str(perimeter) + "π")
            # area = float((radius ** 2))
            # self.lcd_r_area.display(str(area) + "π")

            perimeter = float(2 * math.pi * radius)
            self.lcd_r_perimeter.display(perimeter)
            area = float( math.pi * (radius**2))
            self.lcd_r_area.display(area)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()
    window.setWindowTitle("Weird Calculator")
    window.setFixedSize(800, 600)

    sys.exit(app.exec_())
