# -*- coding: utf-8 -*-
class search(object):

	def __init__(self, elasticsearch_client, logger):
		self.elasticsearch_client = elasticsearch_client
		self.logger = logger

	def test(self):
		self.logger.info("search test")