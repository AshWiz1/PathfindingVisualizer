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

def solve():
    global grid
    ans = []
    
    for i in range(row):
        for j in range(col):
            grid[i][j].calneighbours()
            # print(i,j)
            # print(grid[i][j].x,grid[i][j].y)
            # print(grid[i][j].neigh)
           
    tx,ty = end
    grid[tx][ty].dist = 0
    print(end)
    ans.append(end)
    #print(end)
    path  = {}
    flag = 0
    while len(ans) > 0:
        
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                return -1

       # pygame.time.wait(1)
        index = -1
        min = 10000
        for i in range(0,len(ans)):
           
            x, y =ans[i]
            if min > grid[x][y].dist:
                min = grid[x][y].dist
                index = i
        
        # print(ans[index])
       
        xi,yi = ans[index]
        if (xi == start[0] and yi == start[1]):
            break
        pygame.draw.rect(screen,green,pygame.Rect(yi*sizeblock[0],xi*sizeblock[1],sizeblock[0],sizeblock[1]))
        pygame.display.update()
        ans.pop(index)
        grid[xi][yi].done = True
        
        for i in grid[xi][yi].neigh:
            # print("neigh")
            # print(i)
            # print("end")
            x = i[0]
            y = i[1]

            if grid[x][y].done != True and grid[x][y].dist > grid[xi][yi].dist + 1 and grid[x][y].x != -1:
                grid[x][y].dist =  grid[xi][yi].dist +1
                path[(x,y)] = (xi,yi)
                pygame.draw.rect(screen,blue,pygame.Rect(y*sizeblock[0],x*sizeblock[1],sizeblock[0],sizeblock[1]))
                if (x == start[0] and y == start[1]):
                    flag = 1
                    break
                ans.append([x,y])
        if (flag == 1):
            break
    
    next = tuple(start)
    while next in path:
        x,y = next
        pygame.time.wait(5)
        pygame.draw.rect(screen,yel,pygame.Rect(y*sizeblock[0],x*sizeblock[1],sizeblock[0],sizeblock[1]))
        pygame.display.update()
        print(next)
        next = path[next]