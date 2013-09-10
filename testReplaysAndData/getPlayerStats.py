import sys
import os
import json 
import Image
import ImageDraw
from multiprocessing import Process

global json_data
# to be set
global chosenPlayer
global replayNumber

#---------------------------
# SHOULDN'T BE HARDCODED
chosenPlayer = "dd Funzii"
replayNumber = "194861937"
#---------------------------

# Initialise globals
json_data=open("json/" + replayNumber + "/" + "players" + ".json")

playerList = []
playerGoldOverTime = []
playerTotalGoldOverTime = []
playerGPMOverTime = []
playerXPOverTime = []
playerLevelOverTime = []
playerCSOverTime = []
playerItemProgressionOverTime = []
playerKillsOverTime = []
playerAssistsOverTime = []
playerDeathsOverTime = []
playerBuildingKillsOverTime = []
playerDamageDealtOverTime = []
playerDamageTakenOverTime = []
playerBuybackOverTime = []

playerTotalCS = 0
playerTotalDenies = 0
playerTotalNeuts = 0
playerTotalEnemyRangeCreep = 0
playerTotalEnemyMeleeCreep = 0
playerTotalDenyMeleeCreep = 0
playerTotalDenyRangeCreep = 0
playerTotalDenyNeuts = 0
playerTotalGold = 0
playerTotalXP = 0
playerMaxLevel = 0
playerTotalDamageDealt = 0
playerTotalDamageTaken = 0
playerTotalDivines = 0

def loadJSON(jsonName) :
	json_data=open("json/" + replayNumber + "/" + jsonName + ".json")
	return json.load(json_data)

def closeJSON() :
	json_data.close()

def generatePlayerLevelGraph(playerLevelOverTime) :
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime = float(playerLevelOverTime[-1][0])
	maxLevel = float(playerLevelOverTime[-1][1])
	draw.line((0, imageHeight, float(playerLevelOverTime[0][0])/maxTime*imageWidth, imageHeight-float(playerLevelOverTime[0][1])/maxLevel*imageHeight), fill=(0,0,0))
	for i in range(len(playerLevelOverTime)-1) :
		draw.line((float(playerLevelOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerLevelOverTime[i][1])/maxLevel*imageHeight, float(playerLevelOverTime[i+1][0])/maxTime*imageWidth, imageHeight-float(playerLevelOverTime[i+1][1])/maxLevel*imageHeight), fill=(0,0,0))
		draw.text((float(playerLevelOverTime[i+1][0])/maxTime*imageWidth, imageHeight-30.0), str(playerLevelOverTime[i+1][1]).title(), fill=(255,0,0))

	del draw

	im.save("playerLevelGraph.png")

def generatePlayerKillsGraph(playerKillsOverTime) :	
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime = float(playerKillsOverTime[-1][0])
	numberOfKills = float(len(playerKillsOverTime))
	#draw.line((0, imageHeight, float(playerKillsOverTime[0][0])/maxTime*imageWidth, imageHeight-1.0/numberOfKills*imageHeight), fill=(0,0,0))
	for i in range(len(playerKillsOverTime)-1) :
		draw.line((float(playerKillsOverTime[i][0])/maxTime*imageWidth, imageHeight-float(i)/numberOfKills*imageHeight, float(playerKillsOverTime[i+1][0])/maxTime*imageWidth, imageHeight-float(i+1)/numberOfKills*imageHeight), fill=(0,0,0))
		draw.text((float(playerKillsOverTime[i+1][0])/maxTime*imageWidth, imageHeight-30.0), playerKillsOverTime[i+1][1].title(), fill=(255,0,0))

	del draw

	im.save("playerKillsGraph.png")

