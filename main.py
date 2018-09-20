# -*- coding: utf-8 -*-
from pychallongesearch import pychallongesearch as pcs
from pychallongesearch import fileutils

'''
CONSTANTS
'''

def main():
	print "Starting Main"
	pcsearch = pcs.PyChallongeSearch("127.0.0.1","9200")
	#work on better names
	# pcsearch.indices.test() //For working with creating and deleting indices
	# pcsearch.ingest.test()  //rename to pcsearch.bracket.ingest for inserting a bracket obj
	# pcsearch.insert.test()  //CRUD insert
	# pcsearch.retrieve.test()//CRUD read
	# pcsearch.search.test()  //CRUD read
	# pcsearch.stats.test()   //analysis 
	# pcsearch.update.test()  //CRUD update
	
	# pcsearch.indices.create_elasticsearch_indices()
	# pcsearch.exist.index_exists("players")
	# pcsearch.exist.index_exists("tournaments")
	# pcsearch.exist.index_exists("matches")
	# pcsearch.indices.delete_elasticsearch_indices()

	#pcsearch.exist.player_exists("play")


if __name__ == '__main__':
	main()