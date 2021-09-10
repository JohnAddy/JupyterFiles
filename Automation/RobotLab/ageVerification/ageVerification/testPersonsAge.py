import unittest
import ageOfPerson


class MyTest(unittest.TestCase):

    def test_PersonAge_under_18(self):
        # Arrange
        a = int(17)

        # Act
        receive = ageOfPerson.personAge(a)

        # Assert
        self.assertEqual("You are Child", receive)

    def test_PersonAge_under_70(self):
        # Arrange
        a = int(61)

        # Act
        receive = ageOfPerson.personAge(a)

        # Assert
        self.assertEqual("You are an adult", receive)

    def test_PersonAge_over_70(self):
        # Arrange
        a = int(60)

        # Act
        receive = ageOfPerson.personAge(a)

        # Assert
        self.assertEqual("You are a pensioner", receive)


if __name__ == '__main__':
    unittest.main()
