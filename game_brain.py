class Board:
    def __init__(self):
        self.reset_board()
        self.refresh_board()


    def reset_board(self):
        self.a1 = "-"
        self.a2 = "-"
        self.a3 = "-"
        self.b1 = "-"
        self.b2 = "-"
        self.b3 = "-"
        self.c1 = "-"
        self.c2 = "-"
        self.c3 = "-"

        self.game_is_over = False
        self.is_draw = False
        self.winner = None

    def refresh_board(self):
        self.row_1 = [self.a1, self.b1, self.c1]
        self.row_2 = [self.a2, self.b2, self.c2]
        self.row_3 = [self.a3, self.b3, self.c3]

        self.col_a = [self.a1, self.a2, self.a3]
        self.col_b = [self.b1, self.b2, self.b3]
        self.col_c = [self.c1, self.c2, self.c3]

        self.diag_1 = [self.a3, self.b2, self.c1]
        self.diag_2 = [self.a1, self.b2, self.c3]

        self.rows = [self.row_1, self.row_2, self.row_3]
        self.columns = [self.col_a, self.col_b, self.col_c]
        self.diagonals = [self.diag_1, self.diag_2]
        self.cells = [
            self.a1,
            self.a2,
            self.a3,
            self.b1,
            self.b2,
            self.b3,
            self.c1,
            self.c2,
            self.c3,
        ]

        self.board = f"""
               |     |     
        3   {self.a3}  |  {self.b3}  |  {self.c3}  
          _____|_____|_____
               |     |     
        2   {self.a2}  |  {self.b2}  |  {self.c2}  
          _____|_____|_____
               |     |     
        1   {self.a1}  |  {self.b1}  |  {self.c1}  
               |     |   
            A     B     C   
        """

    def display(self):
        print(self.board)

    def evaluate(self):
        for col in self.columns:
            if col[0] == col[1] and col[1] == col[2]:
                if col[0] == "X":
                    self.winner = "Player 1 (X)"
                    self.game_is_over = True
                    return
                elif col[0] == "O":
                    self.winner = "Player 2 (O)"
                    self.game_is_over = True
                    return

        for row in self.rows:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] == "X":
                    self.winner = "Player 1 (X)"
                    self.game_is_over = True
                    return
                elif row[0] == "O":
                    self.winner = "Player 2 (O)"
                    self.game_is_over = True
                    return

        for diagonal in self.diagonals:
            if diagonal[0] == diagonal[1] and diagonal[1] == diagonal[2]:
                if diagonal[0] == "X":
                    self.winner = "Player 1 (X)"
                    self.game_is_over = True
                    return
                elif diagonal[0] == "O":
                    self.winner = "Player 2 (O)"
                    self.game_is_over = True
                    return

        if "-" not in self.cells:
            self.is_draw = True
            self.game_is_over = True




class Player:
    def __init__(self, nature):

        if nature != "x" and nature != "o":
            raise ValueError("Invalid 'nature' argument. Expected 'x' or 'o'.")

        self.identity = nature.upper()

    def play(self, board, position):
        position = position.lower()

        if getattr(board, position) != "-":
            return False

        setattr(board, position, self.identity)
        board.refresh_board()
        return True