def generatePlayerDeathsGraph(playerDeathsOverTime) :
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime = float(playerDeathsOverTime[-1][0])
	numberOfDeaths = float(len(playerDeathsOverTime))
	#draw.line((0, imageHeight, float(playerDeathsOverTime[0][0])/maxTime*imageWidth, imageHeight-1.0/numberOfDeaths*imageHeight), fill=(0,0,0))
	for i in range(len(playerDeathsOverTime)-1) :
		draw.line((float(playerDeathsOverTime[i][0])/maxTime*imageWidth, imageHeight-float(i)/numberOfDeaths*imageHeight, float(playerDeathsOverTime[i+1][0])/maxTime*imageWidth, imageHeight-float(i+1)/numberOfDeaths*imageHeight), fill=(0,0,0))
		draw.text((float(playerDeathsOverTime[i+1][0])/maxTime*imageWidth, imageHeight-30.0), playerDeathsOverTime[i+1][1].title(), fill=(255,0,0))

	del draw

	im.save("playerDeathsGraph.png")

def generatePlayerAssistsGraph(playerAssistsOverTime) :
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime = float(playerAssistsOverTime[-1][0])
	numberOfAssists = float(len(playerAssistsOverTime))
	#draw.line((0, imageHeight, float(playerAssistsOverTime[0][0])/maxTime*imageWidth, imageHeight-1.0/numberOfAssists*imageHeight), fill=(0,0,0))
	for i in range(len(playerAssistsOverTime)-1) :
		draw.line((float(playerAssistsOverTime[i][0])/maxTime*imageWidth, imageHeight-float(i)/numberOfAssists*imageHeight, float(playerAssistsOverTime[i+1][0])/maxTime*imageWidth, imageHeight-float(i+1)/numberOfAssists*imageHeight), fill=(0,0,0))
		draw.text((float(playerAssistsOverTime[i+1][0])/maxTime*imageWidth, imageHeight-30.0), playerAssistsOverTime[i+1][1].title(), fill=(255,0,0))

	del draw

	im.save("playerAssistsGraph.png")

def generatePlayerGoldGraph(playerTotalGoldOverTime) :
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime =  float(playerTotalGoldOverTime[-1][0])
	maxGold = float(playerTotalGoldOverTime[-1][1])
	draw.line((0, imageHeight, float(playerTotalGoldOverTime[0][0])/maxTime*imageWidth, imageHeight-float(playerTotalGoldOverTime[0][1])/maxGold*imageHeight), fill=(0,0,0))
	for i in range(len(playerTotalGoldOverTime)-1) :
		draw.line((float(playerTotalGoldOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerTotalGoldOverTime[i][1])/maxGold*imageHeight, float(playerTotalGoldOverTime[i+1][0])/maxTime*imageWidth, imageHeight-float(playerTotalGoldOverTime[i+1][1])/maxGold*imageHeight), fill=(0,0,0))
		#draw.text((float(playerTotalGoldOverTime[i+1][0])/float(maxTime)*imageWidth, float(playerTotalGoldOverTime[i+1][1])/float(maxGold)*imageHeight), str(playerTotalGoldOverTime[i+1][1]).title(), fill=(255,0,0))

	del draw

	im.save("playerGoldGraph.png")

def generatePlayerGPMGraph(playerGPMOverTime) :
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime = float(playerGPMOverTime[-1][0])
	maxGPM = 0
	for i in range(len(playerGPMOverTime)) :
		if playerGPMOverTime[i][1] > maxGPM :
			maxGPM = float(playerGPMOverTime[i][1])

	#draw.line((0, imageHeight, float(playerGPMOverTime[0][0])/maxTime*imageWidth, imageHeight-float(playerGPMOverTime[0][1])/maxGPM*imageHeight), fill=(0,0,0))
	for i in range(len(playerGPMOverTime)-1) :
		draw.line((float(playerGPMOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerGPMOverTime[i][1])/maxGPM*imageHeight, float(playerGPMOverTime[i+1][0])/maxTime*imageWidth, imageHeight-float(playerGPMOverTime[i+1][1])/maxGPM*imageHeight), fill=(0,0,0))
		#draw.text((playerGPMOverTime[i+1][0]/10, playerGPMOverTime[i+1][1]*10), str(playerGPMOverTime[i+1][1]).title(), fill=(255,0,0))

	del draw

	im.save("playerGPMGraph.png")

