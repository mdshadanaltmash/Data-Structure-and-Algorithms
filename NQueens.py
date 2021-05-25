class Queens:
 def __init__(self, size):
     self.solutions = 0
     self.size = size
     self.solve()

 def Print_board(self, positions):
     for row in range(self.size):
         line = ""
         for column in range(self.size):
             if positions[row] == column:
                 line += "Q "
             else:
                 line += "- "
         print(line)
     print("\n")

 def solve(self):
     positions = [-1] * self.size
     self.place_queen(positions, 0)
     print(self.solutions, "solutions Found.")

 def place_queen(self, positions, target_row):
     if target_row == self.size:
         self.Print_board(positions)
         self.solutions += 1
     else:
         for column in range(self.size):
           if self.check_position(positions, target_row, column):
                 positions[target_row] = column
                 self.place_queen(positions, target_row + 1)

 def check_position(self, positions, ocuppied_rows, column):
     for i in range(ocuppied_rows):
         if positions[i] == column or \
             positions[i] - i == column - ocuppied_rows or \
             positions[i] + i == column + ocuppied_rows:

             return False
     return True

Queens(int(input("Enter the size of board or no of Queens")))
