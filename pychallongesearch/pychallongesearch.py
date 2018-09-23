# -*- coding: utf-8 -*-
from utils import challongefileutils
from modules import indices
from modules import brackets
from modules import tournaments
from modules import players
from modules import matches
from modules import stats
from elasticsearch import Elasticsearch
import json
import logging

'''
############################################################################################################################
#    PyChallongeSearch
#
#    Author: Patrick C. Stocklin
#	
#        Python Wrapper to handle the creation, insertion, updating, and searching of player, tournament, and match stats
#    within an Elasticsearch cluster. Useful for analysis across an aggregated collection of double-elimination Challonge 
#    Brackets.
#
#	 TO DO:
#	 1) Work out query, then bracket (ingest)
#
#	 Nice to haves:
#    Do we store constants somewhere? Index Names, Target Dir, Etc Etc
#
############################################################################################################################
'''

class PyChallongeSearch(object):

	def __init__(self, host, port):

		##################################################################
		# LOGGING
		##################################################################
		self.logger = logging.getLogger('PyChallongeSearch')
		self.logger.setLevel(logging.INFO)

		fh = logging.FileHandler('pychallongesearch.log')
		fh.setLevel(logging.INFO)
		self.logger.addHandler(fh)

		ch = logging.StreamHandler()
		self.logger.addHandler(ch)

		##################################################################
		# CLIENT AND MODULES
		##################################################################
		self.elasticsearch_client = Elasticsearch([host + ":" + port], timeout = 3)
		self.health_check()

		#Indices, Brackets (ingest), Query (search/retrieve, insert, update, delete), Stats
		self.indices = indices.indices(self)
		#Have a module for each Data Obj (bracket, tournament, match, participant) and 
		self.brackets = brackets.brackets(self)
		self.tournaments = tournaments.tournaments(self)
		self.matches = matches.matches(self)
		self.players = players.players(self)
		#Have a module for various stat queries that fall outside of a domain object
		self.stats = stats.stats(self)
		
		###################################################################
		# FILESYSTEM HELPER FUNCTIONS (should take in a directory arg tbh)
		###################################################################
		self.challongefileutils = challongefileutils.challongefileutils(self)

	def health_check(self):
		if(self.elasticsearch_client.cluster.health(wait_for_status='yellow', request_timeout=3)):
			self.logger.info("Cluster is healthy!")
		else:
			raise Exception("Cluster is not healthy!")