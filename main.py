from plant import *
from farmLayout import *
from sort import *

reset()

FarmType = "Cactus"

if FarmType == "Default":
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
					harvest()
				plant_id(FarmType,i,j)
				fertilize_id(FarmType,i,j)
				if get_water() < 0.1 and get_entity_type() == Entities.Carrot:
					use_item(Items.Water)
				move(East)
			move(North)

if FarmType == "PumpkinOpt":
	#Spawn planters
	inc = 1
	for i in range(max_drones()-1):
		goto_coords(0,inc*i)
		spawn_drone(partitioned_planter_pumpkin)
	#Run harvest
	coordList = find_Pumpkin_corners(FarmType,6)
	pumpkin_harvester(coordList)
	
if FarmType == "Cactus":
	while True:
		#Plant all Cactai
		for_all(plant_cactus)
		goto_coords(0,0)
		#Sort all Cactus
		for i in range(get_world_size()-1):
			spawn_drone(bubble_sort_x)
			move(North)
		bubble_sort_x()
		while num_drones() > 1:
			pass
		move(North)
		for i in range(get_world_size()-1):
			spawn_drone(bubble_sort_y)
			move(East)
		bubble_sort_y()
		while num_drones() > 1:
			pass
		move(East)
		goto_top()
		harvest()
		move(North)

if FarmType == "Maze":
	size = 5
	for i in range(4):
		for j in range(4):
			goto_coords(2*size*(i),2*size*(j))
			spawn_drone(make_and_solve_maze)
	goto_coords(28,28)
	make_and_solve_maze()