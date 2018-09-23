#How to kill
python deploy/delete_elasticsearch_data.py

pid=$(cat /tmp/elasticsearch-pid && echo)
echo "Shutting down Elasticsearch Cluster"
kill -SIGTERM $pid
deactivate