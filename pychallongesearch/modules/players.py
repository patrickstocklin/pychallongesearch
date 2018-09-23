# -*- coding: utf-8 -*-

############################################################################################################################
#
#    Players Module:
#    Holds all Repository actions for a player data type (exists, insert, search, update, delete)
#
#    A participant becomes a player when it is inserted from a bracket into ES
#
############################################################################################################################

class players(object):

  PLAYER_INDEX_NAME = str('players')
  CLAN_TAG_SPLIT_CHAR = str('|')

  def __init__(self, parent):
    self.parent = parent
    self.elasticsearch_client = parent.elasticsearch_client
    self.logger = parent.logger

  '''
  Arg: player_tag
  Abs: retrieves '['hits']['total']' of json response of method search_for_player_by_tag
  Ret: Boolean

  TO DO: Type Null validation of player_tag argument always done before client_query
  '''
  def exists_by_player_tag(self, player_tag):
    res = self.search_for_player_by_tag(player_tag)
    return True if res['hits']['total'] >= 1 else False


  '''
  Arg: player_id
  Abs: retrieves result response from es cluster client's match query by player tag
  Ret: res json

  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def search_for_player_by_id(self, player_id):
    self.elasticsearch_client.indices.refresh(index=self.PLAYER_INDEX_NAME)
    if player_id is not None:
      res = self.elasticsearch_client.search(index=self.PLAYER_INDEX_NAME,
                                              doc_type='player',
                                              body={'query'
                                                    :{'match'
                                                      :{'id'
                                                        : player_id}}})
    return res

  '''
  Arg: player_tag
  Abs: retrieves result response from es cluster client's match query by player tag
  Ret: res json

  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def search_for_player_by_tag(self, player_tag):
    self.elasticsearch_client.indices.refresh(index=self.PLAYER_INDEX_NAME)
    if player_tag is not None:
      res = self.elasticsearch_client.search(index=self.PLAYER_INDEX_NAME,
                                              doc_type='player',
                                              body={'query'
                                                    :{'match'
                                                      :{'tag'
                                                        : player_tag}}})
    return res

  '''
  Arg: player_json
  Abs: inserts into players doc
  Ret:

  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def insert_player(self, player_json):
    player_tag = self.parent.challongefileutils.mapUnfriendlyPlayerTag(player_json['participant']['name'])
    player_id = int(player_json['participant']['id'])
    tournament_id = int(player_json['participant']['tournament_id'])
    seedings_dict = {tournament_id:int(player_json['participant']['seed'])}
    placings_dict = {tournament_id:int(player_json['participant']['final_rank'])}

    if self.CLAN_TAG_SPLIT_CHAR in player_tag:
      player_tag = str(player_tag).split(self.CLAN_TAG_SPLIT_CHAR)[1].strip()

    doc = {
            'id'  : player_id,
            'tag' : player_tag,
            'seedings' : seedings_dict,
            'placings' : placings_dict,
            'tournaments' : [tournament_id],
            'matches' : []
    }

    self.logger.info('Inserting Participant %s into Elasticsearch Cluster' %str(player_tag))
    self.elasticsearch_client.index(index=self.PLAYER_INDEX_NAME,
                                    doc_type='player', #Try to remember what this is for
                                    body=doc,
                                    id=int(player_json['participant']['id']))
    return

  '''
  Arg: player_json
  Abs: retrieves result from response
  Ret: res int
  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def retrieve_player_id(self, player_json):
    if player_json['hits']['total'] > 0:
      return int(player_json['hits']['hits'][0]['_source']['id'])

  '''
  Arg: player_json
  Abs: retrieves result from response
  Ret: res int
  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def retrieve_player_seedings(self, player_json):
    if player_json['hits']['total'] > 0:
      return player_json['hits']['hits'][0]['_source']['seedings']

  '''
  Arg: player_json
  Abs: retrieves result from response
  Ret: res int
  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def retrieve_player_placings(self, player_json):
    if player_json['hits']['total'] > 0:
      return player_json['hits']['hits'][0]['_source']['placings']

  '''
  Arg: player_json
  Abs: retrieves result from response
  Ret: res int
  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def retrieve_player_tournaments(self, player_json):
    if player_json['hits']['total'] > 0:
      return player_json['hits']['hits'][0]['_source']['tournaments']


  '''
  Arg: player_tag
  Abs: retrieves result response from es cluster client's match query by player tag
  Ret: res int
  TO DO: Perform all index refreshes in final call just before all match queries
  '''
  def update_player_seedings_and_placings(self, player_id, player_json):
    #self.logger.info("updating seedings and placings for player_id: %s" %str(player_id))
    target_player_json = self.search_for_player_by_id(player_id)
    target_player_tournaments = self.retrieve_player_tournaments(target_player_json)
    target_player_seedings = self.retrieve_player_seedings(target_player_json)
    target_player_placings = self.retrieve_player_placings(target_player_json)
    print target_player_json['hits']['hits'][0]['_source']['tag']
    print target_player_seedings
    print target_player_placings
