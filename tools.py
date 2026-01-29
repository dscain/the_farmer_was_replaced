
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
			
def coverBoardSetup(x):
	coverPlant(Entities.Sunflower)
	move(East)
	coverPlant(Entities.Carrot,6)
	coverPlant(Entities.Carrot,5)	
	coverPlant("WoodGrass",4)

	


def coverBoardComplete(x, drones=None):
	unlock(Unlocks.Grass)
	unlock(Unlocks.Trees)
	unlock(Unlocks.Auto_Unlock)
	coverPlant(Entities.Sunflower)
	move(East)
	coverPlant(Entities.Sunflower)
	move(East)
	if drones == None:
		drones = max_drones()
	if drones > max_drones():
		drones = max_drones()
	for _ in range(get_world_size()-2):
		if num_drones() < drones:
			def task():
				coverPlant(x)
			spawn_drone(task)
		else:
			coverPlant(x)
		move(East)
	#unlock(Unlocks.Grass)
	
	
needsTill = [Entities.Sunflower, Entities.Carrot, Entities.Pumpkin, Entities.Cactus]
			