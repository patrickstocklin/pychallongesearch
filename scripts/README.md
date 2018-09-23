# How to Run

### Bring up virtualenv
```
~/pychallongesearch$ source .env
```
### Tear down virtualenv
```
~/pychallongesearch$ source .env
```
### Bring up virtualenv, elasticsearch, run deploy/driver.py
```
~/pychallongesearch$ source ./scripts/create_local_environment.sh
```
### Run all unittests against elasticsearch cluster
```
~/pychallongesearch$ source ./scripts/run_unit_tests.sh
```
### Tear down virtualenv, elasticsearch indices, clean up
```
~/pychallongesearch$ source ./scripts/teardown_local_environment.sh
```
### Kill elasticsearch cluster, no clean up
```
~/pychallongesearch$ source ./scripts/destroy_elasticsearch_cluster.sh
```
