import tools

# plant
def plantAll():
	clear()
	for _ in range(get_world_size()):
		tools.coverPlant(Entities.Pumpkin)
		move(East)
		
# clear
def clearAll():
	hasDead = False
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_entity_type() == Entities.Dead_Pumpkin:
				harvest()
				plant(Entities.Pumpkin)
				hasDead = True
			move(North)
		move(East)
	return hasDead

def MegaPumpkin():
	while(True):		
		plantAll()
		while(clearAll()):
			get_cost(Entities.Pumpkin)
			
		harvest()
	