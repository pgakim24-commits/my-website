import unittest

from calculator import calculate


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        result, err = calculate(1, '+', 2)
        self.assertIsNone(err)
        self.assertEqual(result, 3)

    def test_subtraction(self):
        result, err = calculate(10, '-', 4)
        self.assertIsNone(err)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result, err = calculate(3, '*', 5)
        self.assertIsNone(err)
        self.assertEqual(result, 15)

    def test_division(self):
        result, err = calculate(8, '/', 2)
        self.assertIsNone(err)
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        result, err = calculate(8, '/', 0)
        self.assertIsNone(result)
        self.assertEqual(err, '0으로 나눌 수 없습니다')

    def test_power(self):
        result, err = calculate(2, '**', 8)
        self.assertIsNone(err)
        self.assertEqual(result, 256)

    def test_modulo(self):
        result, err = calculate(10, '%', 3)
        self.assertIsNone(err)
        self.assertEqual(result, 1)

    def test_modulo_by_zero(self):
        result, err = calculate(10, '%', 0)
        self.assertIsNone(result)
        self.assertEqual(err, '0으로 나눌 수 없습니다')

    def test_unknown_operator(self):
        result, err = calculate(1, '?', 2)
        self.assertIsNone(result)
        self.assertEqual(err, '지원하지 않는 연산자: ?')

    def test_negative_numbers(self):
        result, err = calculate(-5, '+', 3)
        self.assertIsNone(err)
        self.assertEqual(result, -2)

    def test_float_division(self):
        result, err = calculate(7, '/', 2)
        self.assertIsNone(err)
        self.assertEqual(result, 3.5)


if __name__ == '__main__':
    unittest.main()
