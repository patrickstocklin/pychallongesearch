# -*- coding: utf-8 -*-
from pychallongesearch import pychallongesearch as pcs
from pychallongesearch import fileutils

'''
CONSTANTS
'''

def main():
	print "Starting Main"
	pcsearch = pcs.PyChallongeSearch("127.0.0.1","9200")

	# pcsearch.indices.create_elasticsearch_indices()
	pcsearch.brackets.ingest_bracket();
	# pcsearch.indices.delete_elasticsearch_indices()

	# pcsearch.stats.test()   //analysis 


if __name__ == '__main__':
	main()