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

	def __init__(self, parent):
		self.parent = parent
		self.elasticsearch_client = parent.elasticsearch_client
		self.logger = parent.logger

