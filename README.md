## Overview 🪶
This project is a simple Tic-Tac-Toe game implemented in Python using the Tkinter library for the graphical user interface (GUI). The game allows two players to play against each other on a 3x3 grid, with Player 1 using "X" and Player 2 using "O".

The application features:

A clean and user-friendly GUI.
Input fields for player names.
A dynamically updated turn display.
Winner or tie announcements.
A reset button to restart the game.

## Features 🌟
Start Screen

Players enter their names for Player 1 (X) and Player 2 (O) in input fields.
A "Start Game" button initiates the game after validating the input.
Game Board

A 3x3 grid where players can click on cells to place their marker (X or O).
Each marker is displayed in vibrant colors:
Red (#e63946) for X.
Blue (#457b9d) for O.
Turn Indicator

Displays whose turn it is with a color-coded label.
Win or Tie Detection

Alerts players when:
A winner is found.
The game ends in a tie.
Reset Functionality

Players can restart the game at any time using the "Reset Game" button.

## screenshot
![output](https://github.com/user-attachments/assets/34eb95ac-481a-4ef8-98ca-4b62afbbc88a)


## How it works💻

Structure
The code is structured into multiple functions to handle different aspects of the game:

Game State Management

The board is a 3x3 list initialized with empty strings (""), representing the Tic-Tac-Toe grid.
The current_player variable tracks whether it's Player 1's turn (X) or Player 2's turn (O).
Grid and Input

A Tkinter Canvas widget is used to display the game board and handle player moves.
Each click on the canvas corresponds to a cell in the grid, calculated based on the click coordinates.
Game Logic

The check_winner() function checks for winning conditions by evaluating rows, columns, and diagonals.
If all cells are filled without a winner, the game declares a tie.
Reset Functionality

The reset_game() function clears the board, redraws the grid, and resets the turn display.
Player Turns

Players alternate turns. The turn indicator at the top of the screen dynamically updates to show which player's turn it is.
Start Screen

Before starting, players must input their names. These names are displayed throughout the game to personalize the experience.
