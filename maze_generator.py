import random


class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = None
        self.start_position = None
        self.checkpoint_positions = []

    def generate_maze(self):
        maps = [
            [
                [0, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 3, 0, 1, 0, 1, 0, 1],
                [1, 1, 0, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 0, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 0]
            ],
            [
                [0, 0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 3, 1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 1, 1, 0, 1],
                [1, 0, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 0]
            ]
          ]

        self.maze = random.choice(maps)
        self.start_position = (1, 1)  # Set the start position
        self.checkpoint_positions = [(3, 3), (6, 6)]  # Set checkpoint positions

    def get_maze(self):
        return self.maze

    def get_start_position(self):
        return self.start_position

    def get_checkpoint_positions(self):
        return self.checkpoint_positions


def print_maze(player_pos, maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == player_pos:
                print("@", end=" ")
            elif maze[row][col] == 1:
                print(chr(9608), end=" ")  # Symbol for wall
            elif maze[row][col] == 3:
                print("X", end=" ")  # Symbol for checkpoint 3
            elif (row, col) == (len(maze) - 1, len(maze[0]) - 1):
                print("✩", end=" ")  # Symbol for endpoint
            else:
                print(".", end=" ")  # Symbol for passable space
        print()

def move_player(player_pos, move_key, maze):
    row, col = player_pos
    new_row, new_col = row, col

    if move_key == "w" and row > 0 and maze[row - 1][col] != 1 and maze[row - 1][col] != 3:
        new_row = row - 1
    elif move_key == "s" and row < len(maze) - 1 and maze[row + 1][col] != 1 and maze[row + 1][col] != 3:
        new_row = row + 1
    elif move_key == "a" and col > 0 and maze[row][col - 1] != 1 and maze[row][col - 1] != 3:
        new_col = col - 1
    elif move_key == "d" and col < len(maze[0]) - 1 and maze[row][col + 1] != 1 and maze[row][col + 1] != 3:
        new_col = col + 1

    return new_row, new_col


def main():
    maze_size = 9

    while True:
        maze_generator = MazeGenerator(maze_size, maze_size)
        maze_generator.generate_maze()
        current_position = maze_generator.get_start_position()
        checkpoint_positions = maze_generator.get_checkpoint_positions()

        while True:
            print_maze(current_position, maze_generator.get_maze())

            move = input("Enter move (W/A/S/D): ").lower()
            if move in {'w', 'a', 's', 'd'}:
                current_position = move_player(current_position, move, maze_size)

                # Check if the player reached a checkpoint
                if current_position in checkpoint_positions:
                    print("Checkpoint reached!")
            else:
                print("Invalid move! Use W/A/S/D.")
                continue

            if current_position == (maze_size - 1, maze_size - 1):
                print("Congratulations! You reached the exit!")
                break


if __name__ == "__main__":
    main()