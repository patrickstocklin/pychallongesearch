#!/bin/bash
#This starts up the virtualenv
source ./.env

#This starts up elasticsearch if we need it in the bg
~/elasticsearch-6.4.0/bin/elasticsearch -p /tmp/elasticsearch-pid -d &

#Every 3 s for 20 s we will curl for our elasticsearch's health
#When we get a YELLOW we break
START=`date +%s`
while [ $(( $(date +%s) - 20 )) -lt $START ]; do
  sleep 3
  output=`curl -s -H "Accept: application/json" -H "Content-type: application/json" 'http://localhost:9200/_cluster/health'`
  echo $output | grep -q "yellow"
  health=$?
  if [ $health -eq 0 ]; then
    echo "Elasticsearch Cluster Reached Yellow Status"
    break
  fi
  echo "No successful health check from Elasticsearch Cluster yet. Trying again..."
done

if [ $health -eq 1 ]; then
  echo "Elasticsearch Cluster Failed to Reach Yellow Status"
  return
fi

#Run your driver to insert data
python main.py

#How to kill
pid=$(cat /tmp/elasticsearch-pid && echo)
echo "Shutting down Elasticsearch Cluster"
kill -SIGTERM $pid

