
def specialPlant(x):
	if x in needsTill:
		if get_ground_type() == Grounds.Grassland:
			till()
	if can_harvest():
		harvest()
	if x == "WoodGrass":
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Grass)
	else:
		plant(x)
	if get_water() < 0.5:
		use_item(Items.Water)
	#use_item(Items.Fertilizer)
	
    
def coverPlant(x, m=1):
	for _ in range(m):
		for _ in range(get_world_size()):
			specialPlant(x)
			move(North)
		if m != 1:
			move(East)