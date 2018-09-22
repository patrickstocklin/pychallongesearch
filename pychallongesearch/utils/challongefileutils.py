# -*- coding: utf-8 -*-

############################################################################################################################
#
# Helps us with handling the Challonge JSONs we just downloaded
#
############################################################################################################################

class challongefileutils(object):

	def __init__(self, parent):
		self.parent = parent
		self.logger = parent.logger
		self.logger.info("challongefileutils created")

	def test(self):
		self.logger.info("challongefileutils testtt")
