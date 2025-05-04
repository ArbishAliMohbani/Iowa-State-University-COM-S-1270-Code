import pytest
from fourInSequence import createBoard, placePiece, getPlayerPiece, checkForNextMoveWin, checkAdjacent, checkDraw, checkWinner

class TestConnectFourFunctions:

    def setup_method(self):
        # Set up fresh board before each test
        self.board = createBoard(7, 6)
        self.empty = getPlayerPiece(0)
        self.p1_piece = getPlayerPiece(1) 
        self.p2_piece = getPlayerPiece(2)  
        
    def test_checkWinner_horizontal(self):
        # Place four player 1 pieces in a horizontal row
        for col in range(4):
            placePiece(self.board, 5, col, self.p1_piece)
            
        assert checkWinner(self.board, 1) == True
        assert checkWinner(self.board, 2) == False
        
    def test_checkWinner_vertical(self):
        # Place four player 2 pieces in a vertical column
        for row in range(2, 6):
            placePiece(self.board, row, 3, self.p2_piece)
            
        assert checkWinner(self.board, 2) == True
        assert checkWinner(self.board, 1) == False
        
    def test_checkWinner_diagonal_negative(self):
        # Place a negative diagonal of player 1 pieces
        for i in range(4):
            placePiece(self.board, i + 2, i, self.p1_piece)
            
        assert checkWinner(self.board, 1) == True
        assert checkWinner(self.board, 2) == False
        
    def test_checkWinner_diagonal_positive(self):
        # Place a positive diagonal of player 2 pieces
        for i in range(4):
            placePiece(self.board, 5 - i, i, self.p2_piece)
            
        assert checkWinner(self.board, 2) == True
        assert checkWinner(self.board, 1) == False
        
    def test_checkWinner_no_win(self):
        # Place some random pieces that don't form a winning pattern
        placePiece(self.board, 5, 0, self.p1_piece)
        placePiece(self.board, 5, 2, self.p1_piece)
        placePiece(self.board, 5, 4, self.p1_piece)
        placePiece(self.board, 5, 6, self.p1_piece)
        
        assert checkWinner(self.board, 1) == False
        assert checkWinner(self.board, 2) == False
        
    def test_checkDraw_empty_board(self):
        # Test that an empty board is not a draw
        assert checkDraw(self.board) == False
        
    def test_checkDraw_full_board(self):
        # Fill the entire board with alternating pieces
        for row in range(6):
            for col in range(7):
                piece = self.p1_piece if (row + col) % 2 == 0 else self.p2_piece
                placePiece(self.board, row, col, piece)
                
        assert checkDraw(self.board) == True
        
    def test_checkDraw_partial_board(self):
        # Fill only part of the board
        for row in range(4, 6):
            for col in range(7):
                piece = self.p1_piece if (row + col) % 2 == 0 else self.p2_piece
                placePiece(self.board, row, col, piece)
                
        assert checkDraw(self.board) == False
        
    def test_checkForNextMoveWin_horizontal(self):
        # Place three player 1 pieces in a row with an empty space for a win
        placePiece(self.board, 5, 0, self.p1_piece)
        placePiece(self.board, 5, 1, self.p1_piece)
        placePiece(self.board, 5, 2, self.p1_piece)
        
        # The winning move would be at column 3
        assert checkForNextMoveWin(self.board, 1) == 3
        
    def test_checkForNextMoveWin_vertical(self):
        # Place three player 2 pieces in a column with a space for a win
        placePiece(self.board, 5, 3, self.p2_piece)
        placePiece(self.board, 4, 3, self.p2_piece)
        placePiece(self.board, 3, 3, self.p2_piece)
        
        # The winning move would be at column 3
        assert checkForNextMoveWin(self.board, 2) == 3
        
    def test_checkForNextMoveWin_no_win(self):
        # Place some pieces that don't create a potential winning move
        placePiece(self.board, 5, 0, self.p1_piece)
        placePiece(self.board, 5, 2, self.p1_piece)
        placePiece(self.board, 5, 4, self.p2_piece)
        
        assert checkForNextMoveWin(self.board, 1) == -1
        assert checkForNextMoveWin(self.board, 2) == -1
        
    def test_checkAdjacent_single_adjacent(self):
        # Place a piece and test if the function detects adjacent spaces
        placePiece(self.board, 5, 3, self.p1_piece)
        
        # We need to monkey patch the random choice to make it deterministic
        import random
        random.seed(42)  # Set a fixed seed for reproducibility
        
        result = checkAdjacent(self.board, 1)
        assert result in [2, 4], f"Expected column 2 or 4, got {result}"
        
    def test_checkAdjacent_multiple_adjacent(self):
        # Create a board state with multiple adjacencies
        placePiece(self.board, 5, 2, self.p1_piece)
        placePiece(self.board, 5, 4, self.p1_piece)
        placePiece(self.board, 4, 3, self.p1_piece)
        
        import random
        random.seed(42)
        # Run multiple times to increase chance of getting column 3
        results = [checkAdjacent(self.board, 1) for _ in range(5)]
        assert 3 in results, f"Expected column 3 in results, got {results}"