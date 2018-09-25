# -*- coding: utf-8 -*-
import json

############################################################################################################################
#
#  
#
############################################################################################################################

class brackets(object):

  #Maybe move these elsewhere
  TOURNAMENT_INDEX_NAME = 'tournaments'
  PLAYER_INDEX_NAME = 'players'
  MATCH_INDEX_NAME = 'matches'

  def __init__(self, parent):
    self.parent = parent
    self.elasticsearch_client = parent.elasticsearch_client
    self.logger = parent.logger

  #Given a directory, look at all of the tournaments, matches, and player files
  #M  Load contents and strip prepending tourney ID (name)
  #O  Merge sort 3 dirs according to ID ( order is 1, 10, 100, 101, 102 ... 109, 11, 110, 111, 112 ...)
  #V
  #E  def ingest(3 hashmaps of sorted json objects):
  #  if len of 3 items not equal, something is missing:
  #T    #set bool to warn
  #O
  #    for (list item in list of items):
  #C      #if item.ID != the others, continue without inserting and log it
  #F      readtourneyfromjson
  #U      readmatchesfromjson
  #s      readparticipantsfromjson
  #      ingest bracket()
  #Insert with the super special secret sauce algorithm (may require more work on query commands, spec. update and insert)

  # For tournamentDir under ~/data/tournaments:
      # tA, pA, mA = fileutils.readBrack

    #  tournamentsarr, participantsarr, matchesarr = self.parent.challongefileutils.readBracketFromDirectory(String directory):
      #          find all jsons, insert 
      #          []
      #
      #
      #
      #
    # MOVE THESE
    # MOVE THESE
    # MOVE THESE

  def ingest_series(self, targetDirectory):
  	sortedMatchesDict, sortedParticipantsDict, sortedTournamentsDict = self.parent.challongefileutils.createSortedDictsOfFilesInTournamentSeriesDirectory(targetDirectory)

  	if len(sortedMatchesDict) == len(sortedParticipantsDict) == len(sortedTournamentsDict):
			for i in xrange(0, len(sortedMatchesDict)):
				print "------------------------------------"
				print sortedMatchesDict[i][1]
				print sortedParticipantsDict[i][1]
				print sortedTournamentsDict[i][1]
				self.ingest_bracket(sortedMatchesDict[i][1], sortedParticipantsDict[i][1], sortedTournamentsDict[i][1])

  # Given: 3 filepaths to bracket's jsons
  #
  #
  def ingest_bracket(self, targetMatchesJsonFile, targetParticipantsJsonFile, targetTournamentJsonFile):
    self.logger.info("ingesting bracket")

    matches_arr = self.parent.challongefileutils.readMatchesJson(targetMatchesJsonFile)
    participants_arr = self.parent.challongefileutils.readParticipantsJson(targetParticipantsJsonFile)
    tournament_arr = self.parent.challongefileutils.readTournamentJson(targetTournamentJsonFile)

    participants_old_ids = list()
    participants_new_ids = list()
    participants_old_player_ids_dict = dict()
    #list of participant/player ids and matches to store in tournament obj
    tournament_participants = list()
    tournament_matches = list()

    for participant in participants_arr:

      participant_json = json.loads(participant)
      participant_tag = self.parent.challongefileutils.mapUnfriendlyPlayerTag(participant_json['participant']['name'])

      if not self.parent.players.exists_by_player_tag(participant_tag):
        self.parent.players.insert_player(participant_json)
        participant_new_id = int(participant_json['participant']['id'])
        participants_new_ids.append(participant_new_id)
        tournament_participants.append(participant_new_id)

      elif self.parent.players.exists_by_player_tag(participant_tag):
        target_player = self.parent.players.search_for_player_by_tag(participant_tag)
        player_id = self.parent.players.retrieve_player_id(target_player)
        participant_old_id = int(participant_json['participant']['id'])
        self.parent.players.update_player_seedings_and_placings(player_id, participant_json)
        participants_old_player_ids_dict[participant_old_id] = player_id
        participants_old_ids.append(participant_old_id)
        tournament_participants.append(player_id)

    for match in matches_arr:
      match_json = json.loads(match)
      match_id = int(match_json['match']['id'])
      winner_id = int(match_json['match']['winner_id'])
      loser_id = int(match_json['match']['loser_id'])

      if winner_id in participants_new_ids and loser_id in participants_new_ids:
        self.parent.matches.insert_match(winner_id, loser_id, match_json)
        #self.parent.players.update_player_matches(winner_id, match_json)
        #self.parent.players.update_player_matches(loser_id, match_json)
        tournament_matches.append(match_id)

      elif winner_id in participants_new_ids and loser_id not in participants_new_ids:
        loser_existing_player_id = participants_old_player_ids_dict[loser_id]
        self.parent.matches.insert_match(winner_id, loser_existing_player_id, match_json)
        #self.parent.players.update_player_matches(winner_id, match_json)
        #self.parent.players.update_player_matches(loser_existing_player_id, match_json)
        tournament_matches.append(match_id)

      elif winner_id not in participants_new_ids and loser_id in participants_new_ids:
        winner_existing_player_id = participants_old_player_ids_dict[winner_id]
        self.parent.matches.insert_match(winner_existing_player_id, loser_id, match_json)
        #self.parent.players.update_player_matches(winner_existing_player_id, match_json)
        #self.parent.players.update_player_matches(loser_id, match_json)
        tournament_matches.append(match_id)

      elif winner_id in participants_old_ids and loser_id in participants_old_ids:
        winner_existing_player_id = participants_old_player_ids_dict[winner_id]
        loser_existing_player_id = participants_old_player_ids_dict[loser_id]
        self.parent.matches.insert_match(winner_existing_player_id, loser_existing_player_id, match_json)
        #self.parent.players.update_player_matches(winner_existing_player_id, match_json)
        #self.parent.players.update_player_matches(loser_existing_player_id, match_json)
        tournament_matches.append(match_id)

    tournament_json = json.loads(tournament_arr[0])
    self.parent.tournaments.insert_tournament(tournament_json, tournament_participants, tournament_participants)
    return