# Main

[Tetris Index](../README.md#tetris-index) / [Src](./index.md#src) / Main

> Auto-generated documentation for [src.main](https://github.com/Celudor/tetris/blob/main/src/main.py) module.

#### Attributes

- `s_with` - Global variables: 800

- `S` - SHAPE FORMATS: [['.....', '.....', '..00.', '.00..', '.....'], ['.....', '..0..', '..00.', '...0.', '.....']]


- [Main](#main)
  - [Piece](#piece)
  - [check_lost](#check_lost)
  - [clear_rows](#clear_rows)
  - [convert_shape_format](#convert_shape_format)
  - [create_grid](#create_grid)
  - [draw_grid](#draw_grid)
  - [draw_next_shape](#draw_next_shape)
  - [draw_text_middle](#draw_text_middle)
  - [draw_window](#draw_window)
  - [get_shape](#get_shape)
  - [main](#main)
  - [main_menu](#main_menu)
  - [valid_space](#valid_space)

## Piece

[Show source in main.py:148](https://github.com/Celudor/tetris/blob/main/src/main.py#L148)

Class to represent a piece in Tetris.

#### Signature

```python
class Piece(object):
    def __init__(self, x, y, shape): ...
```



## check_lost

[Show source in main.py:224](https://github.com/Celudor/tetris/blob/main/src/main.py#L224)

Check if the player has lost.

#### Arguments

- `positions` - positions of locked pieces

#### Returns

True if lost, False otherwise

#### Signature

```python
def check_lost(positions): ...
```



## clear_rows

[Show source in main.py:279](https://github.com/Celudor/tetris/blob/main/src/main.py#L279)

Clear the rows that are full and move the pieces down.

#### Arguments

- `grid` - grid of the game
- `locked_positions` - positions of locked pieces

#### Returns

None

#### Signature

```python
def clear_rows(grid, locked_positions): ...
```



## convert_shape_format

[Show source in main.py:183](https://github.com/Celudor/tetris/blob/main/src/main.py#L183)

Convert the shape format to a list of positions.

#### Arguments

- `shape` - shape of the piece

#### Returns

list of positions

#### Signature

```python
def convert_shape_format(shape: Piece): ...
```

#### See also

- [Piece](#piece)



## create_grid

[Show source in main.py:167](https://github.com/Celudor/tetris/blob/main/src/main.py#L167)

Create a grid for the game.

#### Arguments

- `locked_positions` - positions of locked pieces

#### Returns

grid

#### Signature

```python
def create_grid(locked_positions): ...
```



## draw_grid

[Show source in main.py:253](https://github.com/Celudor/tetris/blob/main/src/main.py#L253)

Draw the grid on the surface.

#### Arguments

- `surface` - surface to draw on
- `grid` - grid of the game

#### Returns

None

#### Signature

```python
def draw_grid(surface: Surface, grid): ...
```



## draw_next_shape

[Show source in main.py:305](https://github.com/Celudor/tetris/blob/main/src/main.py#L305)

Draw the next shape on the surface.

#### Arguments

- `surface` - surface to draw on
- `shape` - shape of the piece

#### Returns

None

#### Signature

```python
def draw_next_shape(surface: Surface, shape: Piece): ...
```

#### See also

- [Piece](#piece)



## draw_text_middle

[Show source in main.py:245](https://github.com/Celudor/tetris/blob/main/src/main.py#L245)

Draw the text in the middle of the screen.

#### Returns

None

#### Signature

```python
def draw_text_middle(): ...
```



## draw_window

[Show source in main.py:333](https://github.com/Celudor/tetris/blob/main/src/main.py#L333)

Draw the window with the grid and the title.

#### Arguments

- `surface` - surface to draw on
- `grid` - grid of the game

#### Returns

None

#### Signature

```python
def draw_window(surface: Surface, grid): ...
```



## get_shape

[Show source in main.py:237](https://github.com/Celudor/tetris/blob/main/src/main.py#L237)

Get a random shape from the list of shapes.

#### Returns

random shape

#### Signature

```python
def get_shape(): ...
```



## main

[Show source in main.py:373](https://github.com/Celudor/tetris/blob/main/src/main.py#L373)

Main function to run the game.

#### Arguments

- `surface` - surface to draw on

#### Returns

None

#### Signature

```python
def main(surface: Surface): ...
```



## main_menu

[Show source in main.py:445](https://github.com/Celudor/tetris/blob/main/src/main.py#L445)

Main menu for the game.

#### Returns

None

#### Signature

```python
def main_menu(): ...
```



## valid_space

[Show source in main.py:204](https://github.com/Celudor/tetris/blob/main/src/main.py#L204)

Check if the shape is in a valid space.

#### Arguments

- `shape` - shape of the piece
- `grid` - grid of the game

#### Returns

True if valid space, False otherwise

#### Signature

```python
def valid_space(shape: Piece, grid): ...
```

#### See also

- [Piece](#piece)