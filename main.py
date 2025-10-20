from plant import *
from farmLayout import *
from sort import *

reset()

FarmType = "Maze"

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
	spawn_drone(partitioned_planter_pumpkin)
	goto_coords(0,11)
	spawn_drone(partitioned_planter_pumpkin)
	goto_coords(0,22)
	spawn_drone(partitioned_planter_pumpkin)
	#Run harvest
	coordList = find_Pumpkin_corners(FarmType,6)
	pumpkin_harvester(coordList)
	
if FarmType == "Cactus":
	while True:
		#Plant all Cactai
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				plant_cactus()
				move(East)
			move(North)
		#Sort all Cactus
		for i in range(get_world_size()):
			bubble_sort_x()
			move(North)
		for i in range(get_world_size()):
			bubble_sort_y()
			move(East)
		goto_top()
		harvest()
		move(North)

if FarmType == "Maze":
	while True:
		init_maze(16)
		treasure_hunt_right_hand()
		clear()