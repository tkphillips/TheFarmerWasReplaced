def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def plant_tree():
	plant(Entities.Tree)

def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)

def plant_cactus():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)

def init_maze(size):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def goto_coords(x,y):
	current_x = get_pos_x()
	current_y = get_pos_y()
	step_x = x - current_x
	step_y = y - current_y

	while get_pos_x() != x or get_pos_y() != y:
		if step_x < 0:
			move(West)
			step_x += 1
		elif step_x > 0:
			move(East)
			step_x -= 1
		if step_y < 0:
			move(South)
			step_y += 1
		elif step_y > 0:
			move(North)
			step_y -= 1


def pumpkin_harvester(pumpkinCorners):
	#Find pumpkins in array
	coordList = pumpkinCorners
	while True:
		for i in range(len(coordList)/2):
			goto_coords(coordList[2*i][0],coordList[2*i][1])
			corner1 = measure()
			goto_coords(coordList[(2*i)+1][0],coordList[(2*i)+1][1])
			corner2 = measure()
			if get_entity_type() == Entities.Pumpkin and corner1 == corner2:
				harvest()

def reset():
	clear()