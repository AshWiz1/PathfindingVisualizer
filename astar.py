import pygame
import math


sizeblock = None
screen = None
start = None
end = None
grid = None
row = None
col = None
green = (3, 252, 19)
blue = (0, 40, 201)
yel = (232, 255, 25)
red = (255,0,0)
whi = (255,255,255)

def caldist(s,e):
    return math.sqrt(abs(s[0]-e[0])**2 + abs(s[1]-e[1])**2)

def solve():
    print(start)
    print(end)
    for i in range(row):
        for j in range(col):
            grid[i][j].calneighbours()

    sx,sy = start
    #caldist(start,end)
    grid[sx][sy].h = 0
    grid[sx][sy].g = 0
    grid[sx][sy].f = 0
    grid[sx][sy].par = -1
    #grid[sx][sy].h+grid[sx][sy].g

    openn = {}
    close = {}
    openn[tuple(start)] = 1
    while len(openn) > 0:
        # print(openn)
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                return -1

        #pygame.time.wait(10)
        minindex = -1
        minn = 100000
        for i in openn:
            x,y = i
            if grid[x][y].f < minn:
                minindex = i
                minn = grid[x][y].f
            
        xi,yi = minindex
        if xi == end[0] and yi == end[1]:
            break
        close[minindex] = 1
        pygame.draw.rect(screen,blue,pygame.Rect(yi*sizeblock[0],xi*sizeblock[1],sizeblock[0],sizeblock[1]))
        pygame.display.update()
        openn.pop(minindex) 
        # print("fasd")
        for i in grid[xi][yi].neigh : 
            # print(grid[xi][yi].neigh)
            x,y = i
            g = grid[xi][yi].g+1
            h = caldist([x,y],end)
            f = g+h
            # if tuple(i) in openn and tuple(i) not in close and  f < grid[x][y].f and grid[x][y].x != -1:
            #     grid[x][y].f = f
            #     grid[x][y].par = [xi,yi]
            #     pygame.draw.rect(screen,blue,pygame.Rect(y*sizeblock[0],x*sizeblock[1],sizeblock[0],sizeblock[1]))
            if tuple(i) not in close and  grid[x][y].x != -1 and (grid[x][y].f == 1000 or grid[x][y].f > f):
                
                if abs(x-xi) + abs(y-yi) == 2:
                    grid[x][y].g = g-1+1.414
                else:
                    grid[x][y].g = g
                grid[x][y].h = h

                grid[x][y].f = g + h
            
                grid[x][y].par = [xi,yi]
                pygame.draw.rect(screen,green,pygame.Rect(y*sizeblock[0],x*sizeblock[1],sizeblock[0],sizeblock[1]))
                pygame.display.update()
                openn[tuple(i)] = 1
            
            if tuple(i) in close and  grid[x][y].x != -1 and (grid[x][y].f == 1000 or grid[x][y].f > f):
                if abs(x-xi) + abs(y-yi) == 2:
                    grid[x][y].g = g-1+1.414
                else:
                    grid[x][y].g = g
                grid[x][y].h = h

                grid[x][y].f = g + h
                # if grid[x][y].par == -1:
                grid[x][y].par = [xi,yi]
                pygame.draw.rect(screen,green,pygame.Rect(y*sizeblock[0],x*sizeblock[1],sizeblock[0],sizeblock[1]))
                pygame.display.update()
                openn[tuple(i)] = 1
                close.pop(tuple(i))
    #     print("fasfd")
    tts,tte = start
    grid[tts][tte].par = -1
    ts,te = end
    print(grid[ts][te].par)
    while grid[ts][te].par != -1:
        pygame.time.wait(5)
        pygame.draw.rect(screen,whi,pygame.Rect(te*sizeblock[0],ts*sizeblock[1],sizeblock[0],sizeblock[1]))
        pygame.display.update()
        print([ts,te])
        ts,te = grid[ts][te].par

