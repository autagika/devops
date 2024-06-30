import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_addition2(self):
        assert 5 == calculator.add(2, 3)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_multiplication2(self):
        assert calculator.multiply(3, 5) != 19

    def test_multiplication2(self):
        assert calculator.divide(20, 5) == 4
