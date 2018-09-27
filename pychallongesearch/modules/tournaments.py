# -*- coding: utf-8 -*-

############################################################################################################################
#
#    Tournaments Module:
#    Holds all Repository actions for a tournaments data type (exists, insert, search, update, delete)
#
#    Note: This is entirely different from the Bracket Module; Bracket module is parent domain object that holds all
#    important information regarding a bracket's players, matches, and tournament information. Tournament domain object
#    does not include information like player performance or match history until it is inserted into ES with a list of 
#    match ids and player ids
#
############################################################################################################################

class tournaments(object):

  TOURNAMENT_INDEX_NAME = str('tournaments')

  def __init__(self, parent):
    self.parent = parent
    self.elasticsearch_client = parent.elasticsearch_client
    self.logger = parent.logger

  '''
  Arg: tournament json, tournament participants list, tournament matches list
  Abs: inserts into tournaments doc
  Ret:

  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def insert_tournament(self, tournament_json, tournament_participants, tournament_matches):
    tournament_id = int(tournament_json['tournament']['id'])
    tournament_name = str(tournament_json['tournament']['name'])
    tournament_url = str(tournament_json['tournament']['full_challonge_url'])
    tournament_participant_count = int(tournament_json['tournament']['participants_count'])
    tournament_date = str(tournament_json['tournament']['created_at'])

    #Get rid of these, testing
    # tournament_matches = []
    # tournament_participants = []

    doc = {
            'id' : tournament_id,
            'name' : tournament_name,
            'url' : tournament_url,
            'date' : tournament_date,
            'num_of_participants' : tournament_participant_count,
            'participants' : tournament_participants,
            'matches' : tournament_matches
    }

    self.logger.info('Inserting Tournament %s into Elasticsearch Cluster' %str(tournament_id))
    self.elasticsearch_client.index(index=self.TOURNAMENT_INDEX_NAME,
                                    doc_type='tournament', #Try to remember what this is for
                                    body=doc,
                                    id=int(tournament_id))
    return
