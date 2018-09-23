# -*- coding: utf-8 -*-
from pychallongesearch import pychallongesearch as pcs

'''
CONSTANTS
'''

def main():
  print "Starting Main"
  pcsearch = pcs.PyChallongeSearch("127.0.0.1","9200")

  # pcsearch.indices.create_elasticsearch_indices()

  #should actually be called from within .brackets.ingest_bracket
  #pcsearch.challongefileutils.readTournamentJson("/home/pat/smashdb/data/tournaments/MNM/tournaments/MNM-1-tournament.json")
  #pcsearch.challongefileutils.readParticipantsJson("/home/pat/smashdb/data/tournaments/MNM/participants/MNM-1-participants.json")
  #pcsearch.challongefileutils.readParticipantsJson("/home/pat/smashdb/data/tournaments/MNM/matches/MNM-1-matches.json")


  pcsearch.brackets.ingest_bracket();
  # pcsearch.indices.flush_elasticsearch_indices()
  pcsearch.indices.delete_elasticsearch_indices()
  pcsearch.indices.create_elasticsearch_indices()


  # pcsearch.stats.test()   //analysis 
  print "Done"

if __name__ == '__main__':
  main()