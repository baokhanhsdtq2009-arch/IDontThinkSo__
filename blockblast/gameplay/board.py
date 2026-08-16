import pygame


class Board:

    def __init__(self):

        self.rows = 10
        self.cols = 10

        self.board_size = 600
        self.cell_size = self.board_size // self.cols

        self.offset_x = 300
        self.offset_y = 100

        self.grid = [

            [0 for _ in range(self.cols)]

            for _ in range(self.rows)

        ]

        self.hover_cell = None


    def is_inside(self, row, col):

        return 0 <= row < self.rows and 0 <= col < self.cols


    def mouse_to_cell(self, mouse_pos):

        mx, my = mouse_pos

        col = (mx - self.offset_x) // self.cell_size
        row = (my - self.offset_y) // self.cell_size

        if self.is_inside(row, col):
            return (row, col)

        return None


    def cell_rect(self, row, col):

        return pygame.Rect(

            self.offset_x + col * self.cell_size,
            self.offset_y + row * self.cell_size,
            self.cell_size,
            self.cell_size

        )


    def draw(self, screen):

        for row in range(self.rows):

            for col in range(self.cols):

                rect = self.cell_rect(row, col)

                if self.grid[row][col] == 0:
                    fill_color = (0, 0, 0)
                else:
                    fill_color = (255, 255, 255)

                pygame.draw.rect(
                    screen,
                    fill_color,
                    rect
                )

                border_color = (180, 80, 255)

                if self.hover_cell == (row, col):
                    border_color = (0, 255, 0)

                pygame.draw.rect(
                    screen,
                    border_color,
                    rect,
                    1
                )