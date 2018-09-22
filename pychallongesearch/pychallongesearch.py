# -*- coding: utf-8 -*-
from utils import challongefileutils
from modules import indices
from modules import brackets
from modules import stats
from modules import query
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
		#Do a healthcheck, fail if bad conn

		### ADD OTHER MODULES HERE

		#Indices, Brackets (ingest), Query (search/retrieve, insert, update, delete), Stats
		self.indices = indices.indices(self.elasticsearch_client, self.logger)
		self.brackets = brackets.brackets(self.elasticsearch_client, self.logger)
		self.stats = stats.stats(self.elasticsearch_client, self.logger)
		self.query = query.query(self.elasticsearch_client, self.logger)
