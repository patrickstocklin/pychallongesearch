# -*- coding: utf-8 -*-

############################################################################################################################
#
#
#
############################################################################################################################

class stats(object):

	def __init__(self, elasticsearch_client, logger):
		self.elasticsearch_client = elasticsearch_client
		self.logger = logger

	def test(self):
		self.logger.info("stats test")