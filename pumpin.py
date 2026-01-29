import tools

def move_to(x, y):
	while x != get_pos_x() or y != get_pos_y():
		if get_pos_x() < x:
			move(East)
		elif get_pos_x() > x:
			move(West)

		if get_pos_y() < y:
			move(North)
		elif get_pos_y() > y:
			move(South)

def plantAll():
	clear()
	for _ in range(get_world_size()):
		tools.coverPlant(Entities.Pumpkin)
		move(East)

def scan_dead_positions():
	positions = []
	size = get_world_size()
	start_x = get_pos_x()
	start_y = get_pos_y()
	for _ in range(size):
		for _ in range(size):
			if get_entity_type() == Entities.Dead_Pumpkin:
				positions.append((get_pos_x(), get_pos_y()))
			move(North)
		move(East)
	move_to(start_x, start_y)
	return positions

def replant_positions(positions):
	idx = 0
	while idx < len(positions):
		x, y = positions[idx]
		move_to(x, y)
		if get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
			plant(Entities.Pumpkin)
			idx = idx + 1
		else:
			positions.pop(idx)

def MegaPumpkin():
	while(True):
		plantAll()
		positions = scan_dead_positions()
		while len(positions) > 0:
			replant_positions(positions)
		positions = scan_dead_positions()
		while len(positions) > 0:
			replant_positions(positions)
		harvest()
	