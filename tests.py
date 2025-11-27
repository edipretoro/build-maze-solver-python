import unittest

from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_different_dimensions(self):
        """Test avec différentes dimensions"""
        num_cols = 5
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)
        
        # Vérifier que toutes les colonnes ont le bon nombre de lignes
        for col in m1._Maze__cells:
            self.assertEqual(len(col), num_rows)

    def test_maze_create_cells_single_cell(self):
        """Test avec un seul cell (1x1)"""
        m1 = Maze(0, 0, 1, 1, 20, 20)
        self.assertEqual(len(m1._Maze__cells), 1)
        self.assertEqual(len(m1._Maze__cells[0]), 1)

    def test_maze_create_cells_large_maze(self):
        """Test avec un grand maze"""
        num_cols = 50
        num_rows = 50
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_cells_are_cell_objects(self):
        """Vérifier que les cells sont des instances de Cell"""
        m1 = Maze(0, 0, 3, 3, 10, 10)
        for i in range(3):
            for j in range(3):
                self.assertIsInstance(m1._Maze__cells[i][j], Cell)

    def test_maze_initialization_parameters(self):
        """Vérifier que les paramètres d'initialisation sont correctement stockés"""
        x1, y1 = 10, 20
        num_rows, num_cols = 5, 7
        cell_size_x, cell_size_y = 30, 40
        
        m1 = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y)
        
        self.assertEqual(m1._Maze__x1, x1)
        self.assertEqual(m1._Maze__y1, y1)
        self.assertEqual(m1._Maze__num_rows, num_rows)
        self.assertEqual(m1._Maze__num_cols, num_cols)
        self.assertEqual(m1._Maze__cell_size_x, cell_size_x)
        self.assertEqual(m1._Maze__cell_size_y, cell_size_y)

    def test_maze_without_window(self):
        """Test sans window (win=None par défaut)"""
        m1 = Maze(0, 0, 3, 3, 10, 10)
        self.assertIsNone(m1._Maze__win)
        # Le maze devrait quand même être créé
        self.assertEqual(len(m1._Maze__cells), 3)

    def test_maze_rectangular_not_square(self):
        """Test avec un maze rectangulaire (non carré)"""
        m1 = Maze(0, 0, 10, 5, 15, 20)
        self.assertEqual(len(m1._Maze__cells), 5)  # 5 colonnes
        self.assertEqual(len(m1._Maze__cells[0]), 10)  # 10 lignes

    def test_entrance_top_wall_removed(self):
        """Vérifier que le mur du haut de la cellule d'entrée est supprimé"""
        m1 = Maze(0, 0, 5, 5, 10, 10)
        # La cellule en haut à gauche [0][0] ne devrait plus avoir de mur en haut
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
    
    def test_exit_bottom_wall_removed(self):
        """Vérifier que le mur du bas de la cellule de sortie est supprimé"""
        m1 = Maze(0, 0, 5, 5, 10, 10)
        
        # La cellule en bas à droite [-1][-1] ne devrait plus avoir de mur en bas
        self.assertFalse(m1._Maze__cells[-1][-1].has_bottom_wall)

    def test_entrance_and_exit_different_maze_sizes(self):
        """Test avec différentes tailles de maze"""
        # Petit maze 2x2
        m1 = Maze(0, 0, 2, 2, 10, 10)
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[1][1].has_bottom_wall)
        
        # Grand maze 10x10
        m2 = Maze(0, 0, 10, 10, 10, 10)
        self.assertFalse(m2._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m2._Maze__cells[9][9].has_bottom_wall)
    
    def test_entrance_and_exit_rectangular_maze(self):
        """Test avec un maze rectangulaire (non carré)"""
        # 3 colonnes, 5 lignes
        m1 = Maze(0, 0, 5, 3, 10, 10)
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[2][4].has_bottom_wall)
        
        # 7 colonnes, 3 lignes
        m2 = Maze(0, 0, 3, 7, 10, 10)
        self.assertFalse(m2._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m2._Maze__cells[6][2].has_bottom_wall)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

if __name__ == "__main__":
    unittest.main()
