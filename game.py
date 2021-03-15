import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

seeds ={
    'glider_gun' :\
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    
    'beacon':\
    [[1,1,0,0],
     [1,1,0,0],
     [0,0,1,1],
     [0,0,1,1]],

    'boats':\
    [[0,0,0,1,0,0,0,0],
     [0,0,1,0,1,0,0,0],
     [0,1,0,1,1,0,0,0],
     [1,0,1,0,0,1,1,0],
     [0,1,1,0,0,1,0,1],
     [0,0,0,1,1,0,1,0],
     [0,0,0,1,0,1,0,0],
     [0,0,0,0,1,0,0,0]
    ],

    'pulsar':\
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
     [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
     [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
     [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
     [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
     [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
     [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ],

    'stairstep':\
    [[0,0,1,1],
     [0,1,1,0],
     [1,1,0,0]],

    'pentadecathlon':\
    [[0,0,1,0,0,0,0,1,0,0],
     [1,1,0,1,1,1,1,0,1,1],
     [0,0,1,0,0,0,0,1,0,0]]
}


def apply_rules(universe, x, y) -> int:
    num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    if universe[x, y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1
    else:
        return universe[x, y]
    

def simulate_life(frameNum, img, universe):
    next_universe = np.copy(universe)
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            next_universe[i, j] = apply_rules(universe, i, j)
    
    img.set_data(next_universe)
    universe[:] = next_universe[:]
    return img,

    

if __name__ == "__main__":
    N = 100
    
    universe = np.zeros((N, N))
    seed = 'glider_gun'
    universe[1:len(seeds.get(seed))+1,1:len(seeds.get(seed)[0])+1] = seeds.get(seed)
    
    fig, ax = plt.subplots()
    img = ax.imshow(universe)

    ani = animation.FuncAnimation(fig, simulate_life, fargs=(img, universe), interval=500)
    plt.show()