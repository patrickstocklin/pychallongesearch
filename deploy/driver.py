# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/pat/smashdb/pychallongesearch") 
from pychallongesearch import pychallongesearch as pcs

'''
CONSTANTS
'''

def driver():
  print "Running Driver"
  pcsearch = pcs.PyChallongeSearch("127.0.0.1","9200")
  pcsearch.indices.create_elasticsearch_indices()
  pcsearch.brackets.ingest_series("/home/pat/smashdb/data/tournaments/MNM")
  print "Exiting Driver"

if __name__ == '__main__':
  driver()