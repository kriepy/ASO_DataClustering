import math
import random

datasetSize = 1200		# Determine later
dropThreshold = 0.5		# Determine later
pickupThreshold = 0.5	# Determine later

pickupConst = 1
dropConst = 1
alpha = 1

# Classes
class Ant:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.load = None

class DataItem:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# Chance an ant picks up the item on its position: ( Kp / ( Kp + F(i) )^2
def pickupChance(ant):
	math.pow((pickupConst / (pickupConst + localSimilarity(ant))), 2)
	return
	
# Chance an ant drops an item on its current position:
#	if F(i) < Kd	2F(i)
#	else				1
def dropChance(ant):
	locSim = localSimilarity(ant)
	if locSim < dropConst:
		return 2 * locSim
	return 1

# Calculate local similarity
def localSimilarity(ant):
	locality = 1 / math.pow(localDist * 2, 2)
	locSim = 0;
	for cono in antColony:
		if inLocalArea(ant, cono):
			locSim += (1 - similarity(ant, cono) / alpha)
	
	result = locality * locSim;
	return max(result, 0)

# Determine if one ant is in local area of the other
def inLocalArea(ant1, ant2):
	if abs(ant1.x - ant2.x) <= localDist and abs(ant1.y - ant2.y) <= localDist:
		return True 
	return False

# Distance between to items
def similarity(i, j):
	# TODO, depends on data
	return

# Creates ants and places them randomly on grid
def createAnts(nrOfAnts):
	for i in range(1, nrOfAnts):
		antColony.append(Ant(random.randint(0, gridUpperXBound), random.randint(0, gridUpperYBound)))
	return

def loadDataItems():
	# TODO, depends on data
	return

def itemOnLocation(ant):
	for item in dataItems:
		if item.x == ant.x and item.y == ant.y:
			return True
	return False

def moveAnt(ant):
	chance = random.random()
	if chance > 0.75:
		ant.x += 1
	elif chance > 0.5:
		ant.x -= 1
	elif chance > 0.25:
		ant.y += 1
	else:
		ant.y -= 1
	return

# Create 2D grid which has a surface of 10N: 10 * sqrt(N) by 10 * sqrt(N)
gridLowerXBound = 0
gridLowerYBound = 0
gridUpperXBound = int(10 * math.sqrt(datasetSize))
gridUpperYBound = int(10 * math.sqrt(datasetSize))

# Define local area size
localDist = 5			#Determine later

#Create N/10 number of ants and place randomly in grid
antColony = []
createAnts(datasetSize/10)

# Load data and place data items randomly in the grid
dataItems = []
loadDataItems()


while 1:
	# Select a random ant
	ant = random.choice(antColony)
	
	if ant.load is not None:
		if dropChance(ant) > dropThreshold:
			dropItem(ant)
	elif itemOnLocation(ant):
		if pickupChance(ant) > pickupThreshold:
			pickupItem(ant)
	
	# Move ant in random direction
	moveAnt(ant)

