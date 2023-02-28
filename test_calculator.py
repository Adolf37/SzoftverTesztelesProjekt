import calculator

def test_calc_addition():
    output = calculator.add(2,3)
    assert output == 5

def test_calc_substraction():
    output = calculator.substract(5,3)
    assert output == 2

def test_calc_multiply():
    output = calculator.multiply(2,3)
    assert output == 6
