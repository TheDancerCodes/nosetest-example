"""Tests For a simple Calculator App."""
import unittest
from app.calculator import Calculator


class TddPythonExample(unittest.TestCase):
    """The Test Class."""

    def test_calculator_add_method_returns_correct_result(self):
        """Test For Add Method."""
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
