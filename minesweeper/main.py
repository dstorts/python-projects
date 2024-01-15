import tkinter
from functools import partial
from tile import Tile
import random

GRID_WIDTH = 10
GRID_HEIGHT = 10
TILE_DIM = 40
SIDE_CONTROLS_WIDTH = 80
NUM_BOMBS = 20
placements = {
    'flag_btn_x':0,
    'flag_btn_y':0,
    'tiles_origin_x':80,
    'tiles_origin_y':0,
    'game_on_lbl_x':0,
    'game_on_lbl_y':81,
}
is_flag_mode = False
game_over = False
tiles = []

def check_win():
    global game_over
    all_bombs_flagged = True
    all_nonbombs_revealed = True
    for tile in tiles:
        if tile.bomb and not tile.flagged:
            #here if tile has a bomb and is NOT flagged (necessary to win)
            all_bombs_flagged = False
        if not tile.bomb and not tile.revealed:
            #here if current tile is not a bomb and NOT revealed
            all_nonbombs_revealed = False
    if all_bombs_flagged and all_nonbombs_revealed and game_over == False:
        return True
    return False

def tile_select(tile):
    global game_over #let python know we want to use the global variable game_over
    if is_flag_mode and not game_over:
        #toggle a flag on the tile
        if tile.flagged:
            tile.flagged = False
            #here if tlie is flagged... unflag it
            if tile.bomb:
                tile.config(text=tile.bomb_text)
            else:
                tile.config(text=tile.neighbor_bomb_count)
        else:
            tile.flagged = True
            tile.config(text=tile.flag_text)
    elif not game_over and tile.flagged == False:
        #reveal tile
        i = tiles.index(tile)
        print(i)
        if tiles[i].bomb:
            #game over
            game_over = True
            game_on_lbl.config(text="You LOSE")
            tiles[i].config(bg="red")
        elif not tile.revealed:
            #reveal the bombcount of neighbors of this tile
            tiles_to_reveal = []
            tiles_to_reveal.append(tiles.index(tile))
            print(len(tiles_to_reveal))
            while len(tiles_to_reveal) > 0:
                tiles[tiles_to_reveal[0]].config(bg="yellow")

                i = tiles_to_reveal[0] #get index of tile in the grid from the list of tiles that need revealing
                #reveal neighbors of this tile iff this tile's neighbor bomb count is zero
                if tiles[tiles_to_reveal[0]].neighbor_bomb_count == 0:
                    #do a select on all neighbors
                    is_left_edge = (i % GRID_WIDTH == 0)
                    is_right_edge = (i % GRID_WIDTH == GRID_WIDTH - 1)
                    is_top_edge = (i < GRID_WIDTH)
                    is_bottom_edge = (i >= (GRID_WIDTH * (GRID_HEIGHT - 1)))
                    if not is_top_edge and not is_left_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i -GRID_WIDTH -1) #above left
                    if not is_top_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i -GRID_WIDTH) #above
                    if not is_top_edge and not is_right_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i -GRID_WIDTH +1) #above right
                    if not is_left_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i -1) #left
                    if not is_right_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i +1) #right
                    if not is_bottom_edge and not is_left_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i +GRID_WIDTH -1) #below left
                    if not is_bottom_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i +GRID_WIDTH) #below
                    if not is_bottom_edge and not is_right_edge and not tiles[tiles_to_reveal[0]].revealed: tiles_to_reveal.append(i +GRID_WIDTH +1) #below right
                tiles[tiles_to_reveal[0]].revealed = True
                print(tiles_to_reveal.pop(0))
    # if check_win():
    #     game_on = False
    # game_on = False if check_win() else True
    if check_win() and not game_over:
        game_on_lbl.config(text="You WON")

