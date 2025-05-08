import pygame
from pygame.surface import Surface
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.init()

# Global variables
s_with = 800
s_height = 700
play_width = 300  # meaning 300/10 = 30 width per block
play_height = 600  # meaning 600/20 = 20 height per block
block_size = 30  # size of block

top_left_x = (s_with - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS
S = [
    [".....", ".....", "..00.", ".00..", "....."],
    [".....", "..0..", "..00.", "...0.", "....."],
]
Z = [
    [".....", ".....", ".00..", "..00.", "....."],
    [".....", "..0..", ".00..", ".0...", "....."],
]
I = [
    [
        "..0..",
        "..0..",
        "..0..",
        "..0..",
        ".....",
    ],
    [
        ".....",
        "0000.",
        ".....",
        ".....",
        ".....",
    ],
]
O = [
    [
        ".....",
        ".....",
        ".00..",
        ".00..",
        ".....",
    ]
]
J = [
    [
        ".....",
        ".0...",
        ".000.",
        ".....",
        ".....",
    ],
    [
        ".....",
        "..00.",
        "..0..",
        "..0..",
        ".....",
    ],
    [
        ".....",
        ".....",
        ".000.",
        "...0.",
        ".....",
    ],
    [".....", "...0.", "...0.", "..00.", "....."],
]
L = [
    [
        ".....",
        "...0.",
        ".000.",
        ".....",
        ".....",
    ],
    [
        ".....",
        "..0..",
        "..0..",
        "..00.",
        ".....",
    ],
    [
        ".....",
        ".....",
        ".000.",
        ".0...",
        ".....",
    ],
    [".....", ".00..", "..0..", "..0..", "....."],
]
T = [
    [
        ".....",
        "..0..",
        ".000.",
        ".....",
        ".....",
    ],
    [
        ".....",
        "..0..",
        "..00.",
        "..0..",
        ".....",
    ],
    [
        ".....",
        ".....",
        ".000.",
        "..0..",
        ".....",
    ],
    [
        ".....",
        "..0..",
        ".00..",
        "..0..",
        ".....",
    ],
]

shapes = [S, Z, I, O, J, L, T]
shapes_colors = [
    (0, 255, 0),  # S
    (255, 0, 0),  # Z
    (0, 255, 255),  # I
    (255, 255, 0),  # O
    (0, 0, 255),  # J
    (255, 165, 0),  # L
    (128, 0, 128),  # T
]


class Piece(object):
    """
    Class to represent a piece in Tetris.
    """

    def __init__(self, x, y, shape):
        """
        Initialize the piece with its position and shape.
        :param x: x-coordinate of the piece
        :param y: y-coordinate of the piece
        :param shape: shape of the piece
        """
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shapes_colors[shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_positions):
    """
    Create a grid for the game.
    :param locked_positions: positions of locked pieces
    :return: grid
    """
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[j, i]
                grid[i][j] = c
    return grid


def convert_shape_format(shape: Piece):
    """
    Convert the shape format to a list of positions.
    :param shape: shape of the piece
    :return: list of positions
    """
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape: Piece, grid):
    """
    Check if the shape is in a valid space.
    :param shape: shape of the piece
    :param grid: grid of the game
    :return: True if valid space, False otherwise
    """
    accepted_positions = [
        [(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)
    ]
    accepted_positions = [j for sub in accepted_positions for j in sub]

    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] >= 0:
                return False
    return True


def check_lost(positions):
    """
    Check if the player has lost.
    :param positions: positions of locked pieces
    :return: True if lost, False otherwise
    """
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    """
    Get a random shape from the list of shapes.
    :return: random shape
    """
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle():
    """
    Draw the text in the middle of the screen.
    :return: None
    """
    pass


def draw_grid(surface: Surface, grid):
    """
    Draw the grid on the surface.
    :param surface: surface to draw on
    :param grid: grid of the game
    :return: None
    """
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(
            surface,
            (128, 128, 128),
            (sx, sy + i * block_size),
            (sx + play_width, sy + i * block_size),
        )
        for j in range(len(grid[i])):
            pygame.draw.line(
                surface,
                (128, 128, 128),
                (sx + j * block_size, sy),
                (sx + j * block_size, sy + play_height),
            )


def clear_rows(grid, locked_positions):
    """
    Clear the rows that are full and move the pieces down.
    :param grid: grid of the game
    :param locked_positions: positions of locked pieces
    :return: None
    """
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked_positions[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked_positions), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                new_key = (x, y + inc)
                locked_positions[new_key] = locked_positions.pop(key)


def draw_next_shape(surface: Surface, shape: Piece):
    """
    Draw the next shape on the surface.
    :param surface: surface to draw on
    :param shape: shape of the piece
    :return: None
    """
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255, 255, 255))
    surface.blit(
        label, (top_left_x + play_width + 50, top_left_y + play_height // 2 - 100)
    )
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height // 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, columns in enumerate(row):
            if columns == "0":
                pygame.draw.rect(
                    surface,
                    shape.color,
                    (sx + j * block_size, sy + i * block_size, block_size, block_size),
                    0,
                )


def draw_window(surface: Surface, grid):
    """
    Draw the window with the grid and the title.
    :param surface: surface to draw on
    :param grid: grid of the game
    :return: None
    """
    surface.fill((0, 0, 0))
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                surface,
                grid[i][j],
                (
                    top_left_x + j * block_size,
                    top_left_y + i * block_size,
                    block_size,
                    block_size,
                ),
                0,
            )

    pygame.draw.rect(
        surface,
        (255, 0, 0),
        (
            top_left_x,
            top_left_y,
            play_width,
            play_height,
        ),
        4,
    )
    draw_grid(surface, grid)


def main(surface: Surface):
    """
    Main function to run the game.
    :param surface: surface to draw on
    :return: None
    """
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_format = convert_shape_format(current_piece)
        for i in range(len(shape_format)):
            x, y = shape_format[i]
            if y >= 0:
                grid[y][x] = current_piece.color
        if change_piece:
            for pos in shape_format:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)

        draw_window(surface, grid)
        draw_next_shape(surface, next_piece)
        pygame.display.update()
        if check_lost(locked_positions):
            run = False
    pygame.display.quit()


def main_menu():
    """
    Main menu for the game.
    :return: None
    """
    window = pygame.display.set_mode((s_with, s_height))
    pygame.display.set_caption("Tetris")
    main(window)


if __name__ == "__main__":
    main_menu()
