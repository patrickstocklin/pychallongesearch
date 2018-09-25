# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/pat/smashdb/pychallongesearch") 
from pychallongesearch import pychallongesearch as pcs

'''
CONSTANTS
'''

def ingest_tournament_data():
  print "Ingesting Tournament Data"
  pcsearch = pcs.PyChallongeSearch("127.0.0.1","9200")
  pcsearch.indices.create_elasticsearch_indices()
  #pcsearch.brackets.ingest_bracket();
  
  #some quick way to do the listDirs testing, remove later


  print "Completed Inserting Tournament Data"

if __name__ == '__main__':
  ingest_tournament_data()