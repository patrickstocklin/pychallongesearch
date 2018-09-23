# -*- coding: utf-8 -*-

############################################################################################################################
#
#    Matches Module:
#    Holds all Repository actions for a match data type (exists, insert, search, update, delete)
#
############################################################################################################################

class matches(object):

  MATCH_INDEX_NAME = str('matches')

  def __init__(self, parent):
    self.parent = parent
    self.elasticsearch_client = parent.elasticsearch_client
    self.logger = parent.logger

  '''
  Arg: winner id, loser id, match_json
  Abs: inserts into matches index
  Ret:

  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def insert_match(self, winner_id, loser_id, match_json):
    match_id = int(match_json['match']['id'])
    match_round = int(match_json['match']['id'])

    doc = {
            'id'  : match_id,
            'winner_id' : winner_id,
            'loser_id' : loser_id,
            'round' : match_id
    }

    self.logger.info('Inserting Match %s into Elasticsearch Cluster' %str(match_id))
    self.elasticsearch_client.index(index=self.MATCH_INDEX_NAME,
                                    doc_type='match', #Try to remember what this is for
                                    body=doc,
                                    id=int(match_id))
    return
