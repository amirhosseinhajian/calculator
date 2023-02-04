import math
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("front.ui")
        self.ui.setWindowTitle("Qt Calculator")
        self.ui.show()
        self.numbers = [self.ui.btn_0, self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4,
                        self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]
        self.ui.btn_sum.clicked.connect(self.add)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_ac.clicked.connect(self.ac)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.btn_module.clicked.connect(self.mod)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_sub.clicked.connect(self.subb)
        self.ui.btn_log.clicked.connect(self.log)
        for i in range(10):
            self.numbers[i].clicked.connect(partial(self.num_btn_press, str(i)))
        self.ui.btn_dot.clicked.connect(partial(self.num_btn_press, "."))

    def get_num1(self):
        self.num1 = float(self.ui.tb1.text())
        self.ui.tb1.setText("")

    def add(self):
        try:
            self.get_num1()
            self.operation = "+"
        except:
            self.ui.tb1.setText("Not valid number!")

    def subb(self):
        try:
            self.get_num1()
            self.operation = "-"
        except:
            self.ui.tb1.setText("Not valid number!")

    def div(self):
        try:
            self.get_num1()
            self.operation = "/"
        except:
            self.ui.tb1.setText("Not valid number!")

    def mul(self):
        try:
            self.get_num1()
            self.operation = "*"
        except:
            self.ui.tb1.setText("Not valid number!")

    def mod(self):
        try:
            self.get_num1()
            self.operation = "%"
        except:
            self.ui.tb1.setText("Not valid number!")

    def sign(self):
        try:
            self.num1 = float(self.ui.tb1.text())
            self.ui.tb1.setText(str(int(-self.num1))) if Calculator.is_int(self.num1) else self.ui.tb1.setText(str(-self.num1))
        except:
            self.ui.tb1.setText("Not valid number!")

    def ac(self):
        self.ui.tb1.setText("0")

    def sin(self):
        try:
            self.num1 = round(math.sin(math.radians(float(self.ui.tb1.text()))), 10)
            self.ui.tb1.setText(str(int(self.num1))) if Calculator.is_int(self.num1) else self.ui.tb1.setText(str(self.num1))
        except:
            self.ui.tb1.setText("Not valid number!")

    def cos(self):
        try:
            self.num1 = round(math.cos(math.radians(float(self.ui.tb1.text()))), 10)
            self.ui.tb1.setText(str(int(self.num1))) if Calculator.is_int(self.num1) else self.ui.tb1.setText(str(self.num1))
        except:
            self.ui.tb1.setText("Not valid number!")

    def tan(self):
        try:
            self.num1 = round(math.tan(math.radians(float(self.ui.tb1.text()))), 10)
            self.ui.tb1.setText(str(int(self.num1))) if Calculator.is_int(self.num1) else self.ui.tb1.setText(str(self.num1))
        except:
            self.ui.tb1.setText("Not valid number!")

    def cot(self):
        try:
            self.num1 = round(1 / math.tan(math.radians(float(self.ui.tb1.text()))), 10)
            self.ui.tb1.setText(str(int(self.num1))) if Calculator.is_int(self.num1) else self.ui.tb1.setText(str(self.num1))
        except:
            self.ui.tb1.setText("Not valid number!")

    def log(self):
        try:
            self.num1 = round(math.log(float(self.ui.tb1.text()), 10), 10)
            self.ui.tb1.setText(str(int(self.num1))) if Calculator.is_int(self.num1) else self.ui.tb1.setText(str(self.num1))
        except:
            self.ui.tb1.setText("Not valid number!")

    def sqrt(self):
        try:
            self.num1 = round(math.sqrt(float(self.ui.tb1.text())), 10)
            self.ui.tb1.setText(str(int(self.num1))) if Calculator.is_int(self.num1) else self.ui.tb1.setText(str(self.num1))
        except:
            self.ui.tb1.setText("Not valid number!")
    
    @staticmethod
    def is_int(number):
        if number - math.floor(number) == 0:
            return True
        return False

    def equal(self):
        self.num2 = float(self.ui.tb1.text())
        try:
            if self.operation == "+":
                result = self.num1 + self.num2
            elif self.operation == "-":
                result = self.num1 - self.num2
            elif self.operation == "*":
                result = self.num1 * self.num2
            elif self.operation == "/":
                result = self.num1 / self.num2
            elif self.operation == "%":
                result = self.num1 % self.num2
            self.ui.tb1.setText(str(int(result))) if Calculator.is_int(result) else self.ui.tb1.setText(str(result))
        except:
            self.ui.tb1.setText("Not valid number!")

    def num_btn_press(self, n):
        self.num = self.ui.tb1.text()
        if self.num != '0':
            self.ui.tb1.setText(self.num + n)
        elif self.num=='0' and n == '.':
            self.ui.tb1.setText(self.num + n)
        else:
            self.ui.tb1.setText(n)

if __name__ == "__main__":
    app = QApplication()
    calculator_main_window = Calculator()
    app.exec()