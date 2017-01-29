# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver by Adrian Debbeler

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins problems is solved with the strategy described [http://www.sudokudragon.com/tutorialnakedtwins.htm](here). It's adding additional constraints by looking for two boxes having the same two numbers (and no other!) as solutions in the same unit. If these can be found, we can remove these two numbers from all other peers in this unit.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonal sudoku constraint is strengthening other strategies as the list of units now also includes the two diagonals of the sudoko. When applying strategies which make use of the unit lists, this can lead to additional reductions of the search space.

