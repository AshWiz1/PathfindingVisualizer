import pygame
import math
import astar
import dijistra

pygame.init()


class cell:
    def __init__(self, x, y):
        self.neigh = []
        self.dist = 10000
        self.done = False
        self.x = x
        self.y = y
        self.f = 1000
        self.g = 1000
        self.h = 1000
        self.par = -1

    def calneighbours(self):
        if self.x+1 < row and grid[self.x+1][self.y] != -1:
            self.neigh.append([self.x+1, self.y])
        if self.x-1 >= 0 and grid[self.x-1][self.y] != -1:
            self.neigh.append([self.x-1, self.y])
        if self.y+1 < col and grid[self.x][self.y+1] != -1:
            self.neigh.append([self.x, self.y+1])
        if self.y-1 >= 0 and grid[self.x][self.y-1] != -1:
            self.neigh.append([self.x, self.y-1])
        if self.x+1 < row and self.y+1 < col and grid[self.x+1][self.y+1] != -1:
            self.neigh.append([self.x+1, self.y+1])
        if self.x-1 >= 0 and self.y-1 >= 0 and grid[self.x-1][self.y-1] != -1:
            self.neigh.append([self.x-1, self.y-1])
        if self.y+1 < col and self.x-1 >= 0 and grid[self.x-1][self.y+1] != -1:
            self.neigh.append([self.x-1, self.y+1])
        if self.y-1 >= 0 and self.x+1 < row and grid[self.x+1][self.y-1] != -1:
            self.neigh.append([self.x+1, self.y-1])

        self.done = False


start = -1
end = -1
f = True
size = (400, 400)
footer = 30
row = 50
col = 50
sizeblock = (size[0]//col, size[1]//row)
grid = [[0]*col for i in range(row)]
for i in range(row):
    for j in range(col):
        grid[i][j] = cell(i, j)
screen = pygame.display.set_mode((size[0], size[1]+footer))

#buttons and fonts
startbtn = pygame.draw.rect(screen, [66, 245, 236], pygame.Rect(
    0, size[1], 40, footer))  # dependency in mousebuttondown event
font = pygame.font.SysFont('Arial', 22)
screen.blit(font.render('start!', True, (255, 0, 0)), (0, size[1]))

# setup the grid look
for i in range(row):
    for j in range(col):
        pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(
            i*sizeblock[0], j*sizeblock[1], sizeblock[0]-2, sizeblock[1]-2), 2)
pygame.display.update()

# start
mousedownpos = -1
flag = 0
while f:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            f = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] >= 0 and event.pos[0] <= 40 and event.pos[1] >= size[1] and event.pos[1] < size[1]+footer:

                # calling actual dijistra function , used to call other algo
                dijistra.screen = screen
                dijistra.grid = grid
                dijistra.start = start
                dijistra.end = end
                dijistra.row = row
                dijistra.col = col
                dijistra.sizeblock = sizeblock

                returncode = dijistra.solve()
                if returncode == -1:
                    f = False
            else:
                mousedownpos = event.pos

        if event.type == pygame.MOUSEBUTTONUP and event.pos == mousedownpos:
            pos = event.pos
            left = pos[0]-pos[0] % sizeblock[0]
            j = left//sizeblock[0]

            top = pos[1]-pos[1] % sizeblock[1]
            i = top//sizeblock[1]

            pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(
                left, top, sizeblock[0], sizeblock[1]))
            pygame.display.update()
            if start == -1:
                flag += 1
                start = [i, j]
            else:
                end = [i, j]
                flag += 1
            mousedownpos = -1
        if pygame.mouse.get_pressed()[0] and flag == 2:
            try:
                pos = pygame.mouse.get_pos()
                left = pos[0]-pos[0] % sizeblock[0]
                j = left//sizeblock[0]

                top = pos[1]-pos[1] % sizeblock[1]
                i = top//sizeblock[1]
                grid[i][j] = cell(-1, -1)
                # print(i,j)
                pygame.draw.rect(screen, [255, 0, 255], pygame.Rect(
                    left, top, sizeblock[0], sizeblock[1]))
                pygame.display.update()
               # print("as")
            except:
                pass
