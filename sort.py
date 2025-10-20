def zero_x():
	while get_pos_x() > 0:
		move(West)

def zero_y():
	while get_pos_y() > 0:
		move(South)

def goto_top():
	while get_pos_y() < get_world_size() - 1:
		move(North)

def bubble_sort_x():
	n = get_world_size()
	for i in range(n-1):
		for j in range(n-i-1):
			if measure() > measure(East):
				swap(East)
			move(East)
		zero_x()

def bubble_sort_y():
	n = get_world_size()
	for i in range(n-1):
		for j in range(n-i-1):
			if measure() > measure(North):
				swap(North)
			move(North)
		zero_y()

def turnLeft(i):
	i += 1
	if i > 3:
		i = 0
	return i

def turnRight(i):
	i -= 1
	if i < 0:
		i = 3
	return i

def treasure_hunt_right_hand():
	dir = (West,North,East,South)
	i = 0
	x = get_pos_x()
	y = get_pos_y()
	while True:
		move(dir[i])
		x2 = get_pos_x()
		y2 = get_pos_y()	
		if x==x2 and y==y2:
			i = turnLeft(i)
		else:
			x = get_pos_x()
			y = get_pos_y()
			i = turnRight(i)
		if get_entity_type()==Entities.Treasure:
			harvest()
			break