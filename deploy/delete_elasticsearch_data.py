# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/pat/smashdb/pychallongesearch") 
from pychallongesearch import pychallongesearch as pcs

'''
CONSTANTS
'''

def delete_elasticsearch_data():
  print "Deleting Elasticsearch Data"
  pcsearch = pcs.PyChallongeSearch("127.0.0.1","9200")
  pcsearch.indices.delete_elasticsearch_indices()
  print "Completed Deleting Tournament Data"

if __name__ == '__main__':
  delete_elasticsearch_data()