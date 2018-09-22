# -*- coding: utf-8 -*-

############################################################################################################################
#
# INSERT, RETRIEVE, RETRIEVE FIELD, SEARCH, UPDATE
#
############################################################################################################################

class query(object):

	def __init__(self, parent):
		self.parent = parent
		self.elasticsearch_client = parent.elasticsearch_client
		self.logger = parent.logger

	def test(self):
		self.logger.info("retrieve test")