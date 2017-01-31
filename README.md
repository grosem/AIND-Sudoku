# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver by Adrian Debbeler

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propagation is a process of inference. It satisfies constraints by removing values from the domain. Every box of a sudoku can hold one of nine digits which have to adhere to the sudoku rules. Once digits get removed, there might be other constraints leading to even more removals and so on. *Naked Twins* is a strategy to remove digits from the possible solutions. Its from the sudoku rules derived constraints work like this:

1. Each box has a unique set of 20 peers with the constraint that the box's digit is unique among its peers.
2. If the box has two possible solutions (this also works for n>2 solutions) and has n-1 peers with the same solutions, it is certain that these numbers are distributed between these boxes.
3. Knowing that, these digits are not available for all other peers of the same unit and can get removed safely.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonal sudoku constraint says that both diagonals of a sudoku contain all digits between 1 and 9. We can deduct that a digit is unique in the diagonal and using a strategy such as *Naked Twins* this information can used to remove possible solutions. Boxes in the diagonal would be a special case and have 26 peers instead of 20.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
