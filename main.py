import tools	

def getCarrots():
	clear()
	while(True):
		Organized.coverBoardSetup(None)
		#coverBoardComplete("WoodGrass")
		
def getCactus():
	import CactusBubbleSort
	
def getPumpkin():
	import MegaPumping
	MegaPumping.MegaPumpkin()
	
def getWood():
	clear()
	while(True):
		#Organized.coverBoardSetup(None)
		#tools.coverBoardComplete(Entities.Tree)
		tools.coverBoardComplete("WoodGrass")
		
def getMaze():
	import maze

def getDino():
	import DinoMax
	
#getCarrots()	
#getCactus()
#getPumpkin()
getWood()
#getDino()
	