def bomb_count_neighbors():
    for i in range(len(tiles)):
        neighbor_bomb_count = 0
        is_left_edge = (i % GRID_WIDTH == 0)
        is_right_edge = (i % GRID_WIDTH == GRID_WIDTH -1)
        is_top_edge = (i < GRID_WIDTH)
        is_bottom_edge = (i >= (GRID_WIDTH*(GRID_HEIGHT -1)) )

        if tiles[i].bomb == False:
            #here if current indexed tile does not have a bomb
            if not is_left_edge and not is_top_edge and tiles[i -GRID_WIDTH -1].bomb: neighbor_bomb_count +=1 #above left
            if not is_top_edge and tiles[i - GRID_WIDTH].bomb: neighbor_bomb_count += 1 #above
            if not is_right_edge and not is_top_edge and tiles[i -GRID_WIDTH +1].bomb: neighbor_bomb_count +=1 #above right
            if not is_left_edge and tiles[i -1].bomb: neighbor_bomb_count +=1 #left
            if not is_right_edge and tiles[i +1].bomb: neighbor_bomb_count +=1 #right
            if not is_left_edge and not is_bottom_edge and tiles[i +GRID_WIDTH -1].bomb: neighbor_bomb_count +=1 #below left
            if not is_bottom_edge and tiles[i +GRID_WIDTH].bomb: neighbor_bomb_count +=1 #below
            if not is_bottom_edge and not is_right_edge and tiles[i +GRID_WIDTH +1].bomb: neighbor_bomb_count +=1 #below right
            #--------------------------------------------#
            # if i > 0 and not is_left_edge and tiles[i -1].bomb: neighbor_bomb_count +=1 #left
            # if i > GRID_WIDTH-1 and not is_right_edge and tiles[i +1 -GRID_WIDTH].bomb: neighbor_bomb_count +=1 #above right
            # if i > GRID_WIDTH and tiles[i -GRID_WIDTH].bomb: neighbor_bomb_count +=1 #above
            # if i > GRID_WIDTH +1 and not is_left_edge and tiles[i -1 -GRID_WIDTH].bomb: neighbor_bomb_count +=1 #above left
            # if i < (GRID_WIDTH*GRID_HEIGHT -1) and not is_right_edge and tiles[i +1].bomb: neighbor_bomb_count +=1 #right
            # if i < (GRID_WIDTH*(GRID_HEIGHT -1)) and not is_left_edge and tiles[i -1 +GRID_WIDTH].bomb: neighbor_bomb_count +=1 #below left
            # if i < ((GRID_WIDTH*(GRID_HEIGHT -1)) -1) and not is_right_edge and tiles[i +1 +GRID_WIDTH].bomb: neighbor_bomb_count +=1 #below right
            # if i < ((GRID_WIDTH*(GRID_HEIGHT -1)) -1) and tiles[i +GRID_WIDTH].bomb: neighbor_bomb_count +=1 #below

            tiles[i].neighbor_bomb_count = neighbor_bomb_count
            tiles[i].config(text=f"{neighbor_bomb_count}")

def generate_tiles(width, height):
    ids = 0
    for x in range(width):
        for y in range(height):
            new_tile = Tile("#")
            new_tile.id = ids
            ids += 1
            new_tile.config(command=partial(
                tile_select, new_tile
            ))
            tiles.append(new_tile)

def plant_bombs(bombs_to_make):
    for i in range(bombs_to_make):
        tiles[i].bomb = True
        tiles[i].config(text=tiles[i].bomb_text)
    random.shuffle(tiles)

def generate_grid():
    index = 0
    for x in range(1,GRID_WIDTH+1):
        for y in range(1,GRID_HEIGHT+1):
            tiles[index].xcor = x
            tiles[index].ycor = y

            tiles[index].place(x=placements['tiles_origin_x']+(y * TILE_DIM), y=placements['tiles_origin_y']+(x * TILE_DIM), width=TILE_DIM, height=TILE_DIM)
            index += 1
    bomb_count_neighbors()

def change_flag_mode():
    global is_flag_mode
    is_flag_mode = False if is_flag_mode else True
    if is_flag_mode:
        flag_btn.config(bg="red")
    else:
        flag_btn.config(bg="gray")

window = tkinter.Tk()
window.title("PySweeper")
window.config(width=SIDE_CONTROLS_WIDTH + (TILE_DIM * (GRID_WIDTH + 2)), height=(TILE_DIM * (GRID_HEIGHT + 2)))

flag_btn = tkinter.Button(text="Flag Mode", fg="white", bg="gray", command=change_flag_mode)
flag_btn.place(x=placements['flag_btn_x'], y=placements['flag_btn_y'], width=80, height=80)

game_on_lbl = tkinter.Label(text="Game On", fg="white", bg="gray")
game_on_lbl.place(x=placements['game_on_lbl_x'], y=placements['game_on_lbl_y'])

generate_tiles(GRID_WIDTH, GRID_HEIGHT)
plant_bombs(NUM_BOMBS)
generate_grid()



window.mainloop()