def generatePlayerDamageDealtGraph(playerDamageDealtOverTime) :
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime = float(playerDamageDealtOverTime[-1][0])
	maxDamage = 0
	for i in range(len(playerDamageDealtOverTime)) :
		if playerDamageDealtOverTime[i][2] > maxDamage :
			maxDamage = float(playerDamageDealtOverTime[i][2])
	if maxDamage == 0 :
		pass
	#draw.line((0, imageHeight, float(playerDamageDealtOverTime[0][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[0][2])/maxDamage*imageHeight), fill=(0,0,0))
	#for i in range(len(playerDamageDealtOverTime)-1) :
		#draw.line((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight, float(playerDamageDealtOverTime[i+1][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i+1][2])/maxDamage*imageHeight), fill=(0,0,0))
		#draw.text((playerDamageDealtOverTime[i+1][0]/10, playerDamageDealtOverTime[i+1][1]*10), str(playerDamageDealtOverTime[i+1][1]).title(), fill=(255,0,0))
	for i in range(len(playerDamageDealtOverTime)) :
		draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight), fill=(0,0,0))
		draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth-1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight), fill=(0,0,0))
		draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth+1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight), fill=(0,0,0))
		draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight-1), fill=(0,0,0))
		draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight+1), fill=(0,0,0))

	del draw

	im.save("playerDamageDealtGraph.png")

def generatePlayerDamageDealtSpecificGraph(playerDamageDealtOverTime, dealtTo) :
	imageWidth = 800.0
	imageHeight = 500.0
	im = Image.new("RGB", (800, 500), "white")
	draw = ImageDraw.Draw(im)
	maxTime = float(playerDamageDealtOverTime[-1][0])
	maxDamage = 0
	for i in range(len(playerDamageDealtOverTime)) :
		if playerDamageDealtOverTime[i][2] > maxDamage and dealtTo in playerDamageDealtOverTime[i][1] :
			maxDamage = float(playerDamageDealtOverTime[i][2])
	if maxDamage == 0 :
		pass
	#draw.line((0, imageHeight, float(playerDamageDealtOverTime[0][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[0][2])/maxDamage*imageHeight), fill=(0,0,0))
	for i in range(len(playerDamageDealtOverTime)) :
		if dealtTo in playerDamageDealtOverTime[i][1] :
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight), fill=(0,0,0))
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth-1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight), fill=(0,0,0))
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth+1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight), fill=(0,0,0))
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight-1), fill=(0,0,0))
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight+1), fill=(0,0,0))

			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth-1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight-1), fill=(0,0,0))
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth+1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight+1), fill=(0,0,0))
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth+1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight-1), fill=(0,0,0))
			draw.point((float(playerDamageDealtOverTime[i][0])/maxTime*imageWidth-1, imageHeight-float(playerDamageDealtOverTime[i][2])/maxDamage*imageHeight+1), fill=(0,0,0))


	del draw

	im.save("playerDamageDealtTo" + dealtTo.replace("npc_dota_hero_","").replace("_", " ").title().replace(" ", "") + "Graph.png")





