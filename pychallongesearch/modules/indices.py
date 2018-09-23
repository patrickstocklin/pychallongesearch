# -*- coding: utf-8 -*-

############################################################################################################################
#
#
#
############################################################################################################################

class indices(object):

	#Maybe move these elsewhere
	TOURNAMENT_INDEX_NAME = 'tournaments'
	PLAYER_INDEX_NAME = 'players'
	MATCH_INDEX_NAME = 'matches'

	def __init__(self, parent):
		self.parent = parent
		self.elasticsearch_client = parent.elasticsearch_client
		self.logger = parent.logger

	def test(self):
		self.logger.info("indices test")

	def create_elasticsearch_indices(self):
		self.logger.info("creating elasticsearch indices")
		
		if not self.elasticsearch_client.indices.exists(index=self.TOURNAMENT_INDEX_NAME):
			self.elasticsearch_client.indices.create(index=self.TOURNAMENT_INDEX_NAME)
			self.logger.info('index with name %s created in elasticsearch' %str(self.TOURNAMENT_INDEX_NAME))

		if not self.elasticsearch_client.indices.exists(index=self.PLAYER_INDEX_NAME):
			self.elasticsearch_client.indices.create(index=self.PLAYER_INDEX_NAME)
			self.logger.info('index with name %s created in elasticsearch' %str(self.PLAYER_INDEX_NAME))

		if not self.elasticsearch_client.indices.exists(index=self.MATCH_INDEX_NAME):
			self.elasticsearch_client.indices.create(index=self.MATCH_INDEX_NAME)
			self.logger.info('index with name %s created in elasticsearch' %str(self.MATCH_INDEX_NAME))

	def flush_elasticsearch_indices(self):
		self.logger.info('flushing elasticsearch indices')

		if self.elasticsearch_client.indices.exists(index=self.TOURNAMENT_INDEX_NAME):
			self.elasticsearch_client.indices.flush(index=self.TOURNAMENT_INDEX_NAME)
			self.logger.info('index with name %s flushed in elasticsearch' %str(self.TOURNAMENT_INDEX_NAME))

		if self.elasticsearch_client.indices.exists(index=self.PLAYER_INDEX_NAME):
			self.elasticsearch_client.indices.flush(index=self.PLAYER_INDEX_NAME)
			self.logger.info('index with name %s flushed in elasticsearch' %str(self.PLAYER_INDEX_NAME))

		if self.elasticsearch_client.indices.exists(index=self.MATCH_INDEX_NAME):
			self.elasticsearch_client.indices.flush(index=self.MATCH_INDEX_NAME)
			self.logger.info('index with name %s flushed in elasticsearch' %str(self.MATCH_INDEX_NAME))

	def delete_elasticsearch_indices(self):
		self.logger.info('destroying elasticsearch indices')

		if self.elasticsearch_client.indices.exists(index=self.TOURNAMENT_INDEX_NAME):
			self.elasticsearch_client.indices.delete(index=self.TOURNAMENT_INDEX_NAME)
			self.logger.info('index with name %s deleted in elasticsearch' %str(self.TOURNAMENT_INDEX_NAME))

		if self.elasticsearch_client.indices.exists(index=self.PLAYER_INDEX_NAME):
			self.elasticsearch_client.indices.delete(index=self.PLAYER_INDEX_NAME)
			self.logger.info('index with name %s deleted in elasticsearch' %str(self.PLAYER_INDEX_NAME))

		if self.elasticsearch_client.indices.exists(index=self.MATCH_INDEX_NAME):
			self.elasticsearch_client.indices.delete(index=self.MATCH_INDEX_NAME)
			self.logger.info('index with name %s deleted in elasticsearch' %str(self.MATCH_INDEX_NAME))
