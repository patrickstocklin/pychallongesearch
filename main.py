# -*- coding: utf-8 -*-
from pychallongesearch import pychallongesearch as pcs

'''
CONSTANTS
'''

def main():
  print "Starting Main"
  pcsearch = pcs.PyChallongeSearch("127.0.0.1","9200")

  pcsearch.brackets.ingest_bracket();

  # pcsearch.stats.test()   //analysis 
  print "Done"

if __name__ == '__main__':
  main()