#def loadData() :

	
if __name__ == '__main__' :
	players = loadJSON("players")


	#-----------------------------------------------------------
	# LOAD PLAYER DATA
	for field in players["players"] :
		playerName = field["player"]
		hero = field["hero"]
		if playerName == chosenPlayer :
			chosenHero = hero
		playerList.append((playerName, hero))

	playerObserved = {"name" : chosenPlayer, "hero" : hero}

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET GOLD INFO

	gold = loadJSON("gold")

	for field in gold["gold"] :
		if field["hero"] ==  playerObserved["hero"] :
			time = field["time"]
			gold = field["gold"]
			playerGoldOverTime.append((time, gold))
			playerTotalGold += field["gold"]
			playerTotalGoldOverTime.append((time, playerTotalGold))
			playerGPMOverTime.append((time, playerTotalGold/(time/60)))

	closeJSON()
	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET LEVELUP INFORMATION

	levelup = loadJSON("levelups")

	for field in levelup["leveluptimes"] :
		if field["hero"] == playerObserved["hero"] :
			time = field["time"]
			level = field["level"]
			playerLevelOverTime.append((time, level))

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET CS INFORMATION

	cs = loadJSON("cs")

	for field in cs["cs"] :
		if field["hero"] == playerObserved["hero"] :
			time = field["time"]
			creepKilled = field["kill"]
			if creepKilled.startswith("npc_dota_creep_badguys_melee") :
				playerTotalEnemyMeleeCreep += 1
			elif creepKilled.startswith("npc_dota_creep_badguys_range") :
				playerTotalEnemyRangeCreep += 1
			elif creepKilled.startswith("npc_dota_neutral") :
				playerTotalNeuts += 1

			playerTotalCS += 1
			playerCSOverTime.append((time, creepKilled, creepKilled))

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET DENY INFORMATION
	 
	denies = loadJSON("denies")

	for field in denies["denies"] :
		if field["hero"] == playerObserved["hero"] :
			time = field["time"]
			creepKilled = field["kill"]
			if creepKilled.startswith("npc_dota_creep_badguys_melee") :
				playerTotalDenyMeleeCreep += 1
			elif creepKilled.startswith("npc_dota_creep_badguys_range") :
				playerTotalDenyRangeCreep += 1
			elif creepKilled.startswith("npc_dota_neutral") :
				playerTotalDenyNeuts += 1

			playerTotalDenies += 1
			playerCSOverTime.append((time, creepKilled, creepKilled))

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET ITEM PROGRESSION

	itemtimes = loadJSON("itemtimes")

	for field in itemtimes["itemtimes"] :
		if field["hero"] == playerObserved["hero"] :
			time = field["time"]
			item = field["item"]
			if "divine" in item :
				playerTotalDivines += 1
			playerItemProgressionOverTime.append((time, item))

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET KILLS INFO

	herokills = loadJSON("herokills")

	for field in herokills["herokills"] :
		if field["killer"] == playerObserved["hero"] :
			time = field["time"]
			dead = field["dead"]
			playerKillsOverTime.append((time, dead))
		if playerObserved["hero"] in field["assists"] :
			time = field["time"]
			dead = field["dead"]
			playerAssistsOverTime.append((time, dead))
		if field["dead"] == playerObserved["hero"] :
			time = field["time"]
			killedBy = field["killer"]
			playerDeathsOverTime.append((time, killedBy))		

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET TOWER INFO

	buildings = loadJSON("buildings")

	for field in buildings["buildingtimers"] :
		if field["killer"] == playerObserved["hero"] :
			time = field["time"]
			building = field["building"]
			playerBuildingKillsOverTime.append((time, building))

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET RUNE INFO

	runes = loadJSON("runes")

	for field in runes["runes"] :
		if field["hero"] == playerObserved["hero"] :
			time = field["time"]

			if field["rune"] == 0 :
				rune = "double_damage"
			elif field["rune"] == 1 :
				rune = "haste"
			elif field["rune"] == 2 :
				rune = "illusion"
			elif field["rune"] == 3 :
				rune = "regen"
			elif field["rune"] == 4 :
				rune = "invisibility"

			bottle = field["bottle"]
			playerBuildingKillsOverTime.append((time, rune, bottle))

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET COMBAT LOG INFO

	combatlog = loadJSON("combatlog")

	for field in combatlog["combatlog"] :
		time = field["time"]
		damage = field["value"]
		if field["source"] == playerObserved["hero"] :
			target = field["target"]
			playerTotalDamageDealt += damage
			playerDamageDealtOverTime.append((time, target, damage))
		if field["target"] == playerObserved["hero"] :
			damageFrom = field["source"]
			playerTotalDamageTaken += damage
			playerDamageTakenOverTime.append((time, damageFrom, damage))

	closeJSON()

	#-----------------------------------------------------------

	#-----------------------------------------------------------
	# GET BUYBACK INFO

	buybacks = loadJSON("buybacks")

	for field in buybacks["buybacks"] :
		if field["player"] == playerObserved["hero"] :
			time = field["time"]
			for i in range(len(playerLevelOverTime)) :
				if time >= playerLevelOverTime[i][0] :
					buybackLevel = playerLevelOverTime[i][1]
			level = buybackLevel
			playerBuybackOverTime.append((time, level))

	closeJSON()

	#-----------------------------------------------------------

	# Multiprocessing (is this done properly?)
	playerKillProcess = Process(target=generatePlayerKillsGraph, args=(playerKillsOverTime,))
	playerKillProcess.start()
	playerKillProcess.join()
	playerDeathProcess = Process(target=generatePlayerDeathsGraph, args=(playerDeathsOverTime,))
	playerDeathProcess.start()
	playerDeathProcess.join()
	playerAssistProcess = Process(target=generatePlayerAssistsGraph, args=(playerAssistsOverTime,))
	playerAssistProcess.start()
	playerAssistProcess.join()
	playerLevelProcess = Process(target=generatePlayerLevelGraph, args=(playerLevelOverTime,))
	playerLevelProcess.start()
	playerLevelProcess.join()
	playerGoldProcess = Process(target=generatePlayerGoldGraph, args=(playerTotalGoldOverTime,))
	playerGoldProcess.start()
	playerGoldProcess.join()
	playerGPMProcess = Process(target=generatePlayerGPMGraph, args=(playerGPMOverTime,))
	playerGPMProcess.start()
	playerGPMProcess.join()
	playerDamageDealtProcess = Process(target=generatePlayerDamageDealtGraph, args=(playerDamageDealtOverTime,))
	playerDamageDealtProcess.start()
	playerDamageDealtProcess.join()

	for i in range(len(playerList)) :
		playerDamageDealtSpecificProcess = Process(target=generatePlayerDamageDealtSpecificGraph, args=(playerDamageDealtOverTime, playerList[i][1]))
		playerDamageDealtSpecificProcess.start()
		playerDamageDealtSpecificProcess.join()

