# -*- coding: utf-8 -*-

############################################################################################################################
#
#    Matches Module:
#    Holds all Repository actions for a match data type (exists, insert, search, update, delete)
#
############################################################################################################################

class matches(object):

	def __init__(self, parent):
		self.parent = parent
		self.elasticsearch_client = parent.elasticsearch_client
		self.logger = parent.logger
