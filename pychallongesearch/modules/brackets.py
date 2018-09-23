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

	#Given a directory, look at all of the tournaments, matches, and player files
	#M	Load contents and strip prepending tourney ID (name)
	#O	Merge sort 3 dirs according to ID ( order is 1, 10, 100, 101, 102 ... 109, 11, 110, 111, 112 ...)
	#V
	#E	def ingest(3 hashmaps of sorted json objects):
	#	if len of 3 items not equal, something is missing:
	#T		#set bool to warn
	#O
	#		for (list item in list of items):
	#C			#if item.ID != the others, continue without inserting and log it
	#F			readtourneyfromjson
	#U			readmatchesfromjson
	#s			readparticipantsfromjson
	#			ingest bracket()
	#Insert with the super special secret sauce algorithm (may require more work on query commands, spec. update and insert)

	def ingest_bracket(self):
		self.logger.info("ingesting bracket")


		self.parent.challongefileutils.test()