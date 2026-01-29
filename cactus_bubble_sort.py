# Cactus: plant -> sort (by measure()) -> harvest
# Works on the cactus challenge where "height/value" is read with measure()
# Set SIZE to your field size (e.g., 6 for a 6x6 field)

SIZE = 16

def back(x=0, y=0):
	while x != get_pos_x() or y != get_pos_y():
		if get_pos_x() < x:
			move(East)
		elif get_pos_x() > x:
			move(West)

		if get_pos_y() < y:
			move(North)
		elif get_pos_y() > y:
			move(South)

def reverse(dir):
	if dir == West:  
		return East
	if dir == East:  
		return West
	if dir == North: 
		return South
	if dir == South: 
		return North

def plant_cactus():
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Cactus)

def cactus_cycle(size=SIZE):
	while True:
		# 1) Plant in a snake pattern (covers whole field)
		dir = East
		vdir = North
		for i in range(size):
			for j in range(size):
				plant_cactus()
				if j != size - 1:
					move(dir)
			if i != size - 1:
				move(vdir)
			dir = reverse(dir)
		vdir = reverse(vdir)

		# 2) Sort until fully sorted horizontally AND vertically
		# Horizontal goal: ascending left->right on each row (snake-aware via dir)
		# Vertical goal: ascending bottom->top (so we swap South/North accordingly)
		sorted_h = False
		sorted_v = False
		while not sorted_h or not sorted_v:
			sorted_h = True
			sorted_v = True

			dir = East
			vdir = North
			back(0, 0)

			for i in range(size):
				for j in range(size):
					x = get_pos_x()
					y = get_pos_y()

					current = measure()
					neighbor = measure(dir)
					down = measure(South)
					up = measure(North)

					# Horizontal swaps
					if dir == East and x != size - 1 and neighbor != None and current > neighbor:
						swap(East)
						sorted_h = False
					if dir == West and x != 0 and neighbor != None and current < neighbor:
						swap(West)
						sorted_h = False

					# Vertical swaps (bottom->top ascending)
					if y != 0 and down != None and current < down:
						swap(South)
						sorted_v = False
					if y != size - 1 and up != None and current > up:
						swap(North)
						sorted_v = False

					if j != size - 1:
						move(dir)

				if i != size - 1:
					move(vdir)
				dir = reverse(dir)

		# 3) Harvest (cactus challenge harvests the whole field at once)
		back(0, 0)
		harvest()

clear()
cactus_cycle(SIZE)