# Print statements for debugging
# print "Player " + playerObserved["name"] + " earned " + str(playerTotalGold) + " gold during the match."
# print "They also reached level " + str(playerLevelOverTime[-1][1])
# print "CS: " + str(playerTotalCS) + ", Denies: " + str(playerTotalDenies)
# print "This comprises of " + str(playerTotalEnemyMeleeCreep+playerTotalEnemyRangeCreep) + " enemy creeps and " + str(playerTotalNeuts) + " neutrals killed."
# print "Also, " + str(playerTotalDenyMeleeCreep+playerTotalDenyRangeCreep) + " enemy creeps and " + str(playerTotalDenyNeuts) + " neutrals denied."
# print "Last item bought was " + str(playerItemProgressionOverTime[-1][1].replace("modifier_item_", "").replace("_", " ").title()) + "."
# print "This was at " + str(playerItemProgressionOverTime[-1][0]/60/60) + " mins."
# print "Number of kills: " + str(len(playerKillsOverTime)) 
# print "Number of assists: " + str(len(playerAssistsOverTime))
# print "Number of deaths: " + str(len(playerDeathsOverTime))
# print "Buildings killed: "  + str(len(playerBuildingKillsOverTime))
# print "Damage dealt: " + str(playerTotalDamageDealt)
# print "Damage taken: " + str(playerTotalDamageTaken)



