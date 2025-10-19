# Tic-Tac-Toe with Smarter AI

This project provides a command-line Tic-Tac-Toe implementation that supports both a legacy random-move bot and a new optimal AI powered by minimax search with depth-aware scoring.

## Features
- Interactive console UI with input validation.
- Player can choose to play as `X` or `O`.
- Two AI skill levels:
  - Random: retains the original stochastic play style.
  - Optimal: applies minimax with alpha-beta style pruning heuristics and depth weighting for perfect play.

## Advanced AI Approach
The smart AI uses established game-tree search techniques to guarantee an optimal outcome:
- **State evaluation** relies on the classic win/draw checks used by both the player and AI.
- **Minimax recursion** explores the full decision tree, alternating between maximizing (AI's turn) and minimizing (human's turn) layers to anticipate the best guaranteed result.
- **Depth-aware scoring** encourages faster wins (`10 - depth`) and slower losses (`depth - 10`), ensuring the AI prefers immediate victory and delays defeat where unavoidable.
- **Heuristic shortcut** claims the center square when available before running minimax, reducing tree expansion for the most common high-value move without sacrificing correctness.
- **Move generation** uses compact helper routines to enumerate legal moves and roll the board state forward and back during search, keeping the core algorithm readable and testable.

These techniques transform the AI from reactive randomness into a deterministic strategy engine that never loses when perfect play is possible.

## How to Play
1. Run the game:
   ```bash
   python tictactoe.py
   ```
2. Choose whether you want to be Player 1 (`X`) or Player 2 (`O`).
3. Select the AI difficulty:
   - `1` for the legacy random opponent.
   - `2` for the optimal minimax-powered opponent.
4. Enter moves as two numbers separated by a space (row and column, both 0-2).

Enjoy exploring the contrast between casual and optimal Tic-Tac-Toe play!*** End Patch
