# -*- coding: utf-8 -*-

############################################################################################################################
#
# Helps us with handling the Challonge JSONs we just downloaded
#
############################################################################################################################

class challongefileutils(object):

  def __init__(self, parent):
    self.parent = parent
    self.logger = parent.logger

  def mapUnfriendlyPlayerTag(self, player_tag):
    if player_tag == '&':
      return "Ampersand"
    else:
      return player_tag

  '''
  Arg: tournamentJsonFile by path
  Ret: json[] of tournamentJson from file (count: 1)

  TO DO: FileIO Error Catching
  '''
  def readTournamentJson(self, tournamentJsonFile):
    self.logger.info("Reading Tournament Json from File: %s" %str(tournamentJsonFile))

    jsonStringBuffer = str()
    tournamentJsonArray = list()

    with open(tournamentJsonFile) as file:
      for line in file:
        jsonStringBuffer += line.strip()
      file.close()

    tournamentJsonArray.append(jsonStringBuffer)

    self.logger.info("Successfully loaded Tournament from Json: %s" %str(tournamentJsonFile))
    return tournamentJsonArray

  '''
  Arg: participantsJson by path
  Abs: runs through participants file, removes brackets and adds braces to reform json
  Ret: json[] of participantsJson from file (count: N Participants)

  TO DO: FileIO Error Catching
  '''
  def readParticipantsJson(self, participantsJsonFile):
    self.logger.info("Reading Participants Json from File: %s" %str(participantsJsonFile))

    jsonStringBuffer = str()
    participantsJsonArray = list()

    with open(participantsJsonFile) as file:
      for line in file:
        jsonStringBuffer += line.strip()
      file.close()

    participantsJsonArray = jsonStringBuffer.split('},{')
    
    #Grab the final index of array for bracket ('[', ']') removal
    endIndex = len(participantsJsonArray) - 1
    
    participantsJsonArray[0] = participantsJsonArray[0][1:]
    participantsJsonArray[endIndex] = participantsJsonArray[endIndex][:-1]

    #Prepend and Append curly braces where necessary
    for i in range(0, len(participantsJsonArray)):
      if i != 0 and i != endIndex:
        participantsJsonArray[i] = '{' + participantsJsonArray[i] + '}'
      elif i == 0:
        participantsJsonArray[i] = participantsJsonArray[i] + '}'
      elif i == endIndex:
        participantsJsonArray[i] = '{' + participantsJsonArray[i]

    #Lets see what this looks like
    self.logger.info("Successfully loaded Participants from Json: %s" %str(participantsJsonFile))
    return participantsJsonArray

  '''
  Arg: matchesJson by path
  Abs: runs through matches file, removes brackets and adds braces to reform json
  Ret: json[] of matchesJson from file (count: N Matches)

  TO DO: FileIO Error Catching
  '''
  def readMatches(self, matchesJsonFile):
    self.logger.info("Reading Matches Json from File: %s" %str(matchesJsonFile))

    jsonStringBuffer = str()
    matchesJsonArray = list()

    with open(matchesJsonFile) as file:
      for line in file:
        jsonStringBuffer += line.strip()
      file.close()

    matchesJsonArray = jsonStringBuffer.split('},{')
    
    #Grab the final index of array for bracket ('[', ']') removal
    endIndex = len(matchesJsonArray) - 1
    
    matchesJsonArray[0] = matchesJsonArray[0][1:]
    matchesJsonArray[endIndex] = matchesJsonArray[endIndex][:-1]

    #Prepend and Append curly braces where necessary
    for i in range(0, len(matchesJsonArray)):
      if i != 0 and i != endIndex:
        matchesJsonArray[i] = '{' + matchesJsonArray[i] + '}'
      elif i == 0:
        matchesJsonArray[i] = matchesJsonArray[i] + '}'
      elif i == endIndex:
        matchesJsonArray[i] = '{' + matchesJsonArray[i]

    self.logger.info("Successfully loaded Matches from Json: %s" %str(matchesJsonFile))
    return matchesJsonArray

    
