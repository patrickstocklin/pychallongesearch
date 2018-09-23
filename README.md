# PyChallongeSearch

![Python](./doc/img/python.png)![Challonge](./doc/img/challonge.png)![ES](./doc/img/elasticsearch.png)

## A Python Wrapper for Challonge Brackets in Elasticsearch

## Requirements
* virtualenv
* elasticsearch
* challonge data (see [here](https://github.com/patrickstocklin/challonge-scraper))

## Local Environment 
### Setup
```
~/$ git clone https://github.com/patrickstocklin/pychallongesearch.git
~/$ virtualenv --no-site-packages pychallongesearch

~/$ cd pychallongesearch

#Initial Virtualenv Setup
~/pychallongesearch$ source .env
(pychallongesearch)~/pychallongesearch$ pip install -r requirements.txt
~/pychallongesearch$ source .deactivate-env
```
### Creation
```
~/pychallongesearch$ source ./scripts/create_local_environment.sh
```

### Elasticsearch Health Check
```
(pychallongesearch)~/pychallongesearch$ source ./scripts/health_check.sh
```

### Run Tests
```
(pychallongesearch)~/pychallongesearch$ source ./scripts/run_unit_tests.sh
```

### Teardown
```
(pychallongesearch)~/pychallongesearch$ source ./scripts/teardown_local_environment.sh
```

### Disaster Scenario (Killed Elasticsearch Cluster)
```
(pychallongesearch)~/pychallongesearch$ source ./scripts/destroy_elasticsearch_cluster.sh
```
