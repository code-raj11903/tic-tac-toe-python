# Tic-Tac-Toe Game in Python

This repository contains a simple implementation of the classic Tic-Tac-Toe game using Python. The game allows two players to take turns and compete against each other on a 3x3 grid. The repository provides three main functions to facilitate the game:

1. `disp()`: Display the current state of the Tic-Tac-Toe board.
2. `u_input()`: Take input from players to make their moves.
3. `game_status()`: Check the current status of the game, determine if any player has won, and terminate the game if a winner is found. It also calls the `disp()` function to visualize the board.

## How to Play

1. Clone the repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-python.git
   ```

2. Navigate to the repository directory.
   
   ```bash
   cd tic-tac-toe-python
   ```

3. Run the `tic_tac_toe.py` script using Python.

   ```bash
   python tic_tac_toe.py
   ```

4. Follow the on-screen instructions to take turns making moves. Enter the row and column indices to place your X or O on the board.

5. The game will automatically determine if there's a winner or if the game has ended in a draw.

## Functions

### `disp()`

This function displays the current state of the Tic-Tac-Toe board, showing the positions of Xs and Os. It provides a visual representation of the ongoing game.

### `u_input()`

The `u_input()` function takes input from the players to make their moves. Players need to enter the row and column indices (0 to 2) to indicate where they want to place their X or O on the board.

### `game_status()`

The `game_status()` function checks the current state of the game to determine if there's a winner or if the game has ended in a draw. If a player has won, the function terminates the game and calls the `disp()` function to display the final board state.

## Contributing

Contributions are welcome! If you find any issues, have suggestions for improvements, or want to add new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy the game of Tic-Tac-Toe implemented in Python! Have fun playing against your friends and improving your strategic skills. If you encounter any problems or have ideas for enhancements, don't hesitate to share them. Happy coding!
