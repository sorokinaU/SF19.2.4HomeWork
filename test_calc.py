import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 1) == 9

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_success(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError): # raises для обработки исключений, with ключевое слово
            self.calc.division(self, 1, 0)

    def teardown(self): # метод teardown для закрытия любой функции
        print('Выполнение метода Teardown')