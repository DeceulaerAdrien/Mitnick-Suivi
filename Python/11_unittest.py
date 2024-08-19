import unittest

def add(number_one: int, number_two: int) -> int:
    return number_one + number_two


def multiply(number_one: int, number_two: int) -> int:
    return number_one * number_two


def add_and_multiply(number_one: int, number_two: int) -> int:
    addition_result = add(number_one, number_two)
    multiplying_result = multiply(number_one, number_two)

    result = add(addition_result, multiplying_result)
    return result


# Unit testing
class TestMathFunctions(unittest.TestCase):
    """Class that will test all the math related functions."""

    def test_add(self):
        """Test the add function."""
        test_1 = add(1, 1)
        test_2 = add(2, 3)
        test_3 = add(5, 5)

        assert test_1 == 2
        assert test_2 == 5
        assert test_3 == 10

    def test_multiply(self):
        """Test the multiply function."""
        test_1 = multiply(1, 1)
        test_2 = multiply(2, 3)
        test_3 = multiply(5, 5)

        assert test_1 == 1
        assert test_2 == 6
        assert test_3 == 25

    def test_add_and_multiply(self):
        """Test the add_and_multiply function."""
        test_1 = add_and_multiply(2, 4)

        assert test_1 == 14


if __name__ == "__main__":
    unittest.main()

