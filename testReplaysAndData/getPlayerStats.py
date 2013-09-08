import sys
import os
import json

global json_data
# to be set
global chosenPlayer
global replayNumber

#---------------------------
# SHOULDN'T BE HARDCODED
chosenPlayer = "dd Funzii"
replayNumber = "194861937"
#---------------------------

json_data=open("json/" + replayNumber + "/" + "players" + ".json")

def loadJSON(jsonName) :
	json_data=open("json/" + replayNumber + "/" + jsonName + ".json")
	return json.load(json_data)

def closeJSON() :
	json_data.close()


playerGoldOverTime = []
playerXPOverTime = []
playerLevelOverTime = []
playerCSOverTime = []

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
#-----------------------------------------------------------
# LOAD PLAYER DATA

players = loadJSON("players")

for field in players["players"] :
	playerName = field["player"]
	hero = field["hero"]
	players[playerName] = hero

playerObserved = {"name" : chosenPlayer, "hero" : players[chosenPlayer]}

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
		playerTotalGold += int(field["gold"])

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






print "Player " + playerObserved["name"] + " earned " + str(playerTotalGold) + " gold during the match."
print "They also reached level " + str(playerLevelOverTime[-1][1])
print "CS: " + str(playerTotalCS) + ", Denies: " + str(playerTotalDenies)
print "This comprises of " + str(playerTotalEnemyMeleeCreep+playerTotalEnemyRangeCreep) + " enemy creeps and " + str(playerTotalNeuts) + " neutrals killed."
print "Also, " + str(playerTotalDenyMeleeCreep+playerTotalDenyRangeCreep) + " enemy creeps and " + str(playerTotalDenyNeuts) + " neutrals denied."