from random import randint
class TicTacGame:
    """Класс игры Крестики-нолики"""

    def __init__(self):
        """Создание доски"""
        self.mas = [[0] * 3 for _ in range(3)]
        self.query = 0
        self.game_over = False
        self.vs_comp = False

    def start_game(self) :
        """Метод запуска игры"""
        while True:
            answer = input("Против компютера y/n? ")
            if answer == 'y':
                self.vs_comp = True
                break
            elif answer == 'n':
                break
            else:
                print("Введите либо y (Yes) или n(No)")

        while not self.game_over:
            self.event_handler()
            self.show_board()
            if (self.query - 1) % 2 == 0:
                self.game_over = self.check_winner('X')
            else:
                self.game_over = self.check_winner('O')

            self.check_game_over()

    def show_board(self):
        """Метод отрисовки игрового поля"""
        for row in range(3):
            print("| ",end=' ')
            for col in range(3):
                if self.mas[row][col] == 'X':
                    print("x",end=' ')
                elif self.mas[row][col] == 'O':
                    print("o",end=' ')
                else:
                    print (" ",end=' ')
            print(" |")

    def get_poss(self):
        try:
            poss = input().split()
            poss = [int(q) for q in poss]
            self.filling_board(poss[0]-1, poss[1] - 1)
            print("позиция ", poss[0] , poss[1])
        except (IndexError, ValueError):
            print('Неправильный формат ввода!')

    def event_handler(self):
        """Метод обратоки хода"""

        if self.vs_comp:
            if self.query % 2 == 0:
                print('Ход игрока')
            else:
                self.computer_move()
            self.get_poss()

        else:
            if self.query % 2 == 0:
                print('Ход 1 игрока')
            else:
                print('Ход 2 игрока')
            self.get_poss()



    def filling_board(self, row: int, col: int) -> None:
        """Метод заполнения поля"""
        if self.mas[row][col] == 0:
            if self.query % 2 == 0:
                self.mas[row][col] = 'X'
            else:
                self.mas[row][col] = 'O'
            self.query += 1

    def can_win(self, p1, p2, p3, smb):
        """Метод обработки может ли компьютер выиграть"""

        if p1 == smb and p2 == smb and p3 == 0:
            p3 = 'O'
            return True
        if p1 == smb and p2 == 0 and p3 == smb:
            p2 = 'O'
            return True
        if p1 == 0 and p2 == smb and p3 == smb:
            p1 = 'O'
            return True
        return False

    def computer_move(self):
        """Метод хода компбьтера"""

        for char in ('O','X'):
            for n in range(3):
                if self.can_win(self.mas[n][0], self.mas[n][1], self.mas[n][2], char):
                    return
                if self.can_win(self.mas[0][n], self.mas[1][n], self.mas[2][n], char):
                    return
            if self.can_win(self.mas[0][0], self.mas[1][1], self.mas[2][2], char):
                return
            if self.can_win(self.mas[2][0], self.mas[1][1], self.mas[0][2], char):
                return
        while True:
            row = randint(0, 2)
            col = randint(0, 2)
            if self.mas[row][col] == 0:
                self.mas[row][col] = 'O'
                self.query += 1
                break
        self.show_board()


    def check_game_over(self) -> None:
        """Метод обратоки конца игры"""
        if self.game_over:
            if (self.query - 1) % 2 == 0:
                print("Выиграл X")
            else:
                print("Выиграл O")
            self.game_over = True


    def check_winner(self, sign: str):
        """Метод определения победителя"""
        zeroes = 0
        for row in self.mas:
            zeroes += row.count(0)
            if row.count(sign) == 3:
                return sign

        for col in range(3):
            if (
                    self.mas[0][col] == sign
                    and self.mas[1][col] == sign
                    and self.mas[2][col] == sign
            ):
                return sign

        if (
                self.mas[0][0] == sign
                and self.mas[1][1] == sign
                and self.mas[2][2] == sign
        ):
            return sign

        if (
                self.mas[0][2] == sign
                and self.mas[1][1] == sign
                and self.mas[2][0] == sign
        ):
            return sign

        if zeroes == 0:
            return 'Draw'

        return False

if __name__ == '__main__':
        game = TicTacGame()
        game.start_game()
