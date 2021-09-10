import unittest
import rock_paper_scissors


class MyTest(unittest.TestCase):

    def test_rock_vs_scissors(self):
        ##Arrange

        # Act
        receive = rock_paper_scissors.check()

        # Assert
        self.assertEqual('You Won!', receive)


if __name__ == '__main__':
    unittest.main()
