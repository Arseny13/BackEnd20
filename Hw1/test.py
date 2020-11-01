import unittest
from game import TicTacGame

class TicTacGameTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """Создание экземпляра игры"""
        self.game = TicTacGame()

    def test_filling_array(self) -> None:
        """Тестирование заполнения массива"""
        self.game.filling_board(0, 0)
        self.game.filling_board(1, 1)
        self.assertNotEqual(self.game.mas[0][0], 0)
        self.assertNotEqual(self.game.mas[1][1], 0)

    def test_check_winner_continue(self) -> None:
        """Тестирование продолжение игры"""
        self.game.mas[0][0] = 'X'
        self.game.mas[1][0] = 'O'
        result = self.game.check_winner('X')
        self.assertEqual(result, False)

    def test_check_winner_diagonal(self) -> None:
        """Тестирование проверка по диагоняли)"""
        self.game.mas[0][0] = 'X'
        self.game.mas[1][1] = 'X'
        self.game.mas[2][2] = 'X'
        result = self.game.check_winner('X')
        self.assertEqual(result, 'X')

    def test_check_winner_row(self) -> None:
        """Тестирование проверка по строке"""
        self.game.mas[0][0] = 'X'
        self.game.mas[0][1] = 'X'
        self.game.mas[0][2] = 'X'
        result = self.game.check_winner('X')
        self.assertEqual(result, 'X')

    def test_check_winner_col(self) -> None:
        """Тестирование проверка по столбцу"""
        self.game.mas[0][0] = 'X'
        self.game.mas[1][0] = 'X'
        self.game.mas[2][0] = 'X'
        result = self.game.check_winner('X')
        self.assertEqual(result, 'X')

    def test_check_winner_draw(self) -> None:
        """Тестирование ничья"""
        self.game.mas[0][0] = 'X'
        self.game.mas[0][1] = 'X'
        self.game.mas[1][2] = 'X'
        self.game.mas[2][1] = 'X'
        self.game.mas[2][0] = 'X'
        self.game.mas[0][2] = 'O'
        self.game.mas[1][0] = 'O'
        self.game.mas[1][1] = 'O'
        self.game.mas[2][2] = 'O'
        result = self.game.check_winner('X')
        self.assertEqual(result, 'Draw')


if __name__ == '__name__':
    unittest.main()