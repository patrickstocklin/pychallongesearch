# -*- coding: utf-8 -*-
from utils import challongefileutils
from modules import indices
from modules import brackets
from modules import query
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
#    1) challongefileutils, help me look at a bracket, split the contents into digestible bits, then insert
#	 2) Work out query, then bracket (ingest)
#
#	 Nice to haves:
#    Do we store constants somewhere?
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
		self.elasticsearch_client = Elasticsearch([host + ":" + port])
		self.health_check()

		#Indices, Brackets (ingest), Query (search/retrieve, insert, update, delete), Stats
		self.indices = indices.indices(self)
		self.brackets = brackets.brackets(self)
		self.query = query.query(self)
		self.stats = stats.stats(self)

		###################################################################
		# FILESYSTEM HELPER FUNCTIONS (should take in a directory arg tbh)
		###################################################################
		self.challongefileutils = challongefileutils.challongefileutils(self)

	def health_check(self):
		if(self.elasticsearch_client.cluster.health()):
			self.logger.info("Cluster is healthy!")
		else:
			raise Exception("Cluster is not healthy!")