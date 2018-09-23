#!/bin/bash
#To do, use curl that uses HTTP status code, not YELLOW (200 good enough without needed indices)
echo "Creating Ephemeral Environment on Localhost..."
#This starts up the virtualenv
source ./.env
# #This starts up elasticsearch if we need it in the bg
~/elasticsearch-6.4.0/bin/elasticsearch -p /tmp/elasticsearch-pid -d &

#Every 3 s for 20 s we will curl for our elasticsearch's health
#When we get a YELLOW we break
START=`date +%s`
while [ $(( $(date +%s) - 20 )) -lt $START ]; do
  sleep 3
  HTTPSTATUS=`curl -s -o /dev/null -L -w "%{http_code}" -H "Accept: application/json" -H "Content-type: application/json" http://localhost:9200/_cluster/health`
  echo $HTTPSTATUS
  if [ $HTTPSTATUS -eq 200 ]; then
    echo "Elasticsearch Cluster Reached Healthy Status"
    break
  fi
  echo "No successful health check from Elasticsearch Cluster yet. Trying again..."
done

if [ $HTTPSTATUS -ne 200 ]; then
  echo "Elasticsearch Cluster Failed to Reach Healthy Status"
  echo "Skipping execution of driver function"
  source ./.deactivate-env
  return
fi

if [ $HTTPSTATUS -eq 200 ]; then
  echo "Elasticsearch Cluster Reached Healthy Status"
  echo "Execution of driver function"
  python main.py
fi
#Run your driver to insert data
