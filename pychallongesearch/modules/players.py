# -*- coding: utf-8 -*-

############################################################################################################################
#
#    Players Module:
#    Holds all Repository actions for a player data type (exists, insert, search, update, delete)
#
############################################################################################################################

class players(object):

	def __init__(self, parent):
		self.parent = parent
		self.elasticsearch_client = parent.elasticsearch_client
		self.logger = parent.logger
