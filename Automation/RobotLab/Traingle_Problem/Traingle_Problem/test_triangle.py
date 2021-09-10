import unittest
import triangle_problem


class MyTest(unittest.TestCase):

    def test_equilateral_triangle(self):
        # Arrange
        x = int(10)
        y = int(10)
        z = int(10)

        # Act
        receive = triangle_problem.side(x, y, z)

        # Assert
        self.assertEqual('equilateral', receive)

    def test_isosceles_triangle(self):
        # Arrange
        x = int(8)
        y = int(8)
        z = int(5)

        # Act
        receive = triangle_problem.side(x, y, z)

        # Assert
        self.assertEqual('isosceles', receive)

    def test_irregular_triangle(self):
        # Arrange
        x = int(8)
        y = int(6)
        z = int(7)

        # Act
        receive = triangle_problem.side(x, y, z)

        # Assert
        self.assertEqual('irregular', receive)


if __name__ == '__main__':
    unittest.main()
