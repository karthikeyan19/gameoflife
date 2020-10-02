import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
on = 255
off = 0
vals =[on,off]
N=100
count=0
def randomGrid(N):
    return np.random.choice(vals,N*N,p=[0.2,0.8]).reshape(N,N)
def glider(i,j,N,g):    
    #g = np.zeros(N*N).reshape(N,N)
    glider=np.array([[0,0,255],
                     [255,0,255],
                     [0,255,255]])
    g[i:i+3,j:j+3] = glider
    return g
def gliderl(i,j,N,g):    
    #g = np.zeros(N*N).reshape(N,N)
    glider=np.array([[255,0,0],
                     [0,255,255],
                     [255,255,0]])
    g[i:i+3,j:j+3] = glider
    return g

def gliderl(i,j,N,g):    
    #g = np.zeros(N*N).reshape(N,N)
    glider=np.array([[255,0,0],
                     [0,255,255],
                     [255,255,0]])
    g[i:i+3,j:j+3] = glider
    return g
def gosper_glider_gun(i,j,N,grid):
    gun = np.zeros(11*38).reshape(11,38)
    gun[5,1]=gun[5,2]=255
    gun[6,1]=gun[6,2]=255

    gun[3,13] =gun[3,14]=255
    gun[4,12]=gun[4,16]=255
    gun[5,11]=gun[5,17]=255
    gun[6,11]=gun[6,15]=gun[6,17]=gun[6,18]=255
    gun[7,11]=gun[7,17]=255
    gun[8,12]=gun[8,16]=255
    gun[9,13]=gun[9,14]=255


    gun[1,25]=255
    gun[2,23]=gun[2,25]=255
    gun[3,21]=gun[3,22]=255
    gun[4,21]=gun[4,22]=255
    gun[5,21]=gun[5,22]=255
    gun[6,23]=gun[6,25]=255
    gun[7,25]=255

    gun[3][35]=gun[3][36]=255
    gun[4][35]=gun[4][36]=255
    print("gun")
    print(gun)
    grid[i:i+11,j:j+38] = gun
    return grid    
def low_spaceship(i,j,N,g):
    if(N > 5):
        ss=np.array([[255,0,0,255,0],
                     [0,0,0,0,255],
                     [255,0,0,0,255]
                     ,[0,255,255,255,255]])
    g[i:i+4,j:j+5] = ss
    return g
        
def mid_spaceship(i,j,N,g):
    if(N > 6):
        ss=np.array([[0,255,255,255,255,255],
                     [255,0,0,0,0,255],
                     [0,0,0,0,0,255]
                     ,[255,0,0,0,255,0],
                     [0,0,255,0,0,0]])
    g[i:i+5,j:j+6] = ss
    return g

def large_spaceship(i,j,N,g):
    if(N > 7):
        ss=np.array([[0,255,255,255,255,255,255],
                     [255,0,0,0,0,0,255],
                     [0,0,0,0,0,0,255]
                     ,[255,0,0,0,0,255,0],
                     [0,0,255,255,0,0,0]])
    g[i:i+5,j:j+7] = ss
    return g

def cross(i,j,N,g):    
    #g = np.zeros(N*N).reshape(N,N)
    glider=np.array([[0,0,0],
                     [255,255,255],
                     [0,0,0]])
    g[i:i+3,j:j+3] = glider
    return g


def update(frameNum,img,grid,N):
    newGrid = grid.copy()
    
    for i in range(N):
        for j in range(N):


            total = int((grid[i,(j-1)%N] + grid[i,(j+1)%N]+
                    grid[(i-1)%N,j] + grid[(i+1)%N,j]+
                    grid[(i-1)%N,(j-1)%N]+grid[(i+1)%N,(j+1)%N]+
                         grid[(i+1)%N,(j-1)%N]+grid[(i-1)%N,(j+1)%N])/255)

            if grid[i,j] == on:
                if (total < 2) or (total > 3):
                    newGrid[i,j]=off
            else:
                if  total==3:
                    newGrid[i,j]=on
            #print(total)        
    img.set_data(newGrid)
    #print(newGrid)
    grid[:]=newGrid[:]

    return img,

grid=randomGrid(N)
#print(grid[0][-1])
#grid = glider(16,16,N,np.zeros(N*N).reshape(N,N))
grid=low_spaceship(25,25,N,np.zeros(N*N).reshape(N,N))
grid=mid_spaceship(25,13,N,grid)
grid = large_spaceship(25,1,N,grid)

#grid = cross(25,1,N,grid)

#grid = glider(1,1,N,grid)

grid=gosper_glider_gun(1,1,N,np.zeros(N*N).reshape(N,N))

print(grid)
fig,ax = plt.subplots()
ax.set_title('game of Life')
img=ax.imshow(grid,interpolation='nearest')
a = ani.FuncAnimation(fig,update,fargs=(img,grid,N,),
                      frames=10,
                      interval=500,
                      save_count=50)

plt.show()    
