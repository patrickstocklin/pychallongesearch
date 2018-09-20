# -*- coding: utf-8 -*-
class update(object):

	def __init__(self, elasticsearch_client, logger):
		self.elasticsearch_client = elasticsearch_client
		self.logger = logger

	def test(self):
		self.logger.info("update test")