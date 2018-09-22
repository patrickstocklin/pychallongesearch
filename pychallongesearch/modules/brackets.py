# -*- coding: utf-8 -*-

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

	def test(self):
		self.logger.info("indices test")

	def ingest_bracket(self):
		self.logger.info("ingesting bracket")
		self.parent.challongefileutils.test()