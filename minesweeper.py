"""Create a function that takes a grid of # and -, where each
hash (#) represents a mine and each dash (-) represents a mine-free spot.

Return a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. horizontally, vertically, and
diagonally

Ensure that when checking adjacent positions in the grid that you take into
account that on the edges of the grid, you may go out of bounds

There may be quite a lot of repetition in this task to do things like check
whether a particular row and column combination (i.e. cell) is a valid position
in the grid (within bounds), and to increment the counts of the number of
adjacent # signs.

It makes sense to create functions to handle the repetitive aspects
"""
import random
# random used in grid generation


# grid generator creates a random square grid with various options
# seed can be used to fix a grid, needs to be in single list of values format
def grid_generator(side_size, mine="#", blank="-", output='g', seed=[]):
    grid_size = (side_size ** 2)
    mine_count = round((grid_size / 6))
    if seed == []:
        symbol_list = random.choices(
                    [mine, blank], cum_weights=[mine_count+1, grid_size],
                    k=grid_size)
    else:
        symbol_list = seed
    if output != 'g':
        return symbol_list
    else:
        new_grid = ([])
        temp_list = []
        for n in range(grid_size):
            index = n+1
            temp_list.append(symbol_list[n])
            if index % side_size == 0:
                new_grid.append(temp_list)
                temp_list = []
        return new_grid


# the function converts from nested list to single string list
# and vice versa
def grid_list_swap(grid_or_list, side_length, start_type='g'):
    if start_type != 'g':
        new_grid = ([])
        temp_list = []
        for n in range(len(grid_or_list)):
            index = n+1
            temp_list.append(grid_or_list[n])
            if index % side_length == 0:
                new_grid.append(temp_list)
                temp_list = []
        return new_grid
    else:
        temp_list = []
        for x in range(side_length):
            for item in grid_or_list[x]:
                temp_list.append(item)
        return temp_list


# function to list co-ordinates of mines
def mine_finder(grid, side_size, mine="#"):
    mine_list = []
    for x in range(side_size):
        for y in range(side_size):
            if grid[x][y] == mine:
                mine_list.append([x, y])
    return mine_list


# takes a list of mine locations and lists every adjacent location
# multiples of all locations
def adjacency_list(mine_list, side_size):
    adj_list = []
    for mine in mine_list:
        x = mine[0]
        y = mine[1]
        adj_list.append([x, y+1])
        adj_list.append([x, y-1])
        for y in range(y-1, y+2):
            adj_list.append([x+1, y])
            adj_list.append([x-1, y])
    final_list = []
    for adj in adj_list:
        if adj not in mine_list:
            if 0 <= adj[0] < side_size:
                if 0 <= adj[1] < side_size:
                    final_list.append(adj)
    return final_list


# takes a list of all adjacency cases (as above)
# produces a grid in the requested style
def add_num_to_grid(grid, adjacency_list, side_size, mine="#", blank="-"):
    for x in range(side_size):
        for y in range(side_size):
            if grid[x][y] == blank:
                grid[x][y] = 0
    for coordinate in adjacency_list:
        x = coordinate[0]
        y = coordinate[1]
        grid[x][y] += 1
    for x in range(side_size):
        for y in range(side_size):
            if grid[x][y] == 0:
                grid[x][y] = blank
            else:
                grid[x][y] = str(grid[x][y])
        print(f"{grid[x]}")
    return grid


# print grid a tool to ensure a nice layout of a 2d information list/
# array analogue
def print_grid(grid):
    for row in grid:
        print(f"{row}")
    print("\n")


side_size = 15
new_grid = grid_generator(side_size, mine="#", blank="-")
print_grid(new_grid)

mine_map = mine_finder(new_grid, side_size)

all_adjacents = adjacency_list(mine_map, side_size)

add_num_to_grid(new_grid, all_adjacents, side_size